import re
import subprocess
import tempfile
from pathlib import Path

def calculate_mutation_score(source_code: str, test_code: str) -> float:
    """
    Very simple mutation testing:
    1. Flip common operators (+ -> -, * -> /, etc.)
    2. Return percentage of mutants caught by the test suite.
    """
    mutations = [
        (r"\+", "-"),
        (r"-", "+"),
        (r"\*", "/"),
        (r"==", "!="),
        (r">", "<"),
        (r"if ", "if not "),
    ]
    
    mutants = []
    for pattern, replacement in mutations:
        # Only mutate if pattern exists
        if re.search(pattern, source_code):
            mutated = re.sub(pattern, replacement, source_code, count=1)
            mutants.append(mutated)
            
    if not mutants:
        return 1.0 # Nothing to mutate, assume passed? Or 0? Let's say 1.0.

    killed = 0
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        test_file = tmp / "test_mutant.py"
        test_file.write_text(f"from mutant import *\n\n{test_code}", encoding="utf-8")
        
        for i, m_code in enumerate(mutants):
            m_file = tmp / "mutant.py"
            m_file.write_text(m_code, encoding="utf-8")
            
            # If tests FAIL on a mutant, it means the test CAUGHT the bug (Killed)
            res = subprocess.run(
                ["python", "-m", "pytest", str(test_file), "-q"],
                capture_output=True, text=True, cwd=tmpdir
            )
            if res.returncode != 0:
                killed += 1
                
    return round(killed / len(mutants), 3)
