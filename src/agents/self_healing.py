import time
from typing import TypedDict
from langgraph.graph import StateGraph, END

from src.utils.model_registry import get_model
from src.utils.parser import extract_code
from src.utils.executor import run_tests
from src.config import DEFAULT_MODELS

class SelfHealingState(TypedDict):
    problem: str
    test_code: str
    error_message: str
    iteration: int

def generate_node(state: SelfHealingState, model: str, reasoning_style: str = "zero_shot"):
    llm = get_model(model, temperature=0.7)
    from src.utils.prompts import apply_reasoning_style
    base_instr = "Write a comprehensive pytest suite for the function below. Output ONLY python code. DO NOT re-define the function."
    prompt = apply_reasoning_style(state['problem'], base_instr, reasoning_style)

    if state.get("iteration", 0) > 0: 
        time.sleep(2)

    res = llm.invoke(prompt)
    return {
        "test_code": extract_code(res.content), 
        "iteration": state.get("iteration", 0) + 1
    }

def execute_node(state: SelfHealingState):
    metrics = run_tests(state["problem"], state["test_code"])
    if metrics["errors"] > 0 or metrics["failed"] > 0:
        err = metrics.get("raw_output", "Syntax Error or Test Failure")
        err = err[-1500:] 
        return {"error_message": err}
    else:
        return {"error_message": ""}

def fix_node(state: SelfHealingState, model: str, reasoning_style: str = "zero_shot"):
    llm = get_model(model, temperature=0.2)
    from src.utils.prompts import apply_reasoning_style
    
    context = f"Function:\n{state['problem']}\n\nBroken Test Code:\n{state['test_code']}\n\nError:\n{state['error_message']}"
    base_instr = "The pytest suite above failed. Fix the errors and output ONLY the complete fixed Python code. DO NOT re-define the function."
    
    prompt = apply_reasoning_style(context, base_instr, reasoning_style)
    time.sleep(2)
    res = llm.invoke(prompt)
    return {
        "test_code": extract_code(res.content),
        "iteration": state.get("iteration", 0) + 1,
        "error_message": ""
    }

def setup_self_healing_graph(model: str = None, max_iterations: int = 3, reasoning_style: str = "zero_shot"):
    cfg = DEFAULT_MODELS.get("self_healing", {})
    model = model or cfg.get("model", "llama3-8b")
    
    workflow = StateGraph(SelfHealingState)

    workflow.add_node("generate", lambda s: generate_node(s, model, reasoning_style))
    workflow.add_node("execute", execute_node)
    workflow.add_node("fix",      lambda s: fix_node(s, model, reasoning_style))

    workflow.set_entry_point("generate")
    workflow.add_edge("generate", "execute")

    def router(state: SelfHealingState):
        if not state.get("error_message"): return END
        if state.get("iteration", 0) >= max_iterations: return END
        return "fix"

    workflow.add_conditional_edges("execute", router)
    workflow.add_edge("fix", "execute")

    return workflow.compile()
