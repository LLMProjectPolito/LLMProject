#!/usr/bin/env python3

from __future__ import annotations

import argparse
import concurrent.futures
import csv
import re
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

RESULTS_ROOT_DEFAULT = PROJECT_ROOT / "results"
DATA_ROOT_DEFAULT = PROJECT_ROOT / "data" / "evalplus_subset"
BACKUP_SUFFIX_DEFAULT = ".bak"

METRIC_COLUMNS = [
    "passed",
    "failed",
    "errors",
    "total",
    "functional_correctness",
    "line_coverage",
    "branch_coverage",
    "mutation_score",
    "complexity_cc",
    "maintainability_mi",
    "bloat_ratio",
    "similarity_score",
    "unique_inputs_count",
    "edge_case_count",
    "test_type_count",
    "duplication_ratio",
    "diversity_score",
    "prompt_tokens",
    "completion_tokens",
    "total_tokens",
]


@dataclass(frozen=True)
class RowJob:
    index: int
    row: dict[str, str]
    test_file: Path | None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-root", type=Path, default=RESULTS_ROOT_DEFAULT)
    parser.add_argument("--data-root", type=Path, default=DATA_ROOT_DEFAULT)
    parser.add_argument("--folders", nargs="*", default=None)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--include-backup", action="store_true")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--backup-suffix", type=str, default=BACKUP_SUFFIX_DEFAULT)
    args = parser.parse_args()

    problem_map = _load_problem_map(args.data_root)
    result_dirs = list(_discover_result_dirs(args.results_root, args.folders, args.include_backup))

    if not result_dirs:
        print("No results.csv files found.")
        return

    total_rows = 0
    total_updated = 0
    total_missing = 0

    for csv_path, tests_dir in result_dirs:
        print(f"\n[{csv_path.parent.relative_to(args.results_root)}]")
        all_rows = _read_rows(csv_path)
        if not all_rows:
            print("  empty CSV, skipping")
            continue

        rows = all_rows[: args.limit] if args.limit is not None else all_rows
        jobs = [RowJob(index=idx, row=row, test_file=_find_test_file(tests_dir, row)) for idx, row in enumerate(rows)]

        total_rows += len(jobs)
        missing = sum(1 for job in jobs if job.test_file is None)
        total_missing += missing
        print(f"  rows: {len(jobs)} | matched test files: {len(jobs) - missing} | missing: {missing}")

        if args.dry_run:
            for job in jobs[:5]:
                status = job.test_file.name if job.test_file else "MISSING"
                print(f"  - {job.row.get('task_id')} | {job.row.get('agent')} | {job.row.get('config_label')} -> {status}")
            continue

        rescored_rows = _rescore_rows(jobs, problem_map, args.workers)
        updated_count = sum(1 for row in rescored_rows if row.get("_rescored") == "1")
        total_updated += updated_count
        merged_rows = list(all_rows)
        for job, rescored_row in zip(jobs, rescored_rows):
            merged_rows[job.index] = rescored_row
        _write_rows(csv_path, merged_rows, args.backup_suffix)
        print(f"  rescored: {updated_count}")

    if args.dry_run:
        print("\nDry run complete.")
    else:
        print("\nDone.")
        print(f"Rows inspected: {total_rows}")
        print(f"Rows rescored:   {total_updated}")
        print(f"Rows missing:    {total_missing}")


def _load_problem_map(data_root: Path) -> dict[str, dict[str, str]]:
    problem_map: dict[str, dict[str, str]] = {}
    for json_path in sorted(data_root.glob("*.json")):
        import json

        prob = json.loads(json_path.read_text(encoding="utf-8"))
        problem_map[prob["task_id"]] = prob
    return problem_map


def _discover_result_dirs(results_root: Path, folders: list[str] | None, include_backup: bool) -> Iterable[tuple[Path, Path]]:
    for csv_path in sorted(results_root.rglob("results.csv")):
        if not include_backup and "legacy_backup" in csv_path.parts:
            continue
        if folders is not None and csv_path.parent.name not in folders:
            continue
        tests_dir = csv_path.parent / "tests"
        if tests_dir.is_dir():
            yield csv_path, tests_dir


