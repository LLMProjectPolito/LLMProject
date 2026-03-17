"""
Centralized prompt templates and few-shot examples for the EvalPlus experiment.
"""

FEW_SHOT_EXAMPLES = [
    {
        "problem": "def is_palindrome(s: str) -> bool:\n    return s == s[::-1]",
        "test_code": (
            "def test_palindrome_basic():\n"
            "    assert is_palindrome('radar') is True\n"
            "    assert is_palindrome('hello') is False\n\n"
            "def test_palindrome_empty():\n"
            "    assert is_palindrome('') is True\n\n"
            "def test_palindrome_case_sensitive():\n"
            "    assert is_palindrome('Radar') is False"
        )
    },
    {
        "problem": "def get_max(arr: list[int]) -> int:\n    if not arr: return None\n    return max(arr)",
        "test_code": (
            "def test_max_positive():\n"
            "    assert get_max([1, 2, 3]) == 3\n\n"
            "def test_max_negative():\n"
            "    assert get_max([-1, -5, -2]) == -1\n\n"
            "def test_max_empty():\n"
            "    assert get_max([]) is None"
        )
    }
]

def get_few_shot_prompt(problem: str, base_instruction: str = None) -> str:
    instr = base_instruction or "You are an expert QA engineer. Follow these examples to write your pytest suite:"
    prompt = f"{instr}\n\n"
    for ex in FEW_SHOT_EXAMPLES:
        prompt += f"Problem:\n{ex['problem']}\n\nTests:\n{ex['test_code']}\n\n---\n\n"
    prompt += f"Problem:\n{problem}\n\nTests:"
    return prompt

def apply_reasoning_style(problem: str, base_instruction: str, style: str = "zero_shot") -> str:
    """
    Modular reasoning injector. 
    Can be used by ANY node in ANY agent graph.
    """
    style = style.lower()
    if style == "few_shot":
        return get_few_shot_prompt(problem, base_instruction)
    
    if style == "cot":
        return (
            f"{base_instruction}\n"
            "Think step-by-step before writing the code.\n"
            "CORE RULES:\n"
            "1. Output ONLY the test code block at the end.\n"
            "2. DO NOT RE-DEFINE THE FUNCTION BELOW. Assume it is already imported.\n"
            "3. Focus on edge cases and boundary conditions.\n\n"
            f"Problem:\n{problem}\n\nSolution:"
        )
    
    if style == "scot":
        return (
            f"{base_instruction}\n"
            "Follow a Structured Chain of Thought (SCoT):\n"
            "CORE RULES:\n"
            "1. STEP 1: REASONING - Analyze goals (no code here).\n"
            "2. STEP 2: PLAN - List test functions (no code here).\n"
            "3. STEP 3: CODE - Write the pytest suite (ONLY this step contains code).\n"
            "4. NEVER REDEFINE THE FUNCTION UNDER TEST.\n\n"
            f"Problem:\n{problem}"
        )
    
    # default zero_shot
    return f"{base_instruction}\n\nProblem:\n{problem}\n\nTests:"

# Standard templates for simple usage
COT_PROMPT = apply_reasoning_style("{problem}", "You are an expert QA engineer.", "cot")
SCOT_PROMPT = apply_reasoning_style("{problem}", "You are an expert QA engineer.", "scot")
