import time
from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from src.utils.model_registry import get_model
from src.utils.parser import extract_code
from src.config import DEFAULT_MODELS

class AtomicSwarmState(TypedDict):
    problem: str
    test_cases: List[str]
    final_suite: str

def generate_base_node(state: AtomicSwarmState, model: str):
    llm = get_model(model, temperature=0.7)
    prompt = (
        "Write exactly ONE basic pytest function (e.g., test_basic) testing the most typical positive case for the function below.\n"
        "RULES: Output ONLY Python test code. DO NOT redefine the function.\n\n"
        f"Function:\n{state['problem']}"
    )
    res = llm.invoke(prompt)
    return {"test_cases": state.get("test_cases", []) + [extract_code(res.content)]}

def generate_edge_node(state: AtomicSwarmState, model: str):
    llm = get_model(model, temperature=0.7)
    time.sleep(2) # Respetta RPM limit
    prompt = (
        "Write exactly ONE pytest function (e.g., test_edge) testing an extreme edge case (e.g., empty input, zeroes, negative limits) for the function below.\n"
        "RULES: Output ONLY Python test code. DO NOT redefine the function.\n\n"
        f"Function:\n{state['problem']}"
    )
    res = llm.invoke(prompt)
    return {"test_cases": state.get("test_cases", []) + [extract_code(res.content)]}

def generate_type_node(state: AtomicSwarmState, model: str):
    llm = get_model(model, temperature=0.7)
    time.sleep(2) # Respetta RPM limit
    prompt = (
        "Write exactly ONE pytest function testing either invalid boundaries, wrong types if applicable, or another unusual case for the function below.\n"
        "RULES: Output ONLY Python test code. DO NOT redefine the function.\n\n"
        f"Function:\n{state['problem']}"
    )
    res = llm.invoke(prompt)
    return {"test_cases": state.get("test_cases", []) + [extract_code(res.content)]}

def deterministic_merge_node(state: AtomicSwarmState):
    """
    Pythonic Merge - Bypass the heavy LLM moderator (saves Tokens and 429 Errors).
    """
    imports = "import pytest\nimport math\n\n"
    # Unisce i test ignorando eventuali stringhe vuote
    body = "\n\n".join([tc for tc in state["test_cases"] if tc.strip()])
    return {"final_suite": imports + body}

def setup_atomic_swarm_graph(model: str = None):
    cfg = DEFAULT_MODELS.get("atomic_swarm", {})
    model = model or cfg.get("model", "llama3-8b")
    
    workflow = StateGraph(AtomicSwarmState)

    workflow.add_node("base", lambda s: generate_base_node(s, model))
    workflow.add_node("edge", lambda s: generate_edge_node(s, model))
    workflow.add_node("type", lambda s: generate_type_node(s, model))
    workflow.add_node("merge", deterministic_merge_node)

    workflow.set_entry_point("base")
    workflow.add_edge("base", "edge")
    workflow.add_edge("edge", "type")
    workflow.add_edge("type", "merge")
    workflow.add_edge("merge", END)

    return workflow.compile()
