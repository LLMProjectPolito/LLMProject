import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_best_worst_combinations(results_dir, output_dir):
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
        'line_coverage': 'mean'
    }
    
    agg_dict = {col: func for col, func in metrics_to_agg.items() if col in combined_df.columns}
    
    group = combined_df.groupby(['model_family', 'agent', 'config_label']).agg(agg_dict).reset_index()

    for model in group['model_family'].unique():
        model_group = group[group['model_family'] == model]
        
        sorted_group = model_group.sort_values(
            by=['functional_correctness', 'line_coverage'] if 'line_coverage' in model_group.columns else ['functional_correctness'], 
            ascending=[False, False] if 'line_coverage' in model_group.columns else [False]
        )
        
        top_10 = sorted_group.head(10)
        bottom_5 = sorted_group.tail(5)
        
        # Combine top 10 and bottom 5 for the plot
        # Add a placeholder row so there is a visual gap between top and bottom
        combined_plot_data = pd.concat([top_10, pd.DataFrame([{'agent': '', 'config_label': '---', 'functional_correctness': 0}]), bottom_5])
        
        # Reverse to have the best at the top of the horizontal bar chart
        combined_plot_data = combined_plot_data.iloc[::-1]

        fig, ax = plt.subplots(figsize=(10, 8))
        labels = combined_plot_data['agent'] + " - " + combined_plot_data['config_label']
        values = combined_plot_data['functional_correctness']
        
        colors = ['red' if i < 5 else 'grey' if label.endswith('---') else 'green' for i, label in enumerate(labels)]
        
        bars = ax.barh(labels, values, color=colors)
        
        ax.set_xlabel('Functional Correctness')
        ax.set_title(f'Functional Correctness: Top 10 & Bottom 5 - {model.upper()}')
        ax.set_xlim(0, 1) # Assuming functional correctness is between 0 and 1
        
        # Add labels to the right of the bars
        for bar in bars:
            width = bar.get_width()
            if width > 0:
                ax.text(width + 0.01, bar.get_y() + bar.get_height()/2, f'{width:.2f}', ha='left', va='center')

        plt.tight_layout()
        plot_path = os.path.join(output_dir, f"{model}_chart.png")
        plt.savefig(plot_path)
        plt.close()
        print(f"Creata chart per {model} in {plot_path}")

if __name__ == "__main__":
    results_path = r"c:\Users\j.osagie\OneDrive - Reply\Desktop\LLM\project_a1_evalplus\results"
    output_path = r"c:\Users\j.osagie\OneDrive - Reply\Desktop\LLM\project_a1_evalplus\scratch"
    plot_best_worst_combinations(results_path, output_path)
