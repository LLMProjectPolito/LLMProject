import importlib.util
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def calculate_mutation_score(source_code: str, test_code: str) -> float:
    """
    Prefer mutmut for mutation testing and fall back to a lightweight
    regex-based mutator if mutmut is unavailable or fails.
    """
    mutmut_score = _calculate_mutation_score_mutmut(source_code, test_code)
    if mutmut_score is not None:
        return mutmut_score
    return _calculate_mutation_score_regex(source_code, test_code)


def _calculate_mutation_score_mutmut(source_code: str, test_code: str) -> float | None:
    if importlib.util.find_spec("mutmut") is None:
        return None

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        source_file = tmp / "mutant.py"
        test_file = tmp / "test_mutant.py"
        config_file = tmp / "setup.cfg"

        source_file.write_text(source_code, encoding="utf-8")
        test_file.write_text(f"from mutant import *\n\n{test_code}", encoding="utf-8")
        config_file.write_text(
            "[mutmut]\n"
            "paths_to_mutate=mutant.py\n"
            f"runner={sys.executable} -m pytest -q test_mutant.py\n",
            encoding="utf-8",
        )

        env = os.environ.copy()
        env["PYTHONPATH"] = tmpdir

        run_cmd = [
            sys.executable,
            "-m",
            "mutmut",
            "run",
            "--paths-to-mutate=mutant.py",
        ]
        run_res = subprocess.run(
            run_cmd,
            capture_output=True,
            text=True,
            cwd=tmpdir,
            env=env,
            timeout=180,
        )

        combined_output = f"{run_res.stdout}\n{run_res.stderr}"
        summary = _parse_mutmut_summary(combined_output)

        try:
            results_res = subprocess.run(
                [sys.executable, "-m", "mutmut", "results"],
                capture_output=True,
                text=True,
                cwd=tmpdir,
                env=env,
                timeout=60,
            )
            results_summary = _parse_mutmut_results(results_res.stdout)
            if results_summary["total"]:
                summary = results_summary
        except subprocess.SubprocessError:
            pass

        if summary["total"] > 0:
            return round(summary["killed"] / summary["total"], 3)

    return None


def _parse_mutmut_summary(output: str) -> dict:
    killed = _search_count(output, ["killed", "survived", "timeout", "suspicious", "skipped"], "killed")
    survived = _search_count(output, ["killed", "survived", "timeout", "suspicious", "skipped"], "survived")
    timeout = _search_count(output, ["killed", "survived", "timeout", "suspicious", "skipped"], "timeout")
    suspicious = _search_count(output, ["killed", "survived", "timeout", "suspicious", "skipped"], "suspicious")
    skipped = _search_count(output, ["killed", "survived", "timeout", "suspicious", "skipped"], "skipped")

    if any([killed, survived, timeout, suspicious, skipped]):
        total = killed + survived + timeout + suspicious + skipped
        return {"killed": killed, "total": total}

    emoji_map = {
        "killed": r"🎉\s*(\d+)",
        "timeout": r"⏰\s*(\d+)",
        "suspicious": r"🤔\s*(\d+)",
        "survived": r"🙁\s*(\d+)",
        "skipped": r"🔇\s*(\d+)",
    }
    counts = {name: _first_int_match(output, pattern) for name, pattern in emoji_map.items()}
    total = sum(counts.values())
    return {"killed": counts["killed"], "total": total}


def _parse_mutmut_results(output: str) -> dict:
    lines = [line.strip().lower() for line in output.splitlines() if line.strip()]
    status_counts = {
        "killed": sum("killed" in line for line in lines),
        "survived": sum("survived" in line for line in lines),
        "timeout": sum("timeout" in line for line in lines),
        "suspicious": sum("suspicious" in line for line in lines),
        "skipped": sum("skipped" in line for line in lines),
    }
    total = sum(status_counts.values())
    return {"killed": status_counts["killed"], "total": total}


def _search_count(output: str, labels: list[str], target: str) -> int:
    if target not in labels:
        return 0
    pattern = rf"{target}\D+(\d+)|(\d+)\D+{target}"
    match = re.search(pattern, output, re.IGNORECASE)
    if not match:
        return 0
    return int(next(group for group in match.groups() if group))


def _first_int_match(output: str, pattern: str) -> int:
    match = re.search(pattern, output)
    return int(match.group(1)) if match else 0


def _calculate_mutation_score_regex(source_code: str, test_code: str) -> float:
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
        if re.search(pattern, source_code):
            mutated = re.sub(pattern, replacement, source_code, count=1)
            mutants.append(mutated)

    if not mutants:
        return 1.0

    killed = 0
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        test_file = tmp / "test_mutant.py"
        test_file.write_text(f"from mutant import *\n\n{test_code}", encoding="utf-8")

        for mutated_code in mutants:
            source_file = tmp / "mutant.py"
            source_file.write_text(mutated_code, encoding="utf-8")

            res = subprocess.run(
                [sys.executable, "-m", "pytest", str(test_file), "-q"],
                capture_output=True,
                text=True,
                cwd=tmpdir,
            )
            if res.returncode != 0:
                killed += 1

    return round(killed / len(mutants), 3)
