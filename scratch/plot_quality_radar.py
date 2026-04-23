import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_quality_radar(results_dir, output_dir):
    all_data = []
    if not os.path.exists(results_dir):
        print(f"Directory {results_dir} non trovata.")
        return

    for model in os.listdir(results_dir):
        model_path = os.path.join(results_dir, model)
        if os.path.isdir(model_path):
            csv_path = os.path.join(model_path, 'results.csv')
            if os.path.exists(csv_path):
                try:
                    df = pd.read_csv(csv_path)
                    if not df.empty:
                        df['model_family'] = model
                        all_data.append(df)
                except Exception as e:
                    pass
                    
    if not all_data:
        print("Nessun dato trovato.")
        return

    combined_df = pd.concat(all_data, ignore_index=True)
    metrics_to_agg = {
        'functional_correctness': 'mean',
        'line_coverage': 'mean',
        'branch_coverage': 'mean',
        'mutation_score': 'mean',
        'maintainability_mi': 'mean'
    }
    agg_dict = {col: func for col, func in metrics_to_agg.items() if col in combined_df.columns}
    
    group = combined_df.groupby(['model_family', 'agent', 'config_label']).agg(agg_dict).reset_index()

    metrics = ['line_coverage', 'branch_coverage', 'mutation_score', 'maintainability_mi']
    
    for model in group['model_family'].unique():
        model_group = group[group['model_family'] == model].copy()
        
        # Sort by correctness to get top 3
        sorted_group = model_group.sort_values(by=['functional_correctness'], ascending=[False]).head(3)
        
        if sorted_group.empty:
            continue
            
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, polar=True)
        
        angles = np.linspace(0, 2 * np.pi, len(metrics), endpoint=False).tolist()
        angles += angles[:1]
        
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(['Line Cov (%)', 'Branch Cov (%)', 'Mutation Score (x100)', 'Maintainability (%)'])
        ax.set_ylim(0, 100)
        
        colors = ['b', 'r', 'g']
        
        for i, (_, row) in enumerate(sorted_group.iterrows()):
            lc = row['line_coverage'] if 'line_coverage' in row else 0
            bc = row['branch_coverage'] if 'branch_coverage' in row else 0
            ms = (row['mutation_score'] * 100) if 'mutation_score' in row else 0
            mi = row['maintainability_mi'] if 'maintainability_mi' in row else 0
            
            values = [lc, bc, ms, mi]
            values += values[:1]
            
            label = f"{row['agent']} - {row['config_label'].split(':')[-1]}"
            ax.plot(angles, values, color=colors[i], linewidth=2, label=label)
            ax.fill(angles, values, color=colors[i], alpha=0.1)
            
        plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
        plt.title(f'Code Quality & Testing (Top 3) - {model.upper()}', size=15, y=1.1)
        
        plot_path = os.path.join(output_dir, f"{model}_quality_radar.png")
        plt.savefig(plot_path, bbox_inches='tight')
        plt.close()
        print(f"Creata radar chart qualità per {model} in {plot_path}")

if __name__ == "__main__":
    results_path = r"c:\Users\j.osagie\OneDrive - Reply\Desktop\LLM\project_a1_evalplus\results"
    output_path = r"c:\Users\j.osagie\OneDrive - Reply\Desktop\LLM\project_a1_evalplus\scratch"
    plot_quality_radar(results_path, output_path)
