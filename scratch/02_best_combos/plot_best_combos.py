import os
import pandas as pd
import matplotlib.pyplot as plt

def plot_best_worst_combinations(results_dir, output_dir):
    all_data = []
    if not os.path.exists(results_dir):
        print(f"Directory {results_dir} non trovata.")
        return

    # Models to include (Gen 3 + gemma-31b)
    target_models = ["gemma-1b", "gemma-4b", "gemma-12b", "gemma-27b", "gemma-31b"]
    
    for model in target_models:
        model_path = os.path.join(results_dir, model)
        if os.path.isdir(model_path):
            csv_path = os.path.join(model_path, 'results.csv')
            if os.path.exists(csv_path):
                print(f"Processing model: {model}")
                try:
                    df = pd.read_csv(csv_path)
                    if not df.empty:
                        df['model_family'] = model
                        all_data.append(df)
                except Exception as e:
                    print(f"Error loading {model}: {e}")
                    
    if not all_data:
        print("No target models found.")
        return

    combined_df = pd.concat(all_data, ignore_index=True)
    
    metrics_to_agg = {
        'functional_correctness': 'mean',
        'line_coverage': 'mean',
        'mutation_score': 'mean',
        'total_tokens': 'mean'
    }
    
    agg_dict = {col: func for col, func in metrics_to_agg.items() if col in combined_df.columns}
    group = combined_df.groupby(['model_family', 'agent', 'config_label']).agg(agg_dict).reset_index()

    for model in group['model_family'].unique():
        model_group = group[group['model_family'] == model].copy()
        print(f"\n--- Detailed Analysis for {model} ---")
        
        # Find baseline + zero_shot
        baseline_mask = (model_group['agent'] == 'baseline') & (model_group['config_label'].str.contains('zero_shot'))
        baseline_row = model_group[baseline_mask]
        
        if not baseline_row.empty:
            base_val = baseline_row['functional_correctness'].values[0]
            print(f"Baseline (zero_shot) Score: {base_val:.4f}")
            model_group['perc_change'] = ((model_group['functional_correctness'] - base_val) / base_val) * 100 if base_val > 0 else 0
        else:
            base_val = None
            print("Baseline (zero_shot) NOT found!")
            model_group['perc_change'] = 0

        sorted_group = model_group.sort_values(
            by=['functional_correctness', 'line_coverage'] if 'line_coverage' in model_group.columns else ['functional_correctness'], 
            ascending=[False, False] if 'line_coverage' in model_group.columns else [False]
        )
        
        top_1 = sorted_group.iloc[0]
        worst_1 = sorted_group.iloc[-1]
        
        print(f"BEST Combo:  {top_1['agent']} + {top_1['config_label']} | Score: {top_1['functional_correctness']:.4f} ({top_1['perc_change']:+.1f}%)")
        print(f"WORST Combo: {worst_1['agent']} + {worst_1['config_label']} | Score: {worst_1['functional_correctness']:.4f} ({worst_1['perc_change']:+.1f}%)")
        print(f"Avg Coverage: {model_group['line_coverage'].mean():.2f}%")
        print(f"Avg Tokens:   {model_group['total_tokens'].mean():.0f}")

        top_10 = sorted_group.head(10)
        bottom_5 = sorted_group.tail(5)
        
        plot_data = pd.concat([top_10, bottom_5, baseline_row]).drop_duplicates().sort_values('functional_correctness', ascending=True)

        fig, ax = plt.subplots(figsize=(14, 10))
        labels = plot_data['agent'] + " - " + plot_data['config_label']
        values = plot_data['functional_correctness']
        changes = plot_data['perc_change']
        
        colors = []
        for _, row in plot_data.iterrows():
            if row['agent'] == 'baseline' and 'zero_shot' in str(row['config_label']):
                colors.append('royalblue') 
            elif row['functional_correctness'] == sorted_group['functional_correctness'].max():
                colors.append('forestgreen')
            elif row['functional_correctness'] == sorted_group['functional_correctness'].min():
                colors.append('crimson')
            else:
                colors.append('gray')
        
        bars = ax.barh(labels, values, color=colors)
        ax.set_xlabel('Functional Correctness')
        ax.set_title(f'Functional Correctness: Top/Bottom vs Baseline (Blue) - {model.upper()}')
        ax.set_xlim(0, max(values) * 1.25)
        
        for i, bar in enumerate(bars):
            width = bar.get_width()
            change = changes.iloc[i]
            label_text = f'{width:.3f}'
            if base_val is not None and not (plot_data.iloc[i]['agent'] == 'baseline' and 'zero_shot' in str(plot_data.iloc[i]['config_label'])):
                label_text += f' ({change:+.1f}%)'
            
            ax.text(width + 0.01, bar.get_y() + bar.get_height()/2, label_text, ha='left', va='center', fontsize=9, fontweight='bold')

        plt.tight_layout()
        if not os.path.exists(output_dir): os.makedirs(output_dir)
        plot_path = os.path.join(output_dir, f"{model}_chart.png")
        plt.savefig(plot_path)
        plt.close()
        print(f"Chart saved to {plot_path}")

if __name__ == "__main__":
    results_path = r"c:\Users\j.osagie\OneDrive - Reply\Desktop\LLM\project_a1_evalplus\results"
    output_path = r"c:\Users\j.osagie\OneDrive - Reply\Desktop\LLM\project_a1_evalplus\scratch\02_best_combos\plots"
    plot_best_worst_combinations(results_path, output_path)
