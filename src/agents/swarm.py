import time
from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from src.utils.model_registry import get_model
from src.utils.parser import extract_code
from src.utils.prompts import apply_reasoning_style
from src.config import DEFAULT_MODELS

class SwarmState(TypedDict):
    problem: str
    results: List[str]
    final_suite: str

def worker_agent(state: SwarmState, model: str, reasoning_style: str = "zero_shot"):
    llm = get_model(model, temperature=0.9)
    base_instr = (
        "Generate exactly ONE unique and interesting pytest test case.\n"
        "RULES: Focus on an edge case. Output ONLY the test code. Do NOT redefine the function."
    )
    prompt = apply_reasoning_style(state["problem"], base_instr, reasoning_style)
    
    if state.get("results"): time.sleep(2) # Respect 6 RPM limit
    res = llm.invoke(prompt)
    return {"results": state.get("results", []) + [extract_code(res.content)]}

def aggregator_node(state: SwarmState, model: str):
    llm = get_model(model, temperature=0.2)
    body = "\n\n".join(state["results"])
    prompt = (
        "You are a Quality Engineer. Combine the following tests into a clean, deduplicated pytest file.\n"
        "RULES:\n"
        "1. Output ONLY valid code. Ensure necessary imports (pytest, math) are at the top.\n"
        "2. DO NOT RE-DEFINE the function under test.\n"
        "3. DO NOT use placeholder imports. Assume function is in scope.\n\n"
        f"Individual Tests:\n{body}\n\nFinal Suite:"
    )
    res = llm.invoke(prompt)
    return {"final_suite": extract_code(res.content)}

def setup_swarm_graph(n: int = None, worker_model: str = None, aggregator_model: str = None, reasoning_style: str = "zero_shot"):
    cfg = DEFAULT_MODELS["swarm"]
    n                = n                or cfg["n"]
    worker_model     = worker_model     or cfg["worker_model"]
    aggregator_model = aggregator_model or cfg["aggregator_model"]
    workflow = StateGraph(SwarmState)
    workflow.add_node("worker",     lambda s: worker_agent(s, worker_model, reasoning_style))
    workflow.add_node("aggregator", lambda s: aggregator_node(s, aggregator_model))
    workflow.set_entry_point("worker")

    def loop_until_n(state: SwarmState):
        return "worker" if len(state.get("results", [])) < n else "aggregator"

    workflow.add_conditional_edges("worker", loop_until_n)
    workflow.add_edge("aggregator", END)
    return workflow.compile()
