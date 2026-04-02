import time
from langgraph.graph import StateGraph, END
from typing import TypedDict, Dict
from src.utils.model_registry import get_model
from src.utils.parser import extract_code
from src.utils.executor import run_tests
from src.config import DEFAULT_MODELS

class CompetitiveState(TypedDict):
    problem: str
    generated_tests: Dict[str, str]
    winner: str

def make_generation_node(model_key: str):
    def node(state: CompetitiveState):
        llm = get_model(model_key)
        prompt = (
            "Write a comprehensive pytest suite for the function below.\n"
            "RULES:\n"
            "1. Output ONLY python code in a block. No explanations.\n"
            "2. DO NOT RE-DEFINE the function under test.\n"
            "3. DO NOT use placeholder imports. Assume the function is in scope.\n\n"
            f"Function:\n{state['problem']}"
        )
        if state.get("generated_tests"): time.sleep(2) # Respect 6 RPM
        res = llm.invoke(prompt)
        return {"generated_tests": {**state.get("generated_tests", {}), model_key: extract_code(res.content)}}
    return node

def judge_node(state: CompetitiveState):
    """
    Judge the winner by actually running the tests and comparing metrics.
    Priority: Functional Correctness > Line Coverage > Code Cleanliness.
    """
    best_score = -1
    winner = list(state["generated_tests"].keys())[0]
    
    for model, code in state["generated_tests"].items():
        try:
            # We use the prompt as source_code since it usually contains the docstring/signature 
            # and experiment_runner will handle full source later.
            metrics = run_tests(state["problem"], code)
            # Simple scoring: FC * 100 + Coverage
            score = (metrics["functional_correctness"] * 100) + (metrics["line_coverage"] or 0)
            if score > best_score:
                best_score = score
                winner = model
        except:
            continue
            
    return {"winner": winner}

def setup_competitive_graph(models: list = None):
    models = models or DEFAULT_MODELS["competitive"]["models"]
    if len(models) < 1:
        raise ValueError("competitive requires at least one model")
    workflow = StateGraph(CompetitiveState)
    for m in models:
        workflow.add_node(m, make_generation_node(m))
    workflow.add_node("judge", judge_node)

    workflow.set_entry_point(models[0])
    for i in range(len(models) - 1):
        workflow.add_edge(models[i], models[i + 1])
    workflow.add_edge(models[-1], "judge")
    workflow.add_edge("judge", END)
    return workflow.compile()
