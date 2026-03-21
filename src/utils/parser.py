import re

def extract_code(text: str) -> str:
    """
    Robustly extract Python code from LLM output.
    Supports:
    1. Triple backticks with language: ```python ... ```
    2. Triple backticks without language: ``` ... ```
    3. Raw code if no backticks are present (fallback)
    
    It also removes common conversational prefixes/suffixes.
    """
    # Use NON-GREEDY match for the first block
    match = re.search(r"```(?:python)?\n?(.*?)```", text, re.DOTALL | re.IGNORECASE)
    if match:
        code = match.group(1).strip()
    else:
        code = text.strip()
        
    # Remove common conversational lines if they were accidentally captured or were the only thing
    # (e.g. "Here is the code:", "```python")
    lines = code.splitlines()
    cleaned_lines = []
    for line in lines:
        if line.strip().lower().startswith(("here is", "here's", "improved version", "this script")):
            continue
        cleaned_lines.append(line)
        
    return "\n".join(cleaned_lines).strip()

def clean_test_code(code: str) -> str:
    """
    Specific cleaning for test suites.
    Removes common LLM-generated imports that cause errors in the sandbox.
    """
    lines = code.splitlines()
    filtered = []
    for line in lines:
        # Remove lines that try to import the function from unknown modules
        if re.search(r"from\s+(your_module|test_module|solution_module|actual_module|source)\s+import", line):
            continue
        if re.search(r"import\s+separate_paren_groups", line) and "from solution" not in line:
             # Wait, this is too specific. Let's be more general.
             pass
             
        # More general approach: if it looks like an import from a placeholder module
        if re.search(r"from\s+[a-z_]+\s+import\s+[a-z_]+", line):
             # Keep it if it's standard lib or known, otherwise maybe remove?
             # Actually, the sandbox prepends 'from solution import *'.
             # Let's just remove any line that looks like 'from <something_else> import <function_under_test>'
             pass
             
    return code # For now just return code, extract_code is more important
