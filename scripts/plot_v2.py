#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


PROMPT_ORDER = ["zero_shot", "cot", "scot", "few_shot"]
PROMPT_LABELS = ["Zero-shot", "CoT", "SCoT", "Few-shot"]

MODEL_BAR_METRICS = [
    ("passed_mean", "Passed mean"),
    ("functional_correctness_mean", "Functional correctness"),
    ("line_coverage_mean", "Line coverage"),
    ("mutation_score_mean", "Mutation score"),
    ("fc_per_1k_tokens", "FC / 1k tokens"),
    ("coverage_per_1k_tokens", "Coverage / 1k tokens"),
]

HEATMAP_COLORS = {
    "functional_correctness_mean": "viridis",
    "total_tokens_mean": "magma",
}


def plot_v2(csv_path: str | Path, out_dir: str | Path) -> None:
    df = pd.read_csv(csv_path)
    df = prepare_dataframe(df)

    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    plot_model_dashboard(df, out_path / "radar_chart_combined.png")
    plot_model_heatmaps(
        df,
        metric="functional_correctness_mean",
        title="Functional Correctness by Model / Agent / Prompt",
        out_file=out_path / "radar_charts_individual.png",
        value_format="{:.2f}",
        transform=None,
    )
    plot_model_heatmaps(
        df,
        metric="total_tokens_mean",
        title="Total Tokens by Model / Agent / Prompt",
        out_file=out_path / "extra_metrics.png",
        value_format="{:.0f}",
        transform=np.log10,
    )

    print(f"Plots saved to {out_path}")


def prepare_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    if "model" not in out.columns:
        if "config_label" in out.columns:
            out["model"] = out["config_label"].astype(str).str.split(":").str[0]
        else:
            out["model"] = "unknown"

    if "prompt" not in out.columns:
        if "config_label" in out.columns:
            out["prompt"] = out["config_label"].astype(str).str.split(":").str[-1]
        else:
            out["prompt"] = "zero_shot"

    numeric_columns = [
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
    ]

    for column in numeric_columns:
        if column in out.columns:
            out[column] = pd.to_numeric(out[column], errors="coerce")

    out["prompt"] = pd.Categorical(out["prompt"], categories=PROMPT_ORDER, ordered=True)
    return out


def plot_model_dashboard(df: pd.DataFrame, out_file: Path) -> None:
    model_summary = (
        df.groupby("model")[
            [metric for metric, _ in MODEL_BAR_METRICS]
        ]
        .mean()
        .sort_values("functional_correctness_mean", ascending=False)
    )

    models = list(model_summary.index)
    if not models:
        return

    fig, axes = plt.subplots(2, 3, figsize=(18, 10), constrained_layout=True)
    axes = axes.flatten()

    palette = plt.cm.Blues(np.linspace(0.45, 0.9, len(models)))

    for idx, (metric, label) in enumerate(MODEL_BAR_METRICS):
        ax = axes[idx]
        values = model_summary[metric].sort_values(ascending=True)
        colors = [palette[models.index(model)] for model in values.index]
        bars = ax.barh(values.index, values.values, color=colors, edgecolor="none")
        ax.set_title(label)
        ax.grid(axis="x", alpha=0.2)
        ax.set_axisbelow(True)
        ax.bar_label(bars, fmt="%.2f", padding=3, fontsize=8)
        if metric == "line_coverage_mean":
            ax.set_xlim(0, max(100, float(values.max()) * 1.08))

    for idx in range(len(MODEL_BAR_METRICS), len(axes)):
        fig.delaxes(axes[idx])

    fig.suptitle("Model Comparison Dashboard", fontsize=18, fontweight="bold")
    fig.savefig(out_file, dpi=220, bbox_inches="tight")
    plt.close(fig)


