from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from src.utils.model_registry import get_model
from src.utils.parser import extract_code
from src.config import DEFAULT_MODELS

class CoAState(TypedDict):
    problem: str
    segments: List[str]
    current_idx: int
    test_code: str

def manager_node(state: CoAState, model: str):
    llm = get_model(model, temperature=0.1)
    prompt = (
        "Analyze the following function and identify 3 critical testing dimensions (e.g., 'Boundary Values', 'Type Scenarios', 'Logic Branches').\n"
        "Output ONLY the three dimensions separated by semicolons.\n"
        f"Function:\n{state['problem']}"
    )
    res = llm.invoke(prompt)
    segments = [s.strip() for s in res.content.split(";")]
    return {"segments": segments, "current_idx": 0, "test_code": "import pytest\nimport math\n"}

def worker_node(state: CoAState, model: str):
    llm = get_model(model)
    focus = state["segments"][state["current_idx"]]
    prompt = (
        f"Generate 2-3 pytest functions focusing EXCLUSIVELY on the '{focus}' dimension of the function below.\n"
        "RULES:\n"
        "1. Output ONLY the test function code. No imports, no explanations.\n"
        "2. DO NOT RE-DEFINE the function under test.\n"
        "3. Assume the function is already in the local scope.\n\n"
        f"Function:\n{state['problem']}\n\nTests:"
    )
    res = llm.invoke(prompt)
    new_code = extract_code(res.content)
    return {"test_code": state["test_code"] + f"\n\n# Focus: {focus}\n" + new_code, 
            "current_idx": state["current_idx"] + 1}

def setup_coa_graph(manager_model: str = None, worker_model: str = None):
    cfg = DEFAULT_MODELS["coa"]
    manager_model = manager_model or cfg["manager_model"]
    worker_model  = worker_model  or cfg["worker_model"]
    workflow = StateGraph(CoAState)
    workflow.add_node("manager", lambda s: manager_node(s, manager_model))
    workflow.add_node("worker",  lambda s: worker_node(s, worker_model))

    workflow.set_entry_point("manager")
    workflow.add_edge("manager", "worker")

    def should_continue(state: CoAState):
        return "worker" if state["current_idx"] < len(state["segments"]) else END

    workflow.add_conditional_edges("worker", should_continue)
    return workflow.compile()
