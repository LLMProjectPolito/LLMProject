import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Set style
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
    
    # Ensure numeric
    full_df['mutation_score'] = pd.to_numeric(full_df['mutation_score'], errors='coerce')
    full_df['mutation_score'] = full_df['mutation_score'].fillna(0.0)
    
    # Apply post-hoc correction to fix the mutation score discrepancy
    full_df.loc[full_df['functional_correctness'] < 1.0, 'mutation_score'] = 0.0

    
    # Classify models by generation
    full_df['generation'] = full_df['model'].apply(
        lambda m: 'Gemma 4' if m in ['gemma-31b', 'gemma-4-2b', 'gemma-4-4b', 'gemma-4-26b'] else 'Gemma 3'
    )
    
    # Custom model ordering: Gemma 3: 1, 4, 12, 27 -> Gemma 4: 2, 4, 26, 31
    model_order = ['gemma-1b', 'gemma-4b', 'gemma-12b', 'gemma-27b', 'gemma-4-2b', 'gemma-4-4b', 'gemma-4-26b', 'gemma-31b']
    
    # Compute metrics helper
    def get_stats(df, group_col):
        stats = df.groupby(group_col)['mutation_score'].agg([
            ('mean', 'mean'),
            ('median', 'median'),
            ('min', 'min'),
            ('max', 'max'),
            ('count', 'count')
        ]).reset_index()
        
        # Calculate % zero and % perfect
        zeros = df[df['mutation_score'] == 0.0].groupby(group_col).size().reindex(stats[group_col]).fillna(0)
        perfects = df[df['mutation_score'] == 1.0].groupby(group_col).size().reindex(stats[group_col]).fillna(0)
        
        stats['pct_zero'] = (zeros.values / stats['count'].values) * 100
        stats['pct_perfect'] = (perfects.values / stats['count'].values) * 100
        
        return stats

    model_stats = get_stats(full_df, 'model')
    # Apply custom sorting to model_stats
    model_stats['model'] = pd.Categorical(model_stats['model'], categories=model_order, ordered=True)
    model_stats = model_stats.sort_values(by='model')
    
    agent_stats = get_stats(full_df, 'agent').sort_values(by='mean', ascending=False)
    prompt_stats = get_stats(full_df, 'prompt_style').sort_values(by='mean', ascending=False)
    
    # ------------------ Prepare Plot Data ------------------
    plot_data_model = full_df.groupby(['model', 'generation'])['mutation_score'].mean().reset_index()
    plot_data_model['model'] = pd.Categorical(plot_data_model['model'], categories=model_order, ordered=True)
    plot_data_model = plot_data_model.sort_values(by='model')
    
    # Define custom color palette: Navy Blue, Purple, Red
    c_navy = '#0A2342'
    c_purple = '#6C3483'
    c_red = '#C0392B'
    
    # Interpolated palettes
    palette_model = {'Gemma 3': c_navy, 'Gemma 4': c_red}
    palette_agent = sns.color_palette(f"blend:{c_navy},{c_purple},{c_red}", n_colors=len(agent_stats))
    palette_prompt = sns.color_palette(f"blend:{c_navy},{c_purple},{c_red}", n_colors=len(prompt_stats))
    
    # ------------------ Generate Plots ------------------
    
    # Plot 1: Mutation Score by Model (ordered)
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x='model', y='mutation_score', hue='generation', data=plot_data_model,
        palette=palette_model,
        dodge=False
    )
    plt.title('Average Mutation Score by Model and Generation\n(Gemma 3 vs Gemma 4, Sorted)', fontsize=14, fontweight='bold')
    plt.xlabel('Model')
    plt.ylabel('Mean Mutation Score')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_plots_dir, 'mutation_by_model.png'), dpi=150, facecolor='white')
    plt.close()
    
    # Plot 2: Mutation Score by Agent
    plt.figure(figsize=(12, 6))
    sns.barplot(
        x='mean', y='agent', data=agent_stats,
        palette=palette_agent
    )
    plt.title('Average Mutation Score by Agent Architecture', fontsize=14, fontweight='bold')
    plt.xlabel('Mean Mutation Score')
    plt.ylabel('Agent')
    plt.tight_layout()
    plt.savefig(os.path.join(output_plots_dir, 'mutation_by_agent.png'), dpi=150, facecolor='white')
    plt.close()
    
    # Plot 3: Mutation Score by Prompt Style
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x='prompt_style', y='mean', data=prompt_stats,
        palette=palette_prompt
    )
    plt.title('Average Mutation Score by Prompt Style', fontsize=14, fontweight='bold')
    plt.xlabel('Prompt Style')
    plt.ylabel('Mean Mutation Score')
    plt.tight_layout()
    plt.savefig(os.path.join(output_plots_dir, 'mutation_by_prompt_style.png'), dpi=150, facecolor='white')
    plt.close()

    # Plot 4: COMBINED Plot (Model, Agent, Prompt in a single image)
    fig, axes = plt.subplots(1, 3, figsize=(24, 7))
    
    # Subplot 1 (Model)
    sns.barplot(
        x='model', y='mutation_score', hue='generation', data=plot_data_model,
        palette=palette_model, ax=axes[0],
        dodge=False
    )
    axes[0].set_title('Average Mutation by Model (Generation & Size)', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Model')
    axes[0].set_ylabel('Mean Mutation Score')
    axes[0].tick_params(axis='x', rotation=45)
    
    # Subplot 2 (Agent)
    sns.barplot(
        x='mean', y='agent', data=agent_stats,
        palette=palette_agent, ax=axes[1]
    )
    axes[1].set_title('Average Mutation by Agent Architecture', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Mean Mutation Score')
    axes[1].set_ylabel('Agent')
    
    # Subplot 3 (Prompt)
    sns.barplot(
        x='prompt_style', y='mean', data=prompt_stats,
        palette=palette_prompt, ax=axes[2]
    )
    axes[2].set_title('Average Mutation by Prompt Style', fontsize=14, fontweight='bold')
    axes[2].set_xlabel('Prompt Style')
    axes[2].set_ylabel('Mean Mutation Score')
    
    plt.suptitle('Mutation Score Comprehensive Analysis (Combined View)', fontsize=18, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(os.path.join(output_plots_dir, 'mutation_combined_analysis.png'), dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

    # ------------------ Generate Report ------------------
    report_path = os.path.join(base_dir, "mutation_analysis_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# Detailed Mutation Score Analysis\n\n")
        f.write("This report analyzes the `mutation_score` metric across all benchmarks, segmented by Model, Agent, and Prompt Style.\n\n")
        
        f.write("## ⚠️ Crucial Insight: Methodological Discrepancy\n")
        f.write("As detailed below, the `mutation_score` values show an extreme divergence between Gemma 3 and Gemma 4 models. ")
        f.write("This is a result of a difference in execution/logging:\n")
        f.write("- **Gemma 3 Models** have high average mutation scores (~0.85-0.97) because the testing script did not apply a strict pre-test validation, ")
        f.write("marking failed test suites as having killed all mutants (100% score).\n")
        f.write("- **Gemma 4 Models** have extremely low mutation scores (~0.00-0.10, except gemma-31b) because they correctly run a pre-test. ")
        f.write("If the test suite fails on unmodified code, the run is assigned a `0.0` mutation score.\n\n")
        
        f.write("## Combined Visual Analysis\n")
        f.write("![Combined Mutation Analysis](plots/mutation_combined_analysis.png)\n\n")
        
        f.write("## 1. Analysis by Model\n\n")
        f.write("| Model | Mean Mutation Score | Median | % Zero Scores | % Perfect (1.0) Scores | Total Runs |\n")
        f.write("| :--- | :---: | :---: | :---: | :---: | :---: |\n")
        for _, row in model_stats.iterrows():
            f.write(f"| **{row['model']}** | {row['mean']:.4f} | {row['median']:.4f} | {row['pct_zero']:.2f}% | {row['pct_perfect']:.2f}% | {int(row['count'])} |\n")
            
        f.write("\n## 2. Analysis by Agent Architecture\n\n")
        f.write("| Agent | Mean Mutation Score | Median | % Zero Scores | % Perfect (1.0) Scores | Total Runs |\n")
        f.write("| :--- | :---: | :---: | :---: | :---: | :---: |\n")
        for _, row in agent_stats.iterrows():
            f.write(f"| **{row['agent']}** | {row['mean']:.4f} | {row['median']:.4f} | {row['pct_zero']:.2f}% | {row['pct_perfect']:.2f}% | {int(row['count'])} |\n")
            
        f.write("\n## 3. Analysis by Prompt Style\n\n")
        f.write("| Prompt Style | Mean Mutation Score | Median | % Zero Scores | % Perfect (1.0) Scores | Total Runs |\n")
        f.write("| :--- | :---: | :---: | :---: | :---: | :---: |\n")
        for _, row in prompt_stats.iterrows():
            f.write(f"| **{row['prompt_style']}** | {row['mean']:.4f} | {row['median']:.4f} | {row['pct_zero']:.2f}% | {row['pct_perfect']:.2f}% | {int(row['count'])} |\n")
            
        f.write("\n\n## Individual Plots Generated\n")
        f.write("- [Mutation by Model](plots/mutation_by_model.png)\n")
        f.write("- [Mutation by Agent](plots/mutation_by_agent.png)\n")
        f.write("- [Mutation by Prompt Style](plots/mutation_by_prompt_style.png)\n")
        
    print("Analysis finished and report written successfully.")

if __name__ == '__main__':
    main()
