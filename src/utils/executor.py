import re
import subprocess
import sys
import tempfile
from pathlib import Path
from radon.complexity import cc_visit
from radon.metrics import mi_visit
from difflib import SequenceMatcher
from src.utils.coverage_parser import parse_coverage
from src.utils.diversity import analyze_test_diversity
from src.utils.mutation_check import calculate_mutation_score

def run_tests(source_code: str, test_code: str) -> dict:
    """
    Run pytest and perform static analysis (Radon).
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        src_file  = tmp / "solution.py"
        test_file = tmp / "test_solution.py"
        cov_json_file = tmp / "coverage.json"

        src_file.write_text(source_code, encoding="utf-8")
        
        # Guard against conversational output if it slipped through prompts
        clean_code = _ensure_only_code(test_code)
        
        test_code_final = f"from solution import *\n\n{clean_code}"
        test_file.write_text(test_code_final, encoding="utf-8")

        try:
            result = subprocess.run(
                [
                    sys.executable, "-m", "pytest", str(test_file), "--tb=no", "-q", "--color=no",
                    f"--cov={tmp}", "--cov-branch", "--cov-report=term-missing",
                    f"--cov-report=json:{cov_json_file}"
                ],
                capture_output=True, text=True, cwd=tmpdir,
                timeout=60
            )
        except subprocess.TimeoutExpired as e:
            # Return partial metrics or error if it timed out
            return {
                "passed": 0, "failed": 0, "errors": 1, "total": 0,
                "functional_correctness": 0, "line_coverage": 0, "branch_coverage": 0,
                "mutation_score": 0, "complexity_cc": 0, "maintainability_mi": 0,
                "bloat_ratio": 0, "similarity_score": 0,
                "unique_inputs_count": 0, "edge_case_count": 0, "test_type_count": 0,
                "duplication_ratio": 1.0, "diversity_score": 0,
                "raw_output": "TIMEOUT: Pytest took > 60s"
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
        line_cov, branch_cov = parse_coverage(cov_json_file, raw)

    passed, failed, errors = _parse_summary(raw)
    total = passed + failed + errors
    diversity = analyze_test_diversity(clean_code)
    
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
        "unique_inputs_count": diversity["unique_inputs_count"],
        "edge_case_count": diversity["edge_case_count"],
        "test_type_count": diversity["test_type_count"],
        "duplication_ratio": diversity["duplication_ratio"],
        "diversity_score": diversity["diversity_score"],
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
