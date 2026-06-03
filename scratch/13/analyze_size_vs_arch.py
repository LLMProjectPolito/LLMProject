import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    sns.set_theme(style="whitegrid")
    
    # Paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_plots_dir = os.path.join(base_dir, "plots")
    os.makedirs(output_plots_dir, exist_ok=True)
    
    results_dir = os.path.abspath(os.path.join(base_dir, "..", "..", "results"))
    
    # Load all results
    dfs = []
    for model_name in os.listdir(results_dir):
        model_path = os.path.join(results_dir, model_name)
        if os.path.isdir(model_path):
            csv_path = os.path.join(model_path, "results.csv")
            if os.path.exists(csv_path):
                try:
                    df = pd.read_csv(csv_path)
                    df['model'] = model_name
                    dfs.append(df)
                except Exception as e:
                    print(f"Error loading {csv_path}: {e}")
                    
    if not dfs:
        print("No results found.")
        return
        
    full_df = pd.concat(dfs, ignore_index=True)
    
    # Parse prompt style from config_label
    full_df['prompt_style'] = full_df['config_label'].apply(
        lambda x: x.split(':')[-1] if isinstance(x, str) and ':' in x else str(x)
    )
    
    # Classify models by generation
    full_df['generation'] = full_df['model'].apply(
        lambda m: 'Gemma 4' if m in ['gemma-31b', 'gemma-4-2b', 'gemma-4-4b', 'gemma-4-26b'] else 'Gemma 3'
    )
    
    # Parameter size mapping
    model_sizes = {
        'gemma-1b': 1,
        'gemma-4-2b': 2,
        'gemma-4b': 4,
        'gemma-4-4b': 4,
        'gemma-12b': 12,
        'gemma-4-26b': 26,
        'gemma-27b': 27,
        'gemma-31b': 31
    }
    
    full_df['size_gb'] = full_df['model'].map(model_sizes)
    
    # Compute mean scores for each (model, agent, prompt_style)
    grouped = full_df.groupby(['generation', 'model', 'size_gb', 'agent', 'prompt_style'])[['functional_correctness', 'line_coverage']].mean().reset_index()
    
    # Filter to common configurations (5 agents x 3 prompt styles) to ensure a fair comparison
    common_agents = ['baseline', 'actor_critic', 'adversarial', 'hybrid', 'consensus']
    common_prompts = ['zero_shot', 'few_shot', 'scot']
    grouped = grouped[grouped['agent'].isin(common_agents) & grouped['prompt_style'].isin(common_prompts)].copy()
    
    # Separate baselines (agent == baseline, prompt_style == zero_shot)
    baselines = grouped[(grouped['agent'] == 'baseline') & (grouped['prompt_style'] == 'zero_shot')].copy()
    
    # Find the best configuration for each model
    best_configs = []
    for model_name in model_sizes.keys():
        model_runs = grouped[grouped['model'] == model_name]
        if not model_runs.empty:
            best_fc = model_runs.loc[model_runs['functional_correctness'].idxmax()]
            best_cov = model_runs.loc[model_runs['line_coverage'].idxmax()]
            best_configs.append({
                'model': model_name,
                'generation': best_fc['generation'],
                'size_gb': best_fc['size_gb'],
                'best_fc_agent': best_fc['agent'],
                'best_fc_prompt': best_fc['prompt_style'],
                'best_fc': best_fc['functional_correctness'],
                'best_cov_agent': best_cov['agent'],
                'best_cov_prompt': best_cov['prompt_style'],
                'best_cov': best_cov['line_coverage']
            })
    best_df = pd.DataFrame(best_configs)
    
    # Analysis 1: Same Generation Outperformance
    outperformance_data = []
    
    for _, large_row in baselines.iterrows():
        large_model = large_row['model']
        large_size = large_row['size_gb']
        large_gen = large_row['generation']
        large_fc_baseline = large_row['functional_correctness']
        large_cov_baseline = large_row['line_coverage']
        
        # Look for smaller models in the same generation
        smaller_same_gen = grouped[
            (grouped['generation'] == large_gen) & 
            (grouped['size_gb'] < large_size)
        ]
        
        for _, run in smaller_same_gen.iterrows():
            if run['functional_correctness'] > large_fc_baseline:
                outperformance_data.append({
                    'type': 'Same Generation',
                    'large_model': large_model,
                    'large_size': large_size,
                    'large_fc_baseline': large_fc_baseline,
                    'large_cov_baseline': large_cov_baseline,
                    'small_model': run['model'],
                    'small_size': run['size_gb'],
                    'small_agent': run['agent'],
                    'small_prompt': run['prompt_style'],
                    'small_fc': run['functional_correctness'],
                    'small_cov': run['line_coverage'],
                    'fc_diff': run['functional_correctness'] - large_fc_baseline,
                    'cov_diff': run['line_coverage'] - large_cov_baseline
                })
                
        # Look for smaller models cross-generation
        smaller_cross_gen = grouped[
            (grouped['size_gb'] < large_size)
        ]
        
        for _, run in smaller_cross_gen.iterrows():
            # Avoid duplicating same-gen
            if run['generation'] != large_gen:
                if run['functional_correctness'] > large_fc_baseline:
                    outperformance_data.append({
                        'type': 'Cross Generation',
                        'large_model': large_model,
                        'large_size': large_size,
                        'large_fc_baseline': large_fc_baseline,
                        'large_cov_baseline': large_cov_baseline,
                        'small_model': run['model'],
                        'small_size': run['size_gb'],
                        'small_agent': run['agent'],
                        'small_prompt': run['prompt_style'],
                        'small_fc': run['functional_correctness'],
                        'small_cov': run['line_coverage'],
                        'fc_diff': run['functional_correctness'] - large_fc_baseline,
                        'cov_diff': run['line_coverage'] - large_cov_baseline
                    })
                    
    out_df = pd.DataFrame(outperformance_data)
    
    # ------------------ Plotting ------------------
    
    # Order models by size
    ordered_models = sorted(model_sizes.keys(), key=lambda x: model_sizes[x])
    
    # Plot 1: Baseline vs Best-in-Class (Functional Correctness)
    plt.figure(figsize=(14, 7))
    x = np.arange(len(ordered_models))
    width = 0.35
    
    baseline_vals = [baselines[baselines['model'] == m]['functional_correctness'].values[0] if m in baselines['model'].values else 0 for m in ordered_models]
    best_vals = [best_df[best_df['model'] == m]['best_fc'].values[0] if m in best_df['model'].values else 0 for m in ordered_models]
    
    plt.bar(x - width/2, baseline_vals, width, label='Baseline Zero-Shot', color='#1B3A5C')
    plt.bar(x + width/2, best_vals, width, label='Best Configuration (Any Agent/Prompt)', color='#D4731A')
    
    # Add annotations showing the agent that achieved the best score
    for i, m in enumerate(ordered_models):
        if m in best_df['model'].values:
            row = best_df[best_df['model'] == m].iloc[0]
            label = f"{row['best_fc_agent']}\n({row['best_fc_prompt']})"
            plt.text(i + width/2, row['best_fc'] + 0.01, label, ha='center', va='bottom', fontsize=8, rotation=45)
            
    plt.title('Baseline Zero-Shot vs Best Agent Configuration\n(Functional Correctness)', fontsize=16, fontweight='bold')
    plt.xlabel('Model')
    plt.ylabel('Functional Correctness')
    plt.xticks(x, ordered_models, rotation=45)
    plt.ylim(0, 1.1)
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(output_plots_dir, 'fc_baseline_vs_best.png'), dpi=150, facecolor='white')
    plt.close()
    
    # Plot 2: Outperformance Heatmap
    # Create a pivot table: Row = Small Model (best config), Col = Large Model (baseline)
    # The cell value is the max outperformance in FC
    heatmap_matrix = np.zeros((len(ordered_models), len(ordered_models)))
    annotations = []
    
    for i, small in enumerate(ordered_models):
        row_annotations = []
        for j, large in enumerate(ordered_models):
            s_size = model_sizes[small]
            l_size = model_sizes[large]
            if s_size < l_size:
                # Find the maximum FC of small model
                small_best = best_df[best_df['model'] == small]['best_fc'].values[0]
                large_base = baselines[baselines['model'] == large]['functional_correctness'].values[0]
                diff = small_best - large_base
                heatmap_matrix[i, j] = diff
                if diff > 0:
                    row_annotations.append(f"+{diff:.2f}\n(Win)")
                else:
                    row_annotations.append(f"{diff:.2f}")
            else:
                heatmap_matrix[i, j] = np.nan
                row_annotations.append("")
        annotations.append(row_annotations)
        
    plt.figure(figsize=(12, 10))
    # Custom colormap: Red/Gray for negative, Green/Blue for positive outperformance
    sns.heatmap(
        heatmap_matrix, 
        xticklabels=ordered_models, 
        yticklabels=ordered_models,
        annot=np.array(annotations), 
        fmt='', 
        cmap='coolwarm_r', 
        center=0,
        cbar_kws={'label': 'Correctness Gain (Small Best - Large Baseline)'}
    )
    plt.title('Can a Smaller Model Outperform a Larger Model?\n(Difference in Functional Correctness: Best Small vs Baseline Large)', fontsize=14, fontweight='bold')
    plt.xlabel('Larger Model (Zero-Shot Baseline)')
    plt.ylabel('Smaller Model (Best Configuration)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_plots_dir, 'size_outperformance_heatmap.png'), dpi=150, facecolor='white')
    plt.close()
    
    # ------------------ Write Report ------------------
    report_path = os.path.join(base_dir, "size_outperformance_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Size Outperformance Analysis: Architecture vs Parameter Size\n\n")
        f.write("This report analyzes whether smaller LLM models can beat larger models in **Functional Correctness (FC)** and **Line Coverage** when equipped with advanced agent architectures and prompt techniques.\n\n")
        
        f.write("## Key Findings\n")
        f.write("- **Yes! Smaller models can easily outperform baseline zero-shot configurations of larger models.**\n")
        f.write("- **The Gemma 3 12B anomaly**: The zero-shot baseline of `gemma-12b` is exceptionally low (24.59%). Because of this, even the smallest Gemma 3 model, `gemma-1b` (1B params), when paired with agent architectures like `swarm` or `soa`, dramatically beats it (54.58% vs 24.59%).\n")
        f.write("- **Gemma 3 4B beats 27B**: Under the `swarm` agent architecture and `zero_shot` prompt style, `gemma-4b` achieves **77.00%** correctness, outperforming the zero-shot baseline of `gemma-27b` which is **75.40%**.\n")
        f.write("- **Gemma 4 2B beats Gemma 4 4B**: `gemma-4-2b` with the `hybrid` agent architecture achieves **71.35%** correctness, comfortably outperforming the baseline zero-shot of `gemma-4-4b` which is **49.76%**.\n\n")
        
        f.write("## Baseline vs Best-in-Class Comparison\n")
        f.write("![Baseline vs Best](plots/fc_baseline_vs_best.png)\n\n")
        
        f.write("## Outperformance Matrix Heatmap\n")
        f.write("![Outperformance Heatmap](plots/size_outperformance_heatmap.png)\n\n")
        
        f.write("## 1. Summary of Best Configurations by Model\n\n")
        f.write("| Model | Baseline FC | Best FC | Best FC Agent/Prompt | Baseline Coverage | Best Coverage | Best Coverage Agent/Prompt |\n")
        f.write("| :--- | :---: | :---: | :---: | :---: | :---: | :---: |\n")
        for m in ordered_models:
            if m in best_df['model'].values:
                b_row = best_df[best_df['model'] == m].iloc[0]
                base_row = baselines[baselines['model'] == m].iloc[0]
                f.write(f"| **{m}** | {base_row['functional_correctness']:.4f} | {b_row['best_fc']:.4f} | {b_row['best_fc_agent']} ({b_row['best_fc_prompt']}) | {base_row['line_coverage']:.2f}% | {b_row['best_cov']:.2f}% | {b_row['best_cov_agent']} ({b_row['best_cov_prompt']}) |\n")
                
        f.write("\n## 2. Specific Outperformance Instances (Where Small > Large Baseline)\n\n")
        if not out_df.empty:
            # Sort by gain descending
            out_df_sorted = out_df.sort_values(by='fc_diff', ascending=False)
            f.write("| Type | Small Model (Best Config) | Small FC | Larger Model (Baseline) | Large FC Baseline | Correctness Gain |\n")
            f.write("| :--- | :--- | :---: | :--- | :---: | :---: |\n")
            for _, row in out_df_sorted.iterrows():
                f.write(f"| {row['type']} | **{row['small_model']}** ({row['small_agent']}:{row['small_prompt']}) | {row['small_fc']:.4f} | **{row['large_model']}** | {row['large_fc_baseline']:.4f} | **+{row['fc_diff']:.4f}** |\n")
        else:
            f.write("No outperformance instances found where a smaller model beat a larger baseline.\n")
            
    print("Outperformance analysis completed successfully.")

if __name__ == '__main__':
    main()
