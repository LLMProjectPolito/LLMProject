from langchain_core.prompts import PromptTemplate
from langgraph.graph import StateGraph, END
from typing import TypedDict
from src.utils.model_registry import get_model
from src.utils.parser import extract_code
from src.utils.prompts import apply_reasoning_style
from src.config import DEFAULT_MODELS

class AgentState(TypedDict):
    problem: str
    test_code: str
    feedback: str
    iterations: int

def driver_node(state: AgentState, model: str, reasoning_style: str = "zero_shot"):
    llm = get_model(model)
    if state.get("feedback"):
        instruction = f"Refine the following pytest suite based on this review: {state['feedback']}\n\nCurrent Tests:\n{state.get('test_code', '')}"
    else:
        instruction = "Write a comprehensive pytest suite for the given function. Include edge cases."
    
    prompt = apply_reasoning_style(state["problem"], instruction, reasoning_style)

    res = llm.invoke(prompt)
    return {"test_code": extract_code(res.content), "iterations": state.get("iterations", 0) + 1}

def navigator_node(state: AgentState, model: str):
    llm = get_model(model)
    prompt = PromptTemplate.from_template(
        "You are a Code Reviewer. Review these tests for logic errors, missing edge cases, or redundant checks.\n"
        "If they are excellent, reply with ONLY the word: PASSED\n"
        "Otherwise, provide a bulleted list of specific improvements.\n\n"
        "Tests:\n{test_code}"
    )
    res = llm.invoke(prompt.format(test_code=state["test_code"]))
    return {"feedback": res.content.strip()}

def setup_actor_critic_graph(driver_model: str = None, navigator_model: str = None, reasoning_style: str = "zero_shot"):
    cfg = DEFAULT_MODELS["actor_critic"]
    driver_model    = driver_model    or cfg["driver_model"]
    navigator_model = navigator_model or cfg["navigator_model"]
    workflow = StateGraph(AgentState)
    workflow.add_node("driver",    lambda s: driver_node(s, driver_model, reasoning_style))
    workflow.add_node("navigator", lambda s: navigator_node(s, navigator_model))

    workflow.set_entry_point("driver")
    workflow.add_edge("driver", "navigator")

    def decider(state: AgentState):
        if "PASSED" in state["feedback"].upper() or state["iterations"] >= 3:
            return END
        return "driver"

    workflow.add_conditional_edges("navigator", decider)
    return workflow.compile()
