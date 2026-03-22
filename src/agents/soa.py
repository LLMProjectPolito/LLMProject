from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from src.utils.model_registry import get_model
from src.utils.parser import extract_code
from src.config import DEFAULT_MODELS

class SOAState(TypedDict):
    problem: str
    specialists: List[str]
    test_code: str

def orchestrator_node(state: SOAState, model: str):
    llm = get_model(model, temperature=0.1)
    prompt = (
        "Analyze the following problem and identify the required expertise: 'math', 'string', 'collections', or 'logic'.\n"
        "Output ONLY the comma-separated keywords.\n"
        f"Problem:\n{state['problem']}"
    )
    res = llm.invoke(prompt)
    return {"specialists": [s.strip() for s in res.content.split(",")]}

def specialist_node(state: SOAState, model: str, reasoning_style: str = "zero_shot"):
    llm = get_model(model)
    from src.utils.prompts import apply_reasoning_style
    expertise = ", ".join(state["specialists"])
    base_instr = f"You are an expert specialist in {expertise}. Write a comprehensive pytest suite for the function below. Output ONLY code. DO NOT re-define the function."
    
    prompt = apply_reasoning_style(state['problem'], base_instr, reasoning_style)
    res = llm.invoke(prompt)
    return {"test_code": extract_code(res.content)}

def setup_soa_graph(orchestrator_model: str = None, specialist_model: str = None, reasoning_style: str = "zero_shot"):
    cfg = DEFAULT_MODELS["soa"]
    orchestrator_model = orchestrator_model or cfg["orchestrator_model"]
    specialist_model   = specialist_model   or cfg["specialist_model"]
    workflow = StateGraph(SOAState)
    workflow.add_node("orchestrator", lambda s: orchestrator_node(s, orchestrator_model))
    workflow.add_node("specialist",   lambda s: specialist_node(s, specialist_model, reasoning_style))
    workflow.set_entry_point("orchestrator")
    workflow.add_edge("orchestrator", "specialist")
    workflow.add_edge("specialist", END)
    return workflow.compile()
