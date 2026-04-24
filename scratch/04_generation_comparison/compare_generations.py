import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

# Define the pairs to compare (New vs Old)
pairs = [
    ("gemma-4-2b", "gemma-1b"),
    ("gemma-4-4b", "gemma-4b"),
    ("gemma-4-26b", "gemma-27b")
]

base_path = "results"
all_comparison_data = []

for new_model, old_model in pairs:
    new_csv = os.path.join(base_path, new_model, "results.csv")
    old_csv = os.path.join(base_path, old_model, "results.csv")
    
    if os.path.exists(new_csv) and os.path.exists(old_csv):
        df_new = pd.read_csv(new_csv)
        df_old = pd.read_csv(old_csv)
        
        # Extract style
        df_new['style'] = df_new['config_label'].apply(lambda x: str(x).split(':')[-1] if ':' in str(x) else x)
        df_old['style'] = df_old['config_label'].apply(lambda x: str(x).split(':')[-1] if ':' in str(x) else x)
        
        # Group by combination
        new_combos = df_new.groupby(['agent', 'style'])['functional_correctness'].mean().reset_index()
        old_combos = df_old.groupby(['agent', 'style'])['functional_correctness'].mean().reset_index()
        
        # Merge to find intersection
        merged = pd.merge(new_combos, old_combos, on=['agent', 'style'], suffixes=('_new', '_old'))
        
        # Calculate diff
        merged['perc_change'] = ((merged['functional_correctness_new'] - merged['functional_correctness_old']) / merged['functional_correctness_old']) * 100
        merged['model_pair'] = f"{new_model} vs {old_model}"
        merged['combo'] = merged['agent'] + " + " + merged['style']
        
        all_comparison_data.append(merged)

if not all_comparison_data:
    print("No shared combinations found!")
    exit()

final_df = pd.concat(all_comparison_data, ignore_index=True)

# Plotting
plt.style.use('ggplot')

for pair in final_df['model_pair'].unique():
    subset = final_df[final_df['model_pair'] == pair].sort_values('perc_change', ascending=False)
    
    plt.figure(figsize=(14, 8))
    x = range(len(subset))
    width = 0.35
    
    plt.bar([i - width/2 for i in x], subset['functional_correctness_old'], width, label='Old Version', color='lightgray')
    plt.bar([i + width/2 for i in x], subset['functional_correctness_new'], width, label='New (Gemma-4)', color='dodgerblue')
    
    # Annotate with percentage change
    for i, (_, row) in enumerate(subset.iterrows()):
        change = row['perc_change']
        color = 'green' if change >= 0 else 'red'
        plt.text(i, max(row['functional_correctness_new'], row['functional_correctness_old']) + 0.01, 
                f"{change:+.1f}%", ha='center', va='bottom', fontsize=9, fontweight='bold', color=color)
    
    plt.xticks(x, subset['combo'], rotation=45, ha='right')
    plt.title(f'Combination Comparison: {pair}')
    plt.ylabel('Avg Functional Correctness')
    plt.legend()
    plt.tight_layout()
    
    filename = f"scratch/compare_{pair.replace(' ', '_')}.png"
    plt.savefig(filename)
    print(f"Saved {filename}")
    plt.close()

# Generate a summary table for the top improvements across all models
print("\nSummary of Shared Combinations Performance:")
summary = final_df[['model_pair', 'combo', 'functional_correctness_old', 'functional_correctness_new', 'perc_change']]
summary = summary.sort_values(['model_pair', 'perc_change'], ascending=[True, False])
print(summary.to_string(index=False))
