import time
from typing import TypedDict
from langgraph.graph import StateGraph, END

from src.utils.model_registry import get_model
from src.utils.parser import extract_code
from src.utils.executor import run_tests
from src.config import DEFAULT_MODELS

class SelfHealingState(TypedDict):
    problem: str
    test_code: str
    error_message: str
    iteration: int

def generate_node(state: SelfHealingState, model: str):
    llm = get_model(model, temperature=0.7)
    prompt = (
        "Write a pytest suite for the function below.\n"
        "RULES:\n"
        "1. Output ONLY python code in a block. No conversation.\n"
        "2. DO NOT RE-DEFINE the function under test.\n\n"
        f"Function:\n{state['problem']}"
    )
    if state.get("iteration", 0) > 0: 
        time.sleep(2) # Respetta i rate limit

    res = llm.invoke(prompt)
    return {
        "test_code": extract_code(res.content), 
        "iteration": state.get("iteration", 0) + 1
    }

def execute_node(state: SelfHealingState):
    # Esegue il test code per verificare se ci sono errori di sintassi o logica
    metrics = run_tests(state["problem"], state["test_code"])
    
    # Se il test non passa oppure non copre tutto, estraiamo l'errore
    if metrics["errors"] > 0 or metrics["failed"] > 0:
        err = metrics.get("raw_output", "Syntax Error or Test Failure")
        # limitiamo la lunghezza dell'errore per non sprecare token
        err = err[-1500:] 
        return {"error_message": err}
    else:
        return {"error_message": ""} # Nessun errore, test perfetti

def fix_node(state: SelfHealingState, model: str):
    llm = get_model(model, temperature=0.2)
    prompt = (
        "The following pytest suite failed when executed. Fix the errors.\n"
        "RULES:\n"
        "1. Output ONLY the fixed Python code in a block.\n"
        "2. DO NOT RE-DEFINE the function under test.\n\n"
        f"Function:\n{state['problem']}\n\n"
        f"Current Broken Test Code:\n{state['test_code']}\n\n"
        f"Execution Error Output:\n{state['error_message']}\n\n"
        "Fixed Test Code:"
    )
    time.sleep(2) # Respetta i rate limit
    res = llm.invoke(prompt)
    return {
        "test_code": extract_code(res.content),
        "iteration": state.get("iteration", 0) + 1,
        "error_message": ""
    }

def setup_self_healing_graph(model: str = None, max_iterations: int = 3):
    cfg = DEFAULT_MODELS.get("self_healing", {})
    model = model or cfg.get("model", "llama3-8b")
    
    workflow = StateGraph(SelfHealingState)

    workflow.add_node("generate", lambda s: generate_node(s, model))
    workflow.add_node("execute", execute_node)
    workflow.add_node("fix", lambda s: fix_node(s, model))

    workflow.set_entry_point("generate")
    workflow.add_edge("generate", "execute")

    def router(state: SelfHealingState):
        if not state.get("error_message"):
            return END  # Test passati!
        if state.get("iteration", 0) >= max_iterations:
            return END  # Limite tentativi raggiunto
        return "fix"

    workflow.add_conditional_edges("execute", router)
    workflow.add_edge("fix", "execute")

    return workflow.compile()
