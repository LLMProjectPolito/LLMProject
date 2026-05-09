import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns
import numpy as np

# Define all 8 models
models = [
    "gemma-1b", "gemma-4b", "gemma-12b", "gemma-27b", "gemma-31b",
    "gemma-4-2b", "gemma-4-4b", "gemma-4-26b"
]
base_path = "results"

# Mapping: subplot metric name -> CSV column used to compute it
metric_map = {
    "Correctness":    "functional_correctness",
    "Coverage":       "line_coverage",
    "Efficiency (1k)": None,           # derived: correctness / tokens * 1000
    "Maintainability": "maintainability_mi",
}

# ─── Collect per-model, per-metric WORST combo AND baseline-zeroshot ───
# Structure: per_metric_data[metric][model] = {"worst_value", "worst_combo", "bl_value"}
per_metric_data = {m: {} for m in metric_map}

for model in models:
    csv_path = os.path.join(base_path, model, "results.csv")
    if not os.path.exists(csv_path):
        continue

    df = pd.read_csv(csv_path)
    df['style'] = df['config_label'].apply(
        lambda x: str(x).split(':')[-1] if ':' in str(x) else x
    )

    combos = df.groupby(['agent', 'style']).agg({
        'functional_correctness': 'mean',
        'line_coverage': 'mean',
        'total_tokens': 'mean',
        'maintainability_mi': 'mean',
        'bloat_ratio': 'mean'
    }).reset_index()

    # Compute efficiency column
    combos['efficiency'] = combos.apply(
        lambda r: (r['functional_correctness'] / r['total_tokens']) * 1000
        if r['total_tokens'] > 0 else 0, axis=1
    )

    # Baseline zero-shot row
    bl_mask = (combos['agent'] == 'baseline') & (combos['style'] == 'zero_shot')
    bl_row = combos.loc[bl_mask].iloc[0] if bl_mask.any() else None

    for metric_name in metric_map:
        # Determine which column to minimise
        if metric_name == "Correctness":
            col = "functional_correctness"
        elif metric_name == "Coverage":
            col = "line_coverage"
        elif metric_name == "Efficiency (1k)":
            col = "efficiency"
        elif metric_name == "Maintainability":
            col = "maintainability_mi"

        # WORST combo for THIS metric (minimum value)
        worst_idx = combos[col].idxmin()
        worst_row = combos.loc[worst_idx]
        worst_val = worst_row[col]
        worst_combo = f"{worst_row['agent']} + {worst_row['style']}"

        # Baseline zero-shot value for this metric
        bl_val = float('nan')
        if bl_row is not None:
            bl_val = bl_row[col]

        # Percentage change (negative = worse than baseline)
        if pd.notna(bl_val) and bl_val != 0:
            pct = ((worst_val - bl_val) / bl_val) * 100
        else:
            pct = float('nan')

        per_metric_data[metric_name][model] = {
            "worst_value": worst_val,
            "worst_combo": worst_combo,
            "bl_value":    bl_val,
            "pct_change":  pct,
        }

# ─── Build one DataFrame per metric for plotting ───
plot_frames = {}
for metric_name in metric_map:
    rows = []
    for model in models:
        if model in per_metric_data[metric_name]:
            d = per_metric_data[metric_name][model]
            rows.append({
                "Model":       model,
                "Value":       d["worst_value"],
                "Worst Combo": d["worst_combo"],
                "BL Value":    d["bl_value"],
                "pct":         d["pct_change"],
            })
    plot_frames[metric_name] = pd.DataFrame(rows)

# ──────────── PLOT ────────────
plt.style.use('ggplot')
fig, axes = plt.subplots(2, 2, figsize=(20, 15))
fig.suptitle(
    "Worst-Case Performance per Model  vs  Baseline Zero-Shot\n"
    "(each subplot picks the worst agent+style for THAT specific metric)",
    fontsize=16, fontweight='bold', y=0.99
)

subplot_cfg = [
    ("Correctness",     axes[0, 0], "Worst Case: Functional Correctness",           "YlOrRd",    (0, 1.20)),
    ("Coverage",        axes[0, 1], "Worst Case: Line Coverage",                    "OrRd",      (0, 120)),
    ("Efficiency (1k)", axes[1, 0], "Worst Case: Token Efficiency (Score/1k tok.)",  "Reds",      None),
    ("Maintainability", axes[1, 1], "Worst Case: Maintainability Index",            "RdPu",      None),
]

