#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path

import pandas as pd


PROMPT_ORDER = {
    "zero_shot": 0,
    "cot": 1,
    "scot": 2,
    "few_shot": 3,
}

MEAN_COLS = [
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
    "execution_time",
]

SUM_COLS = [
    "passed",
    "functional_correctness",
    "line_coverage",
    "mutation_score",
    "prompt_tokens",
    "completion_tokens",
    "total_tokens",
]

EXTRA_MEAN_COLS = [
    "unique_inputs_count",
    "edge_case_count",
    "test_type_count",
    "duplication_ratio",
    "diversity_score",
]

EXTRA_TAIL_COLS = [
    "prompt_tokens",
    "completion_tokens",
    "total_tokens",
    "execution_time",
    "norm_config",
]


def main() -> None:
    parser = argparse.ArgumentParser(description="Build gemma_176_aggregate.csv from detailed results.csv files.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Repository root.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output CSV path. Default: reports/gen2/gemma_176_aggregate.csv",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Directory where gemma_176_aggregate.csv will be written. Default: reports/gen2",
    )
    parser.add_argument(
        "--results-roots",
        nargs="*",
        type=Path,
        default=None,
        help="Optional explicit roots to scan. If omitted, uses results_recomputed_* then results/.",
    )
    args = parser.parse_args()

    repo_root = args.repo_root
    output_dir = args.output_dir or (repo_root / "reports" / "gen")
    output_path = args.output or (output_dir / "gemma_176_aggregate.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    result_files = discover_result_files(repo_root, args.results_roots)
    if not result_files:
        raise SystemExit("No gemma results.csv files found.")

    rows: list[dict[str, object]] = []
    for model, csv_path in result_files:
        rows.extend(build_rows_for_model(model, csv_path))

    out_df = pd.DataFrame(rows)
    out_df = out_df.sort_values(
        by=["model", "agent", "prompt"],
        key=lambda col: col.map(prompt_sort_key) if col.name == "prompt" else col,
    ).reset_index(drop=True)

    if "total_tokens_mean" in out_df.columns and not out_df["total_tokens_mean"].empty:
        max_total_tokens = float(out_df["total_tokens_mean"].max())
    else:
        max_total_tokens = 1.0

    out_df["quality_rank"] = out_df.apply(
        lambda row: compute_quality_rank(row, max_total_tokens),
        axis=1,
    )

    column_order = [
        "model",
        "agent",
        "prompt",
        "config_label",
        "problems",
        "passed_mean",
        "failed_mean",
        "errors_mean",
        "total_mean",
        "functional_correctness_mean",
        "line_coverage_mean",
        "branch_coverage_mean",
        "mutation_score_mean",
        "complexity_cc_mean",
        "maintainability_mi_mean",
        "bloat_ratio_mean",
        "similarity_score_mean",
        "unique_inputs_count_mean",
        "edge_case_count_mean",
        "test_type_count_mean",
        "duplication_ratio_mean",
        "diversity_score_mean",
        "prompt_tokens_mean",
        "completion_tokens_mean",
        "total_tokens_mean",
        "execution_time_mean",
        "passed_sum",
        "functional_correctness_sum",
        "line_coverage_sum",
        "mutation_score_sum",
        "prompt_tokens_sum",
        "completion_tokens_sum",
        "total_tokens_sum",
        "fc_per_1k_tokens",
        "passed_per_1k_tokens",
        "coverage_per_1k_tokens",
        "mutation_per_1k_tokens",
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
        "elapsed_s",
        "quality_rank",
    ]

    for col in column_order:
        if col not in out_df.columns:
            out_df[col] = pd.NA

    out_df = out_df[column_order]
    out_df.to_csv(output_path, index=False)
    print(f"Wrote {len(out_df)} aggregated rows to {output_path}")


def discover_result_files(repo_root: Path, explicit_roots: list[Path] | None) -> list[tuple[str, Path]]:
    roots: list[Path] = []
    if explicit_roots:
        roots.extend(explicit_roots)
    else:
        recomputed_roots = sorted(
            [p for p in repo_root.glob("results_recomputed_*") if p.is_dir()],
            reverse=True,
        )
        roots.extend(recomputed_roots)
        results_root = repo_root / "results"
        if results_root.is_dir():
            roots.append(results_root)

    seen_models: set[str] = set()
    discovered: list[tuple[str, Path]] = []

    for root in roots:
        for csv_path in sorted(root.glob("gemma-*/results.csv")):
            model = csv_path.parent.name
            if model in seen_models:
                continue
            seen_models.add(model)
            discovered.append((model, csv_path))

    return discovered


def build_rows_for_model(model: str, csv_path: Path) -> list[dict[str, object]]:
    df = load_results_dataframe(csv_path)

    if "agent" not in df.columns:
        raise ValueError(f"{csv_path} is missing the 'agent' column")

    df = df.copy()
    df["model"] = model
    df["prompt"] = df.apply(infer_prompt, axis=1)
    df["config_label"] = df["model"].astype(str) + ":" + df["prompt"].astype(str)

    numeric_candidates = [c for c in MEAN_COLS if c in df.columns]
    for col in numeric_candidates:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    grouped = df.groupby(["model", "agent", "prompt", "config_label"], dropna=False, sort=False)

    rows: list[dict[str, object]] = []
    for (group_model, agent, prompt, config_label), group in grouped:
        row: dict[str, object] = {
            "model": group_model,
            "agent": agent,
            "prompt": prompt,
            "config_label": config_label,
            "problems": int(group["task_id"].nunique()) if "task_id" in group.columns else int(len(group)),
        }

        for col in MEAN_COLS:
            if col in group.columns:
                row[f"{col}_mean"] = round(float(group[col].mean(skipna=True)), 10)
            else:
                row[f"{col}_mean"] = pd.NA

        for col in SUM_COLS:
            if col in group.columns:
                row[f"{col}_sum"] = round(float(group[col].sum(skipna=True)), 10)
            else:
                row[f"{col}_sum"] = pd.NA

        total_tokens_sum = row.get("total_tokens_sum")
        if total_tokens_sum and float(total_tokens_sum) > 0:
            row["fc_per_1k_tokens"] = round(float(row.get("functional_correctness_sum", 0.0)) / float(total_tokens_sum) * 1000.0, 10)
            row["passed_per_1k_tokens"] = round(float(row.get("passed_sum", 0.0)) / float(total_tokens_sum) * 1000.0, 10)
            row["coverage_per_1k_tokens"] = round(float(row.get("line_coverage_sum", 0.0)) / float(total_tokens_sum) * 1000.0, 10)
            row["mutation_per_1k_tokens"] = round(float(row.get("mutation_score_sum", 0.0)) / float(total_tokens_sum) * 1000.0, 10)
        else:
            row["fc_per_1k_tokens"] = pd.NA
            row["passed_per_1k_tokens"] = pd.NA
            row["coverage_per_1k_tokens"] = pd.NA
            row["mutation_per_1k_tokens"] = pd.NA

        row["passed"] = row["passed_mean"]
        row["failed"] = row["failed_mean"]
        row["errors"] = row["errors_mean"]
        row["total"] = row["total_mean"]
        row["functional_correctness"] = row["functional_correctness_mean"]
        row["line_coverage"] = row["line_coverage_mean"]
        row["branch_coverage"] = row["branch_coverage_mean"]
        row["mutation_score"] = row["mutation_score_mean"]
        row["complexity_cc"] = row["complexity_cc_mean"]
        row["maintainability_mi"] = row["maintainability_mi_mean"]
        row["bloat_ratio"] = row["bloat_ratio_mean"]
        row["similarity_score"] = row["similarity_score_mean"]
        row["unique_inputs_count"] = row["unique_inputs_count_mean"]
        row["edge_case_count"] = row["edge_case_count_mean"]
        row["test_type_count"] = row["test_type_count_mean"]
        row["duplication_ratio"] = row["duplication_ratio_mean"]
        row["diversity_score"] = row["diversity_score_mean"]
        row["prompt_tokens"] = row["prompt_tokens_mean"]
        row["completion_tokens"] = row["completion_tokens_mean"]
        row["total_tokens"] = row["total_tokens_mean"]
        row["elapsed_s"] = row["execution_time_mean"]

        rows.append(row)

    return rows


def load_results_dataframe(csv_path: Path) -> pd.DataFrame:
    with csv_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        try:
            header = next(reader)
        except StopIteration:
            return pd.DataFrame()

        header_extra_count = _header_extra_count(header)
        rows: list[dict[str, str]] = []

        for raw_row in reader:
            if not raw_row:
                continue
            rows.append(_map_row_to_header(header, raw_row, header_extra_count))

    return pd.DataFrame(rows)


def _header_extra_count(header: list[str]) -> int:
    extra_count = 0
    for column_name in EXTRA_MEAN_COLS:
        index = 18 + extra_count
        if index < len(header) and header[index] == column_name:
            extra_count += 1
        else:
            break
    return extra_count


def _map_row_to_header(header: list[str], row: list[str], header_extra_count: int) -> dict[str, str]:
    if len(row) <= len(header):
        padded = row + [""] * (len(header) - len(row))
        return dict(zip(header, padded))

    extra_needed = len(row) - len(header)
    extra_names = list(EXTRA_MEAN_COLS[header_extra_count:]) + list(EXTRA_TAIL_COLS)
    extra_names = extra_names[:extra_needed]

    if len(extra_names) < extra_needed:
        extra_names.extend(f"extra_{i}" for i in range(1, extra_needed - len(extra_names) + 1))

    columns = list(header) + extra_names
    return dict(zip(columns, row))


def infer_prompt(row: pd.Series) -> str:
    if "prompt" in row and pd.notna(row["prompt"]):
        prompt = str(row["prompt"]).strip()
        if prompt and prompt in PROMPT_ORDER:
            return prompt
        if ":" in prompt:
            return prompt.rsplit(":", 1)[-1].strip()

    if "config_label" in row and pd.notna(row["config_label"]):
        config_label = str(row["config_label"]).strip()
        if ":" in config_label:
            return config_label.rsplit(":", 1)[-1].strip()
        return config_label

    return "zero_shot"


def prompt_sort_key(value: object) -> int:
    text = str(value)
    return PROMPT_ORDER.get(text, 99)


def compute_quality_rank(row: pd.Series, max_total_tokens: float) -> float:
    correctness = float(row.get("functional_correctness_mean", 0.0) or 0.0)
    coverage = float(row.get("line_coverage_mean", 0.0) or 0.0) / 100.0
    mutation = float(row.get("mutation_score_mean", 0.0) or 0.0)
    diversity = float(row.get("diversity_score_mean", 0.0) or 0.0)
    total_tokens = float(row.get("total_tokens_mean", 0.0) or 0.0)

    token_efficiency = 0.0
    if max_total_tokens > 0:
        token_efficiency = max(0.0, 1.0 - (total_tokens / max_total_tokens))

    score = (
        0.40 * correctness
        + 0.25 * coverage
        + 0.15 * mutation
        + 0.10 * diversity
        + 0.10 * token_efficiency
    )
    return round(score * 100.0, 6)


if __name__ == "__main__":
    main()