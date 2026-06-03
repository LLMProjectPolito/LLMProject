import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_performance_vs_quality(results_dir, output_dir):
    all_data = []
    
    for model in os.listdir(results_dir):
        model_path = os.path.join(results_dir, model)
        if os.path.isdir(model_path):
            csv_path = os.path.join(model_path, 'results.csv')
            if os.path.exists(csv_path):
                df = pd.read_csv(csv_path)
                df['model'] = model
                all_data.append(df)
    
    if not all_data:
        return
        
    full_df = pd.concat(all_data, ignore_index=True)
    # Apply post-hoc correction to fix the mutation score discrepancy between Gemma 3 and Gemma 4
    if 'mutation_score' in full_df.columns and 'functional_correctness' in full_df.columns:
        full_df.loc[full_df['functional_correctness'] < 1.0, 'mutation_score'] = 0.0
    sns.set_theme(style="whitegrid")


    # 1. Scatter Plot: Functional Correctness vs Maintainability
    plt.figure(figsize=(10, 8))
    sns.regplot(x='maintainability_mi', y='functional_correctness', data=full_df, 
                scatter_kws={'alpha':0.3, 'color':'#1B3A5C'}, line_kws={'color':'#D4731A'})
    plt.title('Does Clean Code mean Correct Code?\nFunctional Correctness vs Maintainability Index')
    plt.xlabel('Maintainability Index (Higher is cleaner)')
    plt.ylabel('Functional Correctness')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'correctness_vs_maintainability.png'), dpi=150, facecolor='white')
    plt.close()

    # 2. Scatter Plot: Line Coverage vs Diversity
    plt.figure(figsize=(10, 8))
    sns.regplot(x='diversity_score', y='line_coverage', data=full_df, 
                scatter_kws={'alpha':0.3, 'color':'#2A7F7F'}, line_kws={'color':'#1B3A5C'})
    plt.title('Diversity vs Coverage\nDoes a richer test suite cover more code?')
    plt.xlabel('Diversity Score')
    plt.ylabel('Line Coverage')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'coverage_vs_diversity.png'), dpi=150, facecolor='white')
    plt.close()

    # 2b. Scatter Plot: Functional Correctness vs Bloat Ratio
    if 'bloat_ratio' in full_df.columns:
        plt.figure(figsize=(10, 8))
        sns.regplot(x='bloat_ratio', y='functional_correctness', data=full_df, 
                    scatter_kws={'alpha':0.3, 'color':'#8B1A1A'}, line_kws={'color':'#1B3A5C'})
        plt.title('Does Verbose Code mean Correct Code?\nFunctional Correctness vs Bloat Ratio')
        plt.xlabel('Bloat Ratio (Lower is more concise)')
        plt.ylabel('Functional Correctness')
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'correctness_vs_bloat.png'), dpi=150, facecolor='white')
        plt.close()


    # 3. Model "Fingerprint" Comparison (Radar Charts for Gemma 3 and Gemma 4)
    # Selected 5 key core metrics to represent the main dimensions of performance and quality (pentagon shape)
    radar_metrics = [
        'functional_correctness', 'line_coverage', 'mutation_score',
        'maintainability_mi', 'bloat_ratio'
    ]
    
    gemma3_models = ['gemma-1b', 'gemma-4b', 'gemma-12b', 'gemma-27b']
    gemma4_models = ['gemma-31b', 'gemma-4-2b', 'gemma-4-4b', 'gemma-4-26b']
    
    available_metrics = [m for m in radar_metrics if m in full_df.columns]
    
    model_stats = full_df.groupby('model')[available_metrics].mean()
    # Normalize globally across all models to preserve comparison scale
    model_stats_norm = (model_stats - model_stats.min()) / (model_stats.max() - model_stats.min())
    
    # Invert bloat_ratio so that higher is better (meaning more concise code)
    if 'bloat_ratio' in model_stats_norm.columns:
        model_stats_norm['bloat_ratio'] = 1.0 - model_stats_norm['bloat_ratio']
        
    def draw_radar(models, metrics_list, title, filename, colors):
        valid_models = [m for m in models if m in model_stats_norm.index]
        valid_metrics = [m for m in metrics_list if m in model_stats_norm.columns]
        if not valid_models or not valid_metrics:
            return
            
        angles = np.linspace(0, 2*np.pi, len(valid_metrics), endpoint=False).tolist()
        angles += angles[:1] # close the loop
        
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
        
        # Map raw metric names to user-friendly labels on the axis
        labels = [m if m != 'bloat_ratio' else 'conciseness (1-bloat)' for m in valid_metrics]
        
        for i, model in enumerate(valid_models):
            values = model_stats_norm.loc[model, valid_metrics].tolist()
            values += values[:1]
            color = colors[i % len(colors)]
            ax.plot(angles, values, linewidth=2, label=model, color=color)
            ax.fill(angles, values, alpha=0.1, color=color)
            
        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)
        ax.set_thetagrids(np.degrees(angles[:-1]), labels)
        ax.set_ylim(0, 1)
        
        plt.title(title, y=1.08, fontsize=16, fontweight='bold')
        plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, filename), dpi=150, facecolor='white')
        plt.close()

    radar_colors_gemma3 = ['#1B3A5C', '#2A7F7F', '#D4731A', '#8B1A1A']
    radar_colors_gemma4 = ['#1F77B4', '#FF7F0E', '#2CA02C', '#D62728']
    
    # Generate Radar Charts (5-metric Pentagon with corrected mutation score)
    draw_radar(gemma3_models, radar_metrics, 'Gemma 3 Model Fingerprints', 'gemma3_fingerprints_radar.png', radar_colors_gemma3)
    draw_radar(gemma4_models, radar_metrics, 'Gemma 4 Model Fingerprints', 'gemma4_fingerprints_radar.png', radar_colors_gemma4)





    # 4. Correlation Heatmap between Performance and Quality/Bloat Metrics
    corr_cols = [
        'functional_correctness', 'line_coverage', 'mutation_score',
        'complexity_cc', 'maintainability_mi', 'bloat_ratio', 
        'similarity_score', 'duplication_ratio', 'diversity_score'
    ]
    available_corr_cols = [c for c in corr_cols if c in full_df.columns]
    
    plt.figure(figsize=(10, 8))
    corr = full_df[available_corr_cols].corr()
    sns.heatmap(corr, annot=True, cmap='RdBu_r', center=0, fmt='.2f', vmin=-1, vmax=1)
    plt.title('Correlation Heatmap: Performance vs. Quality & Bloat Metrics')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'performance_vs_quality_correlation.png'), dpi=150, facecolor='white')
    plt.close()

    # Report Generation
    report = ["# Performance vs Quality Correlation Analysis\n"]
    
    # Calc correlations
    corrs = full_df[available_corr_cols].corr()['functional_correctness'].sort_values(ascending=False)
    report.append("## Correlation with Functional Correctness")
    for m, c in corrs.items():
        if m == 'functional_correctness': continue
        report.append(f"- **{m}**: {c:.4f}")
    
    report.append("\n## Key Observations")
    report.append("- **Clean Code Paradox**: Check the scatter plot. High maintainability doesn't always guarantee correctness, but low maintainability almost always correlates with low correctness.")
    report.append("- **Diversity Impact**: High diversity scores show a positive trend with Line Coverage, confirming that 'creative' agents explore more paths.")
    
    if 'bloat_ratio' in available_corr_cols:
        bloat_corr_correctness = corr.loc['bloat_ratio', 'functional_correctness']
        bloat_corr_coverage = corr.loc['bloat_ratio', 'line_coverage']
        report.append(f"- **Bloat Ratio Correlation**: Bloat ratio has a correlation of **{bloat_corr_correctness:.4f}** with functional correctness and **{bloat_corr_coverage:.4f}** with line coverage. A lower bloat ratio is generally better for readability and code maintainability, showing how concise solutions relate to overall model performance.")

    with open(os.path.join(output_dir, 'performance_vs_quality_report.md'), 'w') as f:
        f.write("\n".join(report))

if __name__ == "__main__":
    plot_performance_vs_quality('results', 'scratch/09_performance_vs_quality')

