import time
from langgraph.graph import StateGraph, END
from typing import TypedDict, List
from src.utils.model_registry import get_model
from src.utils.parser import extract_code
from src.config import DEFAULT_MODELS

class ConsensusState(TypedDict):
    problem: str
    proposals: List[str]
    final_test: str

def generation_node(state: ConsensusState, model: str, reasoning_style: str = "zero_shot"):
    llm = get_model(model, temperature=0.7)
    from src.utils.prompts import apply_reasoning_style
    props = []
    base_instr = "Write a robust and complete pytest suite for the function below. Output ONLY code. DO NOT re-define the function."
    
    for i in range(3):
        prompt = apply_reasoning_style(state['problem'], f"{base_instr} Variation {i+1}/3.", reasoning_style)
        if i > 0: time.sleep(2)
        res = llm.invoke(prompt)
        props.append(extract_code(res.content))
    return {"proposals": props}

def debate_node(state: ConsensusState, model: str):
    time.sleep(2)
    llm = get_model(model, temperature=0.2)
    proposals_text = "\n---\n".join(state["proposals"])
    prompt = (
        "You are the Moderator. Analyze these 3 proposal variations.\n"
        "RULES:\n"
        "1. Eliminate hallucinations. Merge correct tests into one final suite.\n"
        "2. Output ONLY THE FINAL MERGED CODE in a block.\n"
        "3. DO NOT RE-DEFINE the function under test.\n\n"
        f"Proposals:\n{proposals_text}"
    )
    res = llm.invoke(prompt)
    return {"final_test": extract_code(res.content)}

def setup_consensus_graph(generation_model: str = None, debate_model: str = None, reasoning_style: str = "zero_shot"):
    cfg = DEFAULT_MODELS["consensus"]
    generation_model = generation_model or cfg["generation_model"]
    debate_model     = debate_model     or cfg["debate_model"]
    workflow = StateGraph(ConsensusState)
    workflow.add_node("generate", lambda s: generation_node(s, generation_model, reasoning_style))
    workflow.add_node("debate",   lambda s: debate_node(s, debate_model))
    workflow.set_entry_point("generate")
    workflow.add_edge("generate", "debate")
    workflow.add_edge("debate", END)
    return workflow.compile()
