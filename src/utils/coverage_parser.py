import json
import re
from pathlib import Path


def parse_coverage(cov_json_file: Path, output: str) -> tuple[float | None, float | None]:
    line_cov = None
    branch_cov = None

    if cov_json_file.exists():
        try:
            coverage_data = json.loads(cov_json_file.read_text(encoding="utf-8"))
            line_cov, branch_cov = _parse_json_coverage(coverage_data)
        except (OSError, ValueError, TypeError, json.JSONDecodeError):
            line_cov = branch_cov = None

    if line_cov is not None and branch_cov is not None:
        return line_cov, branch_cov

    fallback_line_cov, fallback_branch_cov = _parse_text_coverage(output)
    return (
        line_cov if line_cov is not None else fallback_line_cov,
        branch_cov if branch_cov is not None else fallback_branch_cov,
    )


def _parse_json_coverage(coverage_data: dict) -> tuple[float | None, float | None]:
    line_cov = _coverage_from_summary(coverage_data.get("totals", {}), kind="line")
    branch_cov = _coverage_from_summary(coverage_data.get("totals", {}), kind="branch")

    if line_cov is not None and branch_cov is not None:
        return line_cov, branch_cov

    files = coverage_data.get("files", {})
    if isinstance(files, dict):
        totals = _aggregate_file_summaries(files.values())
        if line_cov is None:
            line_cov = totals["line"]
        if branch_cov is None:
            branch_cov = totals["branch"]

    return line_cov, branch_cov


def _aggregate_file_summaries(file_summaries: list[dict]) -> dict[str, float | None]:
    covered_lines = total_lines = 0
    covered_branches = total_branches = 0

    for summary in file_summaries:
        if not isinstance(summary, dict):
            continue

        summary = summary.get("summary", summary)
        if not isinstance(summary, dict):
            continue

        n_lines = summary.get("num_statements", summary.get("num_lines", 0)) or 0
        c_lines = summary.get("covered_lines", summary.get("covered_statements", 0)) or 0
        n_branches = summary.get("num_branches", 0) or 0
        c_branches = summary.get("covered_branches", 0) or 0

        total_lines += n_lines
        covered_lines += c_lines
        total_branches += n_branches
        covered_branches += c_branches

    line_cov = round((covered_lines / total_lines) * 100, 2) if total_lines else None
    branch_cov = round((covered_branches / total_branches) * 100, 2) if total_branches else None
    return {"line": line_cov, "branch": branch_cov}


def _coverage_from_summary(summary: dict, kind: str) -> float | None:
    if not isinstance(summary, dict):
        return None

    if kind == "line":
        value = summary.get("percent_covered")
        if value is not None:
            return round(float(value), 2)
        return None

    num_branches = summary.get("num_branches")
    covered_branches = summary.get("covered_branches")
    if num_branches is not None and covered_branches is not None:
        num_branches = float(num_branches)
        covered_branches = float(covered_branches)
        if num_branches > 0:
            return round((covered_branches / num_branches) * 100, 2)

    value = summary.get("percent_covered_display")
    if isinstance(value, str):
        value = value.rstrip("%")
    if value is not None:
        try:
            return round(float(value), 2)
        except ValueError:
            return None

    return None


def _parse_text_coverage(output: str) -> tuple[float | None, float | None]:
    lines = output.splitlines()
    total_line = next((l for l in reversed(lines) if l.startswith("TOTAL")), None)
    if not total_line:
        return None, None

    percentages = re.findall(r"(\d+)%", total_line)
    if len(percentages) == 1:
        return float(percentages[0]), None
    if len(percentages) >= 2:
        return float(percentages[-2]), float(percentages[-1])
    return None, None
