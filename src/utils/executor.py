import re
import subprocess
import tempfile
from pathlib import Path
from radon.complexity import cc_visit
from radon.metrics import mi_visit
from difflib import SequenceMatcher
from src.utils.mutation_check import calculate_mutation_score

def run_tests(source_code: str, test_code: str) -> dict:
    """
    Run pytest and perform static analysis (Radon).
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        src_file  = tmp / "solution.py"
        test_file = tmp / "test_solution.py"

        src_file.write_text(source_code, encoding="utf-8")
        
        # Guard against conversational output if it slipped through prompts
        clean_code = _ensure_only_code(test_code)
        
        test_code_final = f"from solution import *\n\n{clean_code}"
        test_file.write_text(test_code_final, encoding="utf-8")

        try:
            result = subprocess.run(
                ["python", "-m", "pytest", str(test_file), "--tb=no", "-q", "--color=no", 
                 f"--cov={tmp}", "--cov-branch", "--cov-report=term-missing"],
                capture_output=True, text=True, cwd=tmpdir,
                timeout=60
            )
        except subprocess.TimeoutExpired as e:
            # Return partial metrics or error if it timed out
            return {
                "passed": 0, "failed": 0, "errors": 1, "total": 0,
                "functional_correctness": 0, "line_coverage": 0, "branch_coverage": 0,
                "mutation_score": 0, "complexity_cc": 0, "maintainability_mi": 0,
                "bloat_ratio": 0, "similarity_score": 0, "raw_output": "TIMEOUT: Pytest took > 60s"
            }

        try:
            cc_blocks = cc_visit(clean_code)
            avg_cc = sum(b.complexity for b in cc_blocks) / len(cc_blocks) if cc_blocks else 0
            mi_score = mi_visit(clean_code, multi=True)
            
            # Bloat Ratio: Test Lines / Source Lines
            test_loc = len([l for l in clean_code.splitlines() if l.strip()])
            src_loc = len([l for l in source_code.splitlines() if l.strip()])
            bloat_ratio = round(test_loc / src_loc, 2) if src_loc > 0 else 0
        except:
            avg_cc, mi_score, bloat_ratio = 0, 0, 0

    raw = result.stdout + result.stderr
    passed, failed, errors = _parse_summary(raw)
    total = passed + failed + errors
    
    line_cov, branch_cov = _parse_coverage(raw)
    
    return {
        "passed": passed,
        "failed": failed,
        "errors": errors,
        "total":  total,
        "functional_correctness": round(passed/total, 3) if total > 0 else 0,
        "line_coverage": line_cov,
        "branch_coverage": branch_cov,
        "mutation_score": calculate_mutation_score(source_code, clean_code),
        "complexity_cc": round(avg_cc, 2),
        "maintainability_mi": round(mi_score, 2),
        "bloat_ratio": bloat_ratio,
        "similarity_score": round(SequenceMatcher(None, source_code, clean_code).ratio(), 3),
        "raw_output": raw[:500] + "..." if len(raw) > 500 else raw
    }

def _ensure_only_code(text: str) -> str:
    # Quick regex to pick the largest block between ``` if present
    blocks = re.findall(r"```(?:python)?\n?(.*?)```", text, re.DOTALL)
    if blocks:
        return max(blocks, key=len).strip()
    return text.strip()

def _parse_summary(output: str) -> tuple[int, int, int]:
    passed = failed = errors = 0
    m = re.search(r"(\d+) passed", output); passed = int(m.group(1)) if m else 0
    m = re.search(r"(\d+) failed", output); failed = int(m.group(1)) if m else 0
    m = re.search(r"(\d+) error", output); errors = int(m.group(1)) if m else 0
    return passed, failed, errors

def _parse_coverage(output: str) -> tuple[float | None, float | None]:
    # Look for the last row starting with TOTAL
    lines = output.splitlines()
    total_line = next((l for l in reversed(lines) if l.startswith("TOTAL")), None)
    if not total_line:
        return None, None
    
    # Extract all percentages
    percentages = re.findall(r"(\d+)%", total_line)
    if len(percentages) >= 2:
        return float(percentages[-2]), float(percentages[-1])
    elif len(percentages) == 1:
        return float(percentages[0]), None
    return None, None