for metric_name, ax, title, palette, ylim in subplot_cfg:
    pdf = plot_frames[metric_name]

    bars = sns.barplot(
        x='Model', y='Value', data=pdf, ax=ax,
        hue='Model', palette=palette, legend=False
    )
    ax.set_title(title, fontsize=13, fontweight='bold')

    if ylim:
        ax.set_ylim(*ylim)
    else:
        # Use BL values to set a sensible ceiling (worst bars are small,
        # but BL-ZS lines may be much higher)
        bl_max = pdf['BL Value'].max()
        val_max = pdf['Value'].max()
        ymax = max(bl_max, val_max) if pd.notna(bl_max) else val_max
        ax.set_ylim(0, ymax * 1.50)

    # Annotate each bar + draw BL-ZS reference line
    bl_line_drawn = False
    for idx, bar in enumerate(bars.patches):
        if idx >= len(pdf):
            break
        row = pdf.iloc[idx]
        x_center = bar.get_x() + bar.get_width() / 2
        x_left   = bar.get_x()
        x_right  = bar.get_x() + bar.get_width()
        y = bar.get_height()
        bl_val = row["BL Value"]

        combo_label = row["Worst Combo"]
        pct = row["pct"]

        # ── Baseline Zero-Shot reference line on the bar ──
        if pd.notna(bl_val):
            lbl = "BL Zero-Shot" if not bl_line_drawn else None
            ax.hlines(
                y=bl_val,
                xmin=x_left - bar.get_width() * 0.12,
                xmax=x_right + bar.get_width() * 0.12,
                colors='#1565c0', linewidths=2.2, linestyles='--',
                label=lbl, zorder=5
            )
            bl_line_drawn = True

        # Percentage change text & colour
        if pd.notna(pct):
            if abs(pct) < 0.05:
                pct_text = "0.0%"
                pct_color = "#555555"
            else:
                sign = "+" if pct >= 0 else ""
                pct_text = f"{sign}{pct:.1f}%"
                # For worst-case: negative = degradation (red), positive = still above BL (green)
                pct_color = "#2e7d32" if pct >= 0 else "#c62828"
        else:
            pct_text = "N/A"
            pct_color = "gray"

        y_span = ax.get_ylim()[1]

        # Combo name above bar
        ax.text(x_center, y + y_span * 0.015, combo_label,
                ha='center', va='bottom', fontsize=6.5, fontweight='bold',
                rotation=30, color='#333333')

        # Percentage change badge above combo name
        ax.text(x_center, y + y_span * 0.09, f"vs BL-ZS: {pct_text}",
                ha='center', va='bottom', fontsize=7, fontweight='bold',
                rotation=0, color=pct_color,
                bbox=dict(boxstyle='round,pad=0.15', facecolor='white',
                          edgecolor=pct_color, alpha=0.85, linewidth=0.6))

    ax.legend(loc='upper right', fontsize=8, framealpha=0.9)
    ax.tick_params(axis='x', rotation=45, labelsize=9)
    ax.set_xlabel("")
    ax.set_ylabel(metric_name)

plt.tight_layout(rect=[0, 0, 1, 0.95])

# ─── Save ───
out1 = 'scratch/06_best_case_comparison/worst_case_comparison.png'
plt.savefig(out1, dpi=180, bbox_inches='tight')
print(f"Saved -> {out1}")

# ─── Console summary ───
print("\n" + "=" * 95)
print("Per-Metric WORST Combination for each Model:")
print("=" * 95)
for metric_name in metric_map:
    print(f"\n  --- {metric_name} ---")
    pdf = plot_frames[metric_name]
    for _, r in pdf.iterrows():
        pct = r['pct']
        if pd.notna(pct):
            pct_s = f"{'+' if pct >= 0 else ''}{pct:.1f}%"
        else:
            pct_s = "N/A"
        print(f"    {r['Model']:15s}  worst={r['Value']:.4f}  bl_zs={r['BL Value']:.4f}"
              f"  delta={pct_s:>8s}  combo=[{r['Worst Combo']}]")
