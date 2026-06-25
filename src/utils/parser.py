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

