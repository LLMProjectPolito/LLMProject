import time
from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from src.utils.model_registry import get_model
from src.utils.parser import extract_code
from src.config import DEFAULT_MODELS

class HybridState(TypedDict):
    problem: str
    population: List[str]
    best_test: str

def generate_initial_node(state: HybridState, model: str, reasoning_style: str = "zero_shot"):
    llm = get_model(model, temperature=0.8)
    pop = []
    base_instr = "Write a unique and comprehensive pytest suite for the function below."
    from src.utils.prompts import apply_reasoning_style
    
    for i in range(2):
        prompt = apply_reasoning_style(state['problem'], f"{base_instr} Variation {i+1}/2.", reasoning_style)
        if i > 0: time.sleep(2) # Respect 6 RPM
        res = llm.invoke(prompt)
        pop.append(extract_code(res.content))
    return {"population": pop}

def evolve_node(state: HybridState, model: str, reasoning_style: str = "zero_shot"):
    llm = get_model(model, temperature=0.4)
    from src.utils.prompts import apply_reasoning_style
    
    base_instr = (
        "Merge these two pytest suites into one single, superior suite.\n"
        f"Suite 1:\n{state['population'][0]}\n\n"
        f"Suite 2:\n{state['population'][1]}"
    )
    # For evolution, we pass the merged context as the 'problem' to apply_reasoning_style
    prompt = apply_reasoning_style("", base_instr, reasoning_style)
    
    res = llm.invoke(prompt)
    return {"best_test": extract_code(res.content)}

def setup_hybrid_graph(generate_model: str = None, evolve_model: str = None, reasoning_style: str = "zero_shot"):
    cfg = DEFAULT_MODELS["hybrid"]
    generate_model = generate_model or cfg["generate_model"]
    evolve_model   = evolve_model   or cfg["evolve_model"]
    workflow = StateGraph(HybridState)
    
    workflow.add_node("generate", lambda s: generate_initial_node(s, generate_model, reasoning_style))
    workflow.add_node("evolve",   lambda s: evolve_node(s, evolve_model, reasoning_style))
    workflow.set_entry_point("generate")
    workflow.add_edge("generate", "evolve")
    workflow.add_edge("evolve", END)
    return workflow.compile()
