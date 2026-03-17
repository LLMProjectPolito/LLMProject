"""
Radar chart visualization of experiment results.

Usage:
  python scripts/plot_results.py                          # reads results/latest_results.csv
  python scripts/plot_results.py --csv results/run_XYZ/results.csv --out results/run_XYZ
"""
import argparse
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

METRICS = ["functional_correctness", "line_coverage", "complexity_score", "maintainability_mi", "similarity_score", "speed_score"]
LABELS  = ["Functional\nCorrectness", "Line\nCoverage", "Code\nSimplicity", "Maintainability\n(MI)", "Semantic\nSimilarity", "Speed"]

AGENT_COLORS = {
    "baseline":     "#4C72B0",
    "actor_critic": "#DD8452",
    "adversarial":  "#55A868",
    "competitive":  "#C44E52",
    "hybrid":       "#8172B3",
    "coa":          "#937860",
    "soa":          "#DA8BC3",
    "swarm":        "#8C8C8C",
    "consensus":    "#CCB974",
}


def normalize(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize all metric columns to [0, 1]."""
    out = df.copy()

    # line_coverage: 0-100 → 0-1
    if "line_coverage" in out.columns:
        out["line_coverage"] = out["line_coverage"].fillna(0) / 100.0

    # complexity_cc: normalize so 1.0 is simplest, 0.0 is complex
    if "complexity_cc" in out.columns:
        out["complexity_score"] = 1.0 / out["complexity_cc"].clip(lower=1.0)
    else:
        out["complexity_score"] = 0

    # maintainability_mi: 0-100 → 0-1
    if "maintainability_mi" in out.columns:
        out["maintainability_mi"] = out["maintainability_mi"].fillna(0) / 100.0

    # speed_score: inverse of elapsed_s
    if "elapsed_s" in out.columns:
        max_t = out["elapsed_s"].max()
        out["speed_score"] = 1.0 - (out["elapsed_s"] / max_t) if max_t > 0 else 1.0

    return out


def radar_chart(ax, values: list[float], color: str, label: str, alpha=0.25):
    n = len(LABELS)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    angles += angles[:1]
    values = list(values) + [values[0]]

    ax.plot(angles, values, color=color, linewidth=2, label=label)
    ax.fill(angles, values, color=color, alpha=alpha)


def plot_all_agents(df: pd.DataFrame):
    df = normalize(df)
    agents = df["agent"].unique()

    n_cols = 3
    n_rows = int(np.ceil(len(agents) / n_cols))

    fig, axes = plt.subplots(
        n_rows, n_cols,
        figsize=(5 * n_cols, 5 * n_rows),
        subplot_kw=dict(polar=True),
    )
    axes = axes.flatten()

    for idx, agent in enumerate(sorted(agents)):
        ax    = axes[idx]
        color = AGENT_COLORS.get(agent, "#333333")
        adf   = df[df["agent"] == agent]
        vals  = [adf[m].mean() for m in METRICS]
        _setup_radar_axes(ax)
        radar_chart(ax, vals, color=color, label=agent)
        ax.set_title(agent.replace("_", " ").title(), pad=14, fontsize=13, fontweight="bold")

    # hide unused axes
    for j in range(idx + 1, len(axes)):
        axes[j].set_visible(False)

    fig.suptitle("Multi-Agent Test Generation — Performance per Agent",
                 fontsize=16, fontweight="bold", y=1.01)
    plt.tight_layout()
    out = OUT_DIR / "radar_chart.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    print(f"Saved {out}")
    plt.close()


def plot_combined(df: pd.DataFrame):
    """All agents overlaid on a single radar chart."""
    df = normalize(df)

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    _setup_radar_axes(ax)

    patches = []
    for agent in sorted(df["agent"].unique()):
        color = AGENT_COLORS.get(agent, "#333333")
        adf   = df[df["agent"] == agent]
        vals  = [adf[m].mean() for m in METRICS]
        radar_chart(ax, vals, color=color, label=agent, alpha=0.12)
        patches.append(mpatches.Patch(color=color, label=agent.replace("_", " ").title()))

    ax.legend(handles=patches, loc="upper right",
              bbox_to_anchor=(1.35, 1.15), fontsize=10)
    ax.set_title("All Agents — Overlay Radar", fontsize=15,
                 fontweight="bold", pad=20)

    out = OUT_DIR / "radar_combined.png"
    plt.savefig(out, dpi=150, bbox_inches="tight")
    print(f"Saved {out}")
    plt.close()


def _setup_radar_axes(ax):
    n = len(LABELS)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    angles += angles[:1]
    ax.set_thetagrids(np.degrees(angles[:-1]), LABELS, fontsize=10)
    ax.set_ylim(0, 1)
    ax.set_yticks([0.25, 0.5, 0.75, 1.0])
    ax.set_yticklabels(["0.25", "0.50", "0.75", "1.00"], fontsize=7, color="grey")
    ax.grid(color="grey", linestyle="--", linewidth=0.5, alpha=0.7)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", type=Path, default=Path("results/latest_results.csv"),
                        help="Path to results CSV")
    parser.add_argument("--out", type=Path, default=Path("results"),
                        help="Output directory for generated charts")
    args = parser.parse_args()

    if not args.csv.exists():
        print(f"No results found at {args.csv}.")
        print("Run experiment_runner.py first.")
        return

    df = pd.read_csv(args.csv)
    print(f"Loaded {len(df)} rows from {args.csv}")

    args.out.mkdir(exist_ok=True, parents=True)

    # pass the out dir to the plot functions via module-level vars
    global OUT_DIR
    OUT_DIR = args.out

    plot_all_agents(df)
    plot_combined(df)
    print("Done.")


if __name__ == "__main__":
    main()
