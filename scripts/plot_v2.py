import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


MODEL_ORDER = ["gemma-4b", "gemma-27b", "gemma-12b", "gemma-1b"]
PROMPT_ORDER = ["zero_shot", "cot", "scot", "few_shot"]
PROMPT_LABELS = ["Zero-shot", "CoT", "SCoT", "Few-shot"]


def plot_v2(csv_path, out_dir):
    df = pd.read_csv(csv_path)
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    _plot_model_dashboard(df, out_path / "radar_chart_combined.png")
    _plot_metric_heatmap(
        df,
        value_column=_resolve_column(df, ["total_tokens", "total_tokens_mean"]),
        title="Total Tokens by Model / Agent / Prompt",
        output_path=out_path / "extra_metrics.png",
        cmap="magma",
        value_format="{:.0f}",
    )
    _plot_metric_heatmap(
        df,
        value_column=_resolve_column(df, ["functional_correctness", "functional_correctness_mean"]),
        title="Functional Correctness by Model / Agent / Prompt",
        output_path=out_path / "radar_charts_individual.png",
        cmap="viridis",
        value_format="{:.2f}",
    )

    print(f"Plots saved to {out_path}")


def _plot_model_dashboard(df, output_path):
    metrics = [
        (["passed_mean", "passed"], "Passed mean"),
        (["functional_correctness_mean", "functional_correctness"], "Functional correctness"),
        (["line_coverage_mean", "line_coverage"], "Line coverage"),
        (["mutation_score_mean", "mutation_score"], "Mutation score"),
        (["fc_per_1k_tokens", "functional_correctness_per_1k_tokens"], "FC / 1k tokens"),
        (["coverage_per_1k_tokens", "line_coverage_per_1k_tokens"], "Coverage / 1k tokens"),
    ]

    fig, axes = plt.subplots(2, 3, figsize=(20, 12))
    fig.suptitle("Model Comparison Dashboard", fontsize=20, fontweight="bold", y=0.97)

    for ax, (columns, title) in zip(axes.flat, metrics):
        value_column = _resolve_column(df, columns)
        summary = df.groupby("model", dropna=False)[value_column].mean().sort_values(ascending=False)
        labels = summary.index.tolist()
        values = summary.to_numpy()

        colors = plt.cm.Blues(np.linspace(0.45, 0.85, len(labels))) if len(labels) else []
        bars = ax.barh(labels, values, color=colors, edgecolor="none")
        ax.invert_yaxis()
        ax.set_title(title, fontsize=14)
        ax.grid(axis="x", alpha=0.2)
        ax.set_axisbelow(True)

        if len(values):
            pad = max(float(np.nanmax(values)) * 0.02, 0.02)
            for bar, value in zip(bars, values):
                ax.text(
                    value + pad,
                    bar.get_y() + bar.get_height() / 2,
                    f"{value:.2f}",
                    va="center",
                    ha="left",
                    fontsize=9,
                )

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def _plot_metric_heatmap(df, value_column, title, output_path, cmap, value_format):
    models = _ordered_models(df)
    fig, axes = plt.subplots(2, 2, figsize=(20, 14))
    axes = axes.flatten()

    series = pd.to_numeric(df[value_column], errors="coerce")
    vmax = float(series.max()) if series.notna().any() else 1.0
    if not np.isfinite(vmax) or vmax <= 0:
        vmax = 1.0

    images = []
    for ax, model in zip(axes, models):
        subset = df[df["model"] == model].copy()
        pivot = subset.pivot_table(
            index="agent",
            columns="prompt",
            values=value_column,
            aggfunc="mean",
        )
        pivot = pivot.reindex(columns=PROMPT_ORDER)
        pivot.columns = PROMPT_LABELS
        pivot = pivot.fillna(0)
        pivot = pivot.loc[pivot.mean(axis=1).sort_values(ascending=False).index]

        data = pivot.to_numpy()
        image = ax.imshow(data, aspect="auto", cmap=cmap, vmin=0.0, vmax=vmax)
        images.append(image)

        ax.set_title(model, fontsize=16, fontweight="bold")
        ax.set_xlabel("Prompt")
        ax.set_ylabel("Agent")
        ax.set_xticks(np.arange(len(PROMPT_LABELS)))
        ax.set_xticklabels(PROMPT_LABELS)
        ax.set_yticks(np.arange(len(pivot.index)))
        ax.set_yticklabels(pivot.index.tolist())

        for row_index in range(data.shape[0]):
            for col_index in range(data.shape[1]):
                value = data[row_index, col_index]
                text_color = "white" if value / vmax >= 0.55 else "black"
                ax.text(
                    col_index,
                    row_index,
                    value_format.format(value),
                    ha="center",
                    va="center",
                    fontsize=8,
                    color=text_color,
                )

    for ax in axes[len(models):]:
        ax.set_visible(False)

    fig.suptitle(title, fontsize=20, fontweight="bold", y=0.97)
    fig.colorbar(images[0], ax=axes.tolist(), fraction=0.025, pad=0.02)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def _ordered_models(df):
    models = [str(value) for value in df["model"].dropna().unique()]
    preferred = [model for model in MODEL_ORDER if model in models]
    extras = sorted(model for model in models if model not in MODEL_ORDER)
    return preferred + extras


def _resolve_column(df, candidates):
    for column_name in candidates:
        if column_name in df.columns:
            return column_name
    raise ValueError(f"None of these columns exist in the CSV: {', '.join(candidates)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    plot_v2(args.csv, args.out)