def plot_model_heatmaps(
    df: pd.DataFrame,
    metric: str,
    title: str,
    out_file: Path,
    value_format: str,
    transform,
) -> None:
    models = list(
        df.groupby("model")["functional_correctness_mean"]
        .mean()
        .sort_values(ascending=False)
        .index
    )
    if not models:
        return

    ncols = 2
    nrows = math.ceil(len(models) / ncols)
    fig, axes = plt.subplots(
        nrows,
        ncols,
        figsize=(ncols * 8, nrows * 6),
        constrained_layout=True,
    )
    axes = np.array(axes).reshape(-1)

    matrices: list[pd.DataFrame] = []
    for model in models:
        model_df = df[df["model"] == model].copy()
        if model_df.empty:
            continue

        agent_order = (
            model_df.groupby("agent")[metric]
            .mean()
            .sort_values(ascending=False)
            .index.tolist()
        )

        matrix = (
            model_df.pivot_table(index="agent", columns="prompt", values=metric, aggfunc="mean")
            .reindex(index=agent_order, columns=PROMPT_ORDER)
        )
        matrices.append(matrix)

    if not matrices:
        return

    transformed_matrices = [apply_transform(matrix.to_numpy(dtype=float), transform) for matrix in matrices]
    finite_values = np.concatenate([matrix[np.isfinite(matrix)] for matrix in transformed_matrices if np.isfinite(matrix).any()])
    if finite_values.size == 0:
        vmin, vmax = 0.0, 1.0
    else:
        vmin, vmax = float(np.nanmin(finite_values)), float(np.nanmax(finite_values))
        if vmin == vmax:
            vmax = vmin + 1.0

    cmap = HEATMAP_COLORS.get(metric, "viridis")
    last_image = None

    for idx, model in enumerate(models):
        ax = axes[idx]
        model_df = df[df["model"] == model].copy()
        if model_df.empty:
            ax.axis("off")
            continue

        agent_order = (
            model_df.groupby("agent")[metric]
            .mean()
            .sort_values(ascending=False)
            .index.tolist()
        )
        matrix = (
            model_df.pivot_table(index="agent", columns="prompt", values=metric, aggfunc="mean")
            .reindex(index=agent_order, columns=PROMPT_ORDER)
        )

        display_matrix = apply_transform(matrix.to_numpy(dtype=float), transform)
        masked = np.ma.masked_invalid(display_matrix)
        last_image = ax.imshow(masked, aspect="auto", cmap=cmap, vmin=vmin, vmax=vmax)

        ax.set_title(model, fontsize=13, fontweight="bold")
        ax.set_xticks(range(len(PROMPT_ORDER)), PROMPT_LABELS, rotation=0)
        ax.set_yticks(range(len(agent_order)), agent_order)
        ax.tick_params(axis="y", labelsize=9)
        ax.tick_params(axis="x", labelsize=9)
        ax.set_xlabel("Prompt")
        ax.set_ylabel("Agent")

        for row_idx, agent in enumerate(agent_order):
            for col_idx, prompt in enumerate(PROMPT_ORDER):
                value = matrix.loc[agent, prompt] if prompt in matrix.columns else np.nan
                if pd.notna(value):
                    ax.text(
                        col_idx,
                        row_idx,
                        value_format.format(float(value)),
                        ha="center",
                        va="center",
                        fontsize=7,
                        color="white" if is_dark_cell(display_matrix[row_idx, col_idx], vmin, vmax) else "black",
                    )

    for idx in range(len(models), len(axes)):
        fig.delaxes(axes[idx])

    if last_image is not None:
        fig.colorbar(last_image, ax=fig.axes, shrink=0.85, pad=0.01)

    fig.suptitle(title, fontsize=18, fontweight="bold")
    fig.savefig(out_file, dpi=220, bbox_inches="tight")
    plt.close(fig)


def apply_transform(values: np.ndarray, transform) -> np.ndarray:
    if transform is None:
        return values

    with np.errstate(divide="ignore", invalid="ignore"):
        return transform(values)


def is_dark_cell(value: float, vmin: float, vmax: float) -> bool:
    if not np.isfinite(value):
        return False
    midpoint = (vmin + vmax) / 2.0
    return value > midpoint


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    plot_v2(args.csv, args.out)