from langchain_core.prompts import PromptTemplate
from langgraph.graph import StateGraph, END
from typing import TypedDict
from src.utils.model_registry import get_model
from src.utils.parser import extract_code
from src.utils.prompts import apply_reasoning_style
from src.config import DEFAULT_MODELS

class BaselineState(TypedDict):
    problem: str
    test_code: str

def generation_node(state: BaselineState, model: str, reasoning_style: str = "zero_shot"):
    llm = get_model(model)
    base_instr = (
        "You are an expert QA engineer. Write a comprehensive pytest suite.\n"
        "RULES: Output code in a block. Do NOT redefine the function. Do NOT use fake imports."
    )
    prompt = apply_reasoning_style(state["problem"], base_instr, reasoning_style)
    res = llm.invoke(prompt)
    return {"test_code": extract_code(res.content)}

def setup_baseline_graph(model: str = None, reasoning_style: str = "zero_shot"):
    cfg = DEFAULT_MODELS["baseline"]
    model = model or cfg["model"]
    workflow = StateGraph(BaselineState)
    workflow.add_node("generate", lambda s: generation_node(s, model, reasoning_style))
    workflow.set_entry_point("generate")
    workflow.add_edge("generate", END)
    return workflow.compile()