def _read_rows(csv_path: Path) -> list[dict[str, str]]:
    with csv_path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def _write_rows(csv_path: Path, rows: list[dict[str, str]], backup_suffix: str) -> None:
    if csv_path.exists():
        backup_path = csv_path.with_suffix(csv_path.suffix + backup_suffix)
        if not backup_path.exists():
            shutil.copy2(csv_path, backup_path)

    fieldnames = [key for key in rows[0].keys() if key != "_rescored"]
    for column in METRIC_COLUMNS:
        if column not in fieldnames:
            fieldnames.append(column)

    with csv_path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})


def _rescore_rows(jobs: list[RowJob], problem_map: dict[str, dict[str, str]], workers: int) -> list[dict[str, str]]:
    if workers <= 1:
        return [_rescore_single(job, problem_map) for job in jobs]

    indexed_results: dict[int, dict[str, str]] = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        future_map = {executor.submit(_rescore_single, job, problem_map): job.index for job in jobs}
        for future in concurrent.futures.as_completed(future_map):
            indexed_results[future_map[future]] = future.result()

    return [indexed_results[job.index] for job in jobs]


def _rescore_single(job: RowJob, problem_map: dict[str, dict[str, str]]) -> dict[str, str]:
    row = dict(job.row)
    if job.test_file is None:
        row["_rescored"] = "0"
        return row

    problem = problem_map.get(row.get("task_id", ""))
    if not problem:
        row["_rescored"] = "0"
        return row

    run_tests = _load_run_tests()
    source_code = problem["prompt"] + problem["canonical_solution"]
    test_code = job.test_file.read_text(encoding="utf-8")
    metrics = run_tests(source_code, test_code)

    for key in METRIC_COLUMNS:
        if key in metrics:
            row[key] = metrics[key]

    row["_rescored"] = "1"
    return row


def _find_test_file(tests_dir: Path, row: dict[str, str]) -> Path | None:
    task_id = row.get("task_id", "")
    agent = row.get("agent", "")
    config_label = row.get("config_label", "")
    norm_config = row.get("norm_config", "")

    safe_task = task_id.replace("/", "_")
    if not safe_task:
        return None

    candidates = [p for p in tests_dir.glob(f"{safe_task}__*.py") if p.is_file()]
    if not candidates:
        candidates = [p for p in tests_dir.glob("*.py") if p.is_file() and safe_task in p.stem]
    if not candidates:
        return None

    row_tokens = set(_tokenize(" ".join([agent, config_label, norm_config, task_id])))
    agent_lower = agent.lower().strip()
    task_prefix = f"{safe_task}__".lower()

    scored: list[tuple[int, int, str, Path]] = []
    for candidate in candidates:
        stem = candidate.stem.lower()
        after_prefix = stem[len(task_prefix):] if stem.startswith(task_prefix) else stem
        cand_tokens = set(_tokenize(stem))
        score = len(row_tokens & cand_tokens)
        if agent_lower and after_prefix.startswith(agent_lower):
            score += 10
        if config_label:
            score += len(set(_tokenize(config_label)) & cand_tokens)
        if norm_config:
            score += len(set(_tokenize(norm_config)) & cand_tokens)
        scored.append((-score, len(candidate.name), candidate.name, candidate))

    scored.sort()
    best = scored[0][3]

    if len(scored) > 1 and scored[0][:3] == scored[1][:3]:
        tied = [item[3] for item in scored if item[:3] == scored[0][:3]]
        for candidate in tied:
            if agent_lower and agent_lower in candidate.stem.lower():
                return candidate

    return best


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def _load_run_tests():
    try:
        from src.utils.executor import run_tests
    except ModuleNotFoundError as exc:
        raise SystemExit("Missing runtime dependencies for rescoring. Install requirements first.") from exc
    return run_tests


if __name__ == "__main__":
    main()
