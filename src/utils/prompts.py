"""
Centralized prompt templates and few-shot examples for the EvalPlus experiment.
Refined for 1B-120B model consistency.
"""

FEW_SHOT_EXAMPLES = [
    {
        "problem": (
            "def is_palindrome(s: str) -> bool:\n"
            "    \"\"\" Checks if a string is a palindrome \"\"\""
        ),
        "test_code": (
            "def test_palindrome_basic():\n"
            "    assert is_palindrome('radar') == True\n"
            "    assert is_palindrome('hello') == False\n\n"
            "def test_palindrome_empty():\n"
            "    assert is_palindrome('') == True"
        )
    },
    {
        "problem": (
            "def get_max(arr: list[int]) -> int:\n"
            "    \"\"\" Returns the maximum element in a list, or None if empty \"\"\""
        ),
        "test_code": (
            "def test_max_positive():\n"
            "    assert get_max([1, 2, 3]) == 3\n\n"
            "def test_max_empty():\n"
            "    assert get_max([]) == None"
        )
    }
]

def get_few_shot_prompt(problem: str, base_instruction: str = None) -> str:
    instr = base_instruction or "You are an expert QA engineer. Follow these examples to write your pytest suite:"
    prompt = f"{instr}\n\n"
    for ex in FEW_SHOT_EXAMPLES:
        prompt += f"### Problem:\n{ex['problem']}\n\n### Tests (Pytest):\n```python\n{ex['test_code']}\n```\n\n---\n\n"
    prompt += f"### Problem:\n{problem}\n\n### Tests (Pytest):\n"
    return prompt

def apply_reasoning_style(problem: str, base_instruction: str, style: str = "zero_shot") -> str:
    """
    Modular reasoning injector.
    Universal bridge between Runner, Agents, and Prompts.
    """
    style = style.lower() if style else "zero_shot"
    
    if style == "few_shot":
        return get_few_shot_prompt(problem, base_instruction)
    
    if style == "cot":
        return (
            f"{base_instruction}\n"
            "PLANNING: Think step-by-step about the edge cases, types, and logic of the problem below.\n"
            "OUTPUT RULES:\n"
            "1. Output ONLY the code block at the end.\n"
            "2. DO NOT REDEFINE the function under test.\n"
            "3. Use a single Python code block for all tests.\n\n"
            f"Problem:\n{problem}\n\n### Thought & Solution:"
        )
    
    if style == "scot":
        return (
            f"{base_instruction}\n"
            "Follow the Structured Chain of Thought (SCoT) framework:\n"
            "STEP 1: REASONING - Analyze functional goals and constraints.\n"
            "STEP 2: PLAN - List test functions names and scenarios.\n"
            "STEP 3: CODE - Write the high-quality pytest suite.\n\n"
            "CRITICAL: The Python code MUST be in its own ```python ... ``` block.\n"
            "DO NOT REDEFINE the function below.\n\n"
            f"Problem:\n{problem}\n\n### SCoT Steps:"
        )
    
    # Default: Optimized Zero-Shot
    return (
        f"{base_instruction}\n\n"
        f"Problem:\n{problem}\n\n"
        "### Tests (Pytest):\n"
        "Output ONLY the code block."
    )

# Static templates for quick referencing
COT_PROMPT = apply_reasoning_style("{problem}", "Expert Test Engineer.", "cot")
SCOT_PROMPT = apply_reasoning_style("{problem}", "Expert Test Engineer.", "scot")
