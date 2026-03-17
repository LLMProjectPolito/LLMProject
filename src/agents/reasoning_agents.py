import time
from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from src.utils.model_registry import get_model
from src.utils.parser import extract_code
from src.utils.prompts import get_few_shot_prompt, COT_PROMPT, SCOT_PROMPT

class ReasoningState(TypedDict):
    problem: str
    test_code: str
    thought_process: str
    proposals: List[str]

# ── 1. FEW-SHOT AGENT ────────────────────────────────────────────────────────
def few_shot_node(state: ReasoningState, model: str):
    llm = get_model(model)
    prompt = get_few_shot_prompt(state["problem"])
    res = llm.invoke(prompt)
    return {"test_code": extract_code(res.content)}

# ── 2. CHAIN OF THOUGHT (CoT) AGENT ──────────────────────────────────────────
def cot_node(state: ReasoningState, model: str):
    llm = get_model(model)
    prompt = COT_PROMPT.format(problem=state["problem"])
    res = llm.invoke(prompt)
    return {"test_code": extract_code(res.content), "thought_process": res.content}

# ── 3. STRUCTURED CoT (SCoT) AGENT ───────────────────────────────────────────
def scot_node(state: ReasoningState, model: str):
    llm = get_model(model)
    prompt = SCOT_PROMPT.format(problem=state["problem"])
    res = llm.invoke(prompt)
    return {"test_code": extract_code(res.content)}

# ── 4. SELF-CONSISTENCY AGENT ────────────────────────────────────────────────
def self_consistency_node(state: ReasoningState, model: str):
    llm = get_model(model, temperature=0.7)
    proposals = []
    for _ in range(3):
        res = llm.invoke(COT_PROMPT.format(problem=state["problem"]))
        proposals.append(extract_code(res.content))
        time.sleep(2)
    
    merge_prompt = (
        "Consolidate these 3 test suites into one clean file. Deduplicate tests.\n"
        "RULES: Output ONLY code. DO NOT redefine the function.\n"
        f"1:\n{proposals[0]}\n2:\n{proposals[1]}\n3:\n{proposals[2]}"
    )
    final_res = llm.invoke(merge_prompt)
    return {"test_code": extract_code(final_res.content)}

# ── 5. TREE OF THOUGHTS (ToT - Simplified) ──────────────────────────────────
def tot_node(state: ReasoningState, model: str):
    llm = get_model(model)
    ideas = llm.invoke(
        f"Brainstorm 3 diverse testing strategies for this function:\n{state['problem']}\n"
        "Focus on boundary conditions and edge cases."
    )
    best = llm.invoke(
        f"Based on these ideas:\n{ideas.content}\n\n"
        "Write the final pytest suite.\n"
        "RULES: Output ONLY code in a block. NEVER redefine the function. No placeholders."
    )
    return {"test_code": extract_code(best.content)}

# ── Graph Setup Functions ───────────────────────────────────────────────────

def setup_reasoning_graph(technique: str, model: str):
    workflow = StateGraph(ReasoningState)
    
    nodes = {
        "few_shot": lambda s: few_shot_node(s, model),
        "cot":      lambda s: cot_node(s, model),
        "scot":     lambda s: scot_node(s, model),
        "consistency": lambda s: self_consistency_node(s, model),
        "tot":      lambda s: tot_node(s, model)
    }
    
    workflow.add_node("process", nodes[technique])
    workflow.set_entry_point("process")
    workflow.add_edge("process", END)
    
    return workflow.compile()
