import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_all_combos_scatter(results_dir, output_dir):
    for model in os.listdir(results_dir):
        model_path = os.path.join(results_dir, model)
        if os.path.isdir(model_path):
            csv_path = os.path.join(model_path, 'results.csv')
            if os.path.exists(csv_path):
                df = pd.read_csv(csv_path)
                
                # Aggregate by combination
                group = df.groupby(['agent', 'config_label']).agg({
                    'functional_correctness': 'mean',
                    'total_tokens': 'mean'
                }).reset_index()
                
                plt.figure(figsize=(12, 8))
                scatter = sns.scatterplot(
                    data=group, 
                    x='total_tokens', 
                    y='functional_correctness', 
                    hue='agent', 
                    style='agent',
                    s=100,
                    alpha=0.7
                )
                
                plt.title(f'Efficiency Scatter: All Combinations - {model.upper()}')
                plt.xlabel('Average Total Tokens')
                plt.ylabel('Functional Correctness')
                plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Agents')
                plt.grid(True, linestyle='--', alpha=0.6)
                plt.tight_layout()
                
                plot_path = os.path.join(output_dir, f"{model}_all_combos_scatter.png")
                plt.savefig(plot_path)
                plt.close()
                print(f"Scatter plot (all combos) created for {model}")

if __name__ == "__main__":
    if not os.path.exists('scratch/05b_model_specific_plots_all_combos'):
        os.makedirs('scratch/05b_model_specific_plots_all_combos')
    plot_all_combos_scatter('results', 'scratch/05b_model_specific_plots_all_combos')
