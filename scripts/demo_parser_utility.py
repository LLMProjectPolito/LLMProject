import os
import re
from dotenv import load_dotenv
load_dotenv()

from src.utils.model_registry import get_model
from src.utils.parser import extract_code

# We bypass the standard executor to show the raw failure
def mock_run_pytest_raw(code: str):
    print("\n" + "="*50)
    print("EXECUTING RAW OUTPUT (NO PARSER):")
    try:
        # Simulate what python would do if we try to execute the whole LLM response
        compile(code, "<string>", "exec")
        print("RESULT: Correct Syntax (Unexpected for chatty LLM)")
    except Exception as e:
        print(f"RESULT: FAILED with {type(e).__name__}: {e}")

def mock_run_pytest_robust(code: str):
    print("\n" + "="*50)
    print("EXECUTING ROBUST OUTPUT (WITH PARSER):")
    clean = extract_code(code)
    try:
        compile(clean, "<string>", "exec")
        print("RESULT: SUCCESS (Syntax is valid)")
        print(f"EXTRACT_CODE Length: {len(clean)} chars vs RAW: {len(code)} chars")
    except Exception as e:
        print(f"RESULT: FAILED with {type(e).__name__}: {e}")

def demo():
    llm = get_model("llama3-70b")
    # Ask it something that usually triggers conversational fluff
    prompt = (
        "Write a python pytest file for HumanEval/0. "
        "Talk a lot before and after the code block to explain your reasoning."
    )
    print("Querying LLM...")
    res = llm.invoke(prompt).content
    
    print("\n--- LLM RAW OUTPUT PREVIEW ---")
    print(res[:200] + "...")
    print("...")
    print(res[-200:])
    
    mock_run_pytest_raw(res)
    mock_run_pytest_robust(res)

if __name__ == "__main__":
    demo()
