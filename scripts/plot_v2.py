import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse
from pathlib import Path

def plot_v2(csv_path, out_dir):
    df = pd.read_csv(csv_path)
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    # Prepare data
    df["full_name"] = df.apply(lambda r: f"{r['agent']} ({r['config_label']})" if r['config_label'] != 'default' else r['agent'], axis=1)
    
    # 1. RADAR CHART (Combined)
    fig_radar = plt.figure(figsize=(10, 8))
    ax_radar = fig_radar.add_subplot(111, polar=True)
    
    radar_metrics = ["functional_correctness", "line_coverage", "mutation_score"]
    labels = ["Acc", "Cov", "Mut"]
    
    summary = df.groupby("full_name")[radar_metrics].mean().reset_index()
    # Normalizzazione per il radar (Line Cov da 100 a 1)
    radar_data = summary.copy()
    radar_data["line_coverage"] /= 100.0
    
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]

    for i, row in radar_data.iterrows():
        values = row[radar_metrics].values.flatten().tolist()
        values += values[:1]
        ax_radar.plot(angles, values, linewidth=2, label=row["full_name"])
        ax_radar.fill(angles, values, alpha=0.1)

    ax_radar.set_theta_offset(np.pi / 2)
    ax_radar.set_theta_direction(-1)
    ax_radar.set_thetagrids(np.degrees(angles[:-1]), labels)
    ax_radar.set_title("Radar Chart: Combined Metrics", size=15, pad=20)
    ax_radar.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    
    fig_radar.tight_layout()
    fig_radar.savefig(out_path / "radar_chart_combined.png")
    
    # 2. RADAR CHARTS (Individual)
    n_agents = len(summary)
    cols = 3
    rows = (n_agents + cols - 1) // cols
    fig_ind, axes = plt.subplots(rows, cols, subplot_kw={'projection': 'polar'}, figsize=(cols*5, rows*5))
    if n_agents == 1: axes = [axes]
    else: axes = axes.flatten()

    for i, (idx, row) in enumerate(radar_data.iterrows()):
        values = row[radar_metrics].values.flatten().tolist()
        values += values[:1]
        axes[i].plot(angles, values, linewidth=2, color='C'+str(i))
        axes[i].fill(angles, values, alpha=0.25, color='C'+str(i))
        axes[i].set_theta_offset(np.pi / 2)
        axes[i].set_theta_direction(-1)
        axes[i].set_thetagrids(np.degrees(angles[:-1]), labels)
        axes[i].set_title(row["full_name"], size=12)
    
    # Rimuovi assi vuoti
    for j in range(i + 1, len(axes)):
        fig_ind.delaxes(axes[j])
        
    fig_ind.tight_layout()
    fig_ind.savefig(out_path / "radar_charts_individual.png")

    # 3. EXTRA METRICS (Time, Bloat, Complexity)
    extra_metrics = ["elapsed_s", "bloat_ratio", "complexity_cc"]
    summary_extra = df.groupby("full_name")[extra_metrics].mean().reset_index()
    
    fig_extra, (ax_time, ax_bloat) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Time bar
    ax_time.bar(summary_extra["full_name"], summary_extra["elapsed_s"], color='skyblue')
    ax_time.set_title("Efficiency: Execution Time (s)")
    ax_time.set_ylabel("Seconds")
    ax_time.tick_params(axis='x', rotation=45)
    
    # Bloat bar
    ax_bloat.bar(summary_extra["full_name"], summary_extra["bloat_ratio"], color='lightcoral')
    ax_bloat.set_title("Bloat Ratio (Test LoC / Src LoC)")
    ax_bloat.axhline(1.0, color='red', linestyle='--', alpha=0.3)
    ax_bloat.tick_params(axis='x', rotation=45)

    fig_extra.tight_layout()
    fig_extra.savefig(out_path / "extra_metrics.png")

    print(f"Plots saved to {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    plot_v2(args.csv, args.out)
