import os
import tempfile
import subprocess
from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_core.prompts import PromptTemplate
from src.utils.model_registry import get_model
from src.utils.parser import extract_code
from src.utils.prompts import apply_reasoning_style
from src.config import DEFAULT_MODELS

class AdversarialState(TypedDict):
    source_code: str
    mutated_code: str
    test_code: str
    mutation_caught: bool

def hacker_node(state: AdversarialState, model: str):
    llm = get_model(model, temperature=0.7)
    prompt = PromptTemplate.from_template(
        "You are a 'Red Team' hacker. Introduce a subtle logical bug into this function.\n"
        "RULES:\n"
        "1. Do NOT change the function signature.\n"
        "2. Output ONLY the mutated code inside a code block.\n"
        "3. Focus on edge cases or boundary conditions.\n\n"
        "Original Code:\n{source_code}\n\nMutated Code:"
    )
    res = llm.invoke(prompt.format(source_code=state["source_code"]))
    return {"mutated_code": extract_code(res.content)}

def tester_node(state: AdversarialState, model: str, reasoning_style: str = "zero_shot"):
    llm = get_model(model, temperature=0.2)
    base_instr = "You are a 'Blue Team' QA engineer. Write a robust pytest suite to detect bugs in the provided function."
    prompt = apply_reasoning_style(state["source_code"], base_instr, reasoning_style)
    res = llm.invoke(prompt)
    return {"test_code": extract_code(res.content)}

def execution_node(state: AdversarialState):
    """
    Check if the tests fail on the mutated code (indicating the bug was caught).
    """
    from src.utils.executor import run_tests
    # Here source_code is actually the MUTATED code for the verification step
    metrics = run_tests(state["mutated_code"], state["test_code"])
    # If any test fails or errors on the mutated code, the mutation was caught.
    caught = (metrics["failed"] > 0 or metrics["errors"] > 0)
    return {"mutation_caught": caught}

def setup_adversarial_graph(hacker_model: str = None, tester_model: str = None, reasoning_style: str = "zero_shot"):
    cfg = DEFAULT_MODELS["adversarial"]
    hacker_model = hacker_model or cfg["hacker_model"]
    tester_model = tester_model or cfg["tester_model"]
    workflow = StateGraph(AdversarialState)
    workflow.add_node("hacker",   lambda s: hacker_node(s, hacker_model))
    workflow.add_node("tester",   lambda s: tester_node(s, tester_model, reasoning_style))
    workflow.add_node("executor", execution_node)

    workflow.set_entry_point("hacker")
    workflow.add_edge("hacker",   "tester")
    workflow.add_edge("tester",   "executor")
    workflow.add_edge("executor", END)
    return workflow.compile()
