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

def generation_node(state: ConsensusState, model: str):
    llm = get_model(model, temperature=0.7)
    props = []
    for i in range(3):
        prompt = (
            f"Generate a robust pytest suite (v{i+1}) for the function below.\n"
            "RULES:\n"
            "1. Output ONLY code in a block.\n"
            "2. DO NOT RE-DEFINE the function under test.\n"
            "3. DO NOT use placeholder imports.\n\n"
            f"Function:\n{state['problem']}"
        )
        if i > 0: time.sleep(2) # Respect 6 RPM limit
        res = llm.invoke(prompt)
        props.append(extract_code(res.content))
    return {"proposals": props}

def debate_node(state: ConsensusState, model: str):
    time.sleep(2) # Respect 6 RPM limit before moderator speaks
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

def setup_consensus_graph(generation_model: str = None, debate_model: str = None):
    cfg = DEFAULT_MODELS["consensus"]
    generation_model = generation_model or cfg["generation_model"]
    debate_model     = debate_model     or cfg["debate_model"]
    workflow = StateGraph(ConsensusState)
    workflow.add_node("generate", lambda s: generation_node(s, generation_model))
    workflow.add_node("debate",   lambda s: debate_node(s, debate_model))
    workflow.set_entry_point("generate")
    workflow.add_edge("generate", "debate")
    workflow.add_edge("debate", END)
    return workflow.compile()
