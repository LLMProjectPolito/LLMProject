import os
import pandas as pd
import matplotlib.pyplot as plt

# Use the Polito-style palette
POLITO_BLUE = '#1B3A5C'      # dark navy blue (top performers)
POLITO_RED = '#8B1A1A'       # dark red (bottom performers)
BASELINE_BLUE = '#2E75B6'    # bright blue (baseline highlight)

def plot_best_worst_metric(results_dir, output_dir, metric_col, metric_label):
    all_data = []
    if not os.path.exists(results_dir):
        return

    # ALL 8 MODELS
    target_models = ["gemma-1b", "gemma-4b", "gemma-12b", "gemma-27b", "gemma-31b",
                     "gemma-4-2b", "gemma-4-4b", "gemma-4-26b"]
    
    for model in target_models:
        model_path = os.path.join(results_dir, model)
        if os.path.isdir(model_path):
            csv_path = os.path.join(model_path, 'results.csv')
            if os.path.exists(csv_path):
                try:
                    df = pd.read_csv(csv_path)
                    if not df.empty and metric_col in df.columns:
                        df['model_family'] = model
                        all_data.append(df)
                except Exception as e:
                    pass
                    
    if not all_data:
        print(f"No target models found with column {metric_col}.")
        return

    combined_df = pd.concat(all_data, ignore_index=True)
    
    # Fill NaN values with 0 if they represent failures
    combined_df[metric_col] = pd.to_numeric(combined_df[metric_col], errors='coerce').fillna(0)
    
    agg_dict = {metric_col: 'mean'}
    group = combined_df.groupby(['model_family', 'agent', 'config_label']).agg(agg_dict).reset_index()

    metric_out_dir = os.path.join(output_dir, metric_col)
    if not os.path.exists(metric_out_dir): 
        os.makedirs(metric_out_dir)

    for model in group['model_family'].unique():
        model_group = group[group['model_family'] == model].copy()
        
        # Find baseline + zero_shot
        baseline_mask = (model_group['agent'] == 'baseline') & (model_group['config_label'].str.contains('zero_shot'))
        baseline_row = model_group[baseline_mask]
        
        if not baseline_row.empty:
            base_val = baseline_row[metric_col].values[0]
            model_group['perc_change'] = ((model_group[metric_col] - base_val) / base_val) * 100 if base_val > 0 else 0
        else:
            base_val = None
            model_group['perc_change'] = 0

        sorted_group = model_group.sort_values(by=[metric_col], ascending=[False])
        
        top_10 = sorted_group.head(10)
        bottom_5 = sorted_group.tail(5)
        
        plot_data = pd.concat([top_10, bottom_5, baseline_row]).drop_duplicates().sort_values(metric_col, ascending=True)

        # --- POLITO-STYLE CHART ---
        fig, ax = plt.subplots(figsize=(14, 10))
        
        plot_data['style'] = plot_data['config_label'].apply(lambda x: str(x).split(':')[-1])
        labels = plot_data['agent'] + ' · ' + plot_data['style']
        values = plot_data[metric_col]
        changes = plot_data['perc_change']
        
        top_10_threshold = top_10[metric_col].min()
        
        colors = []
        for _, row in plot_data.iterrows():
            if row['agent'] == 'baseline' and 'zero_shot' in str(row['config_label']):
                colors.append(BASELINE_BLUE) 
            elif row[metric_col] >= top_10_threshold:
                colors.append(POLITO_BLUE)
            else:
                colors.append(POLITO_RED)
        
        bars = ax.barh(labels, values, color=colors, edgecolor='white', linewidth=0.5)
        
        ax.set_xlabel(f'{metric_label} (mean over 25 problems)', fontsize=12, fontweight='bold')
        ax.set_title(f'{model.upper()} — 10 best (blue) and 5 worst (red) for {metric_label}', fontsize=14, fontweight='bold')
        ax.set_xlim(0, max(values) * 1.2 if max(values) > 0 else 1)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.tick_params(axis='y', labelsize=10)
        ax.tick_params(axis='x', labelsize=10)
        
        for i, bar in enumerate(bars):
            width = bar.get_width()
            change = changes.iloc[i]
            is_baseline = (plot_data.iloc[i]['agent'] == 'baseline' and 'zero_shot' in str(plot_data.iloc[i]['config_label']))
            
            label_text = f'{width:.2f}'
            if base_val is not None and not is_baseline:
                label_text += f' ({change:+.1f}%)'
            
            ax.text(width + (max(values)*0.01), bar.get_y() + bar.get_height()/2, label_text,
                    ha='left', va='center', fontsize=9, fontweight='bold', color='#333333')

        plt.tight_layout()
        plot_path = os.path.join(metric_out_dir, f"{model}_{metric_col}_chart.png")
        plt.savefig(plot_path, dpi=150, bbox_inches='tight', facecolor='white')
        plt.close()
        print(f"Chart saved to {plot_path}")

if __name__ == "__main__":
    results_path = r"results"
    output_path = r"scratch\11_best_coverage_mutation\plots"
    
    print("Generating Line Coverage plots...")
    plot_best_worst_metric(results_path, output_path, 'line_coverage', 'Line Coverage (%)')
    
    print("\nGenerating Mutation Score plots...")
    plot_best_worst_metric(results_path, output_path, 'mutation_score', 'Mutation Score')
