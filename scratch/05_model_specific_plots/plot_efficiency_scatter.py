import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_efficiency(results_dir, output_dir):
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
        'total_tokens': 'mean'
    }
    agg_dict = {col: func for col, func in metrics_to_agg.items() if col in combined_df.columns}
    
    group = combined_df.groupby(['model_family', 'agent', 'config_label']).agg(agg_dict).reset_index()

    for model in group['model_family'].unique():
        model_group = group[group['model_family'] == model]
        
        sorted_group = model_group.sort_values(by=['functional_correctness'], ascending=[False]).head(10)
        
        fig, ax = plt.subplots(figsize=(8, 6))
        
        x = sorted_group['total_tokens']
        y = sorted_group['functional_correctness']
        labels = sorted_group['agent'] + " - " + sorted_group['config_label'].str.split(':').str[-1]
        
        ax.scatter(x, y, color='blue', s=100)
        
        for i, label in enumerate(labels):
            ax.annotate(label, (x.iloc[i], y.iloc[i]), xytext=(5, 5), textcoords='offset points', fontsize=9)
            
        ax.set_xlabel('Total Tokens (Cost)')
        ax.set_ylabel('Functional Correctness (Performance)')
        ax.set_title(f'Efficiency Trade-offs (Top 10) - {model.upper()}')
        ax.grid(True, linestyle='--', alpha=0.7)
        
        plt.tight_layout()
        plot_path = os.path.join(output_dir, f"{model}_efficiency_scatter.png")
        plt.savefig(plot_path)
        plt.close()
        print(f"Creata scatter plot efficienza per {model} in {plot_path}")

if __name__ == "__main__":
    results_path = r"c:\Users\j.osagie\OneDrive - Reply\Desktop\LLM\project_a1_evalplus\results"
    output_path = r"c:\Users\j.osagie\OneDrive - Reply\Desktop\LLM\project_a1_evalplus\scratch"
    plot_efficiency(results_path, output_path)
