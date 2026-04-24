import pandas as pd
import matplotlib.pyplot as plt
import os
import seaborn as sns

# Define all 8 models
models = [
    "gemma-1b", "gemma-4b", "gemma-12b", "gemma-27b", "gemma-31b",
    "gemma-4-2b", "gemma-4-4b", "gemma-4-26b"
]
base_path = "results"

best_results = []

for model in models:
    csv_path = os.path.join(base_path, model, "results.csv")
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        
        # Extract style
        df['style'] = df['config_label'].apply(lambda x: str(x).split(':')[-1] if ':' in str(x) else x)
        
        # Group by combination to find the best one
        # Best = highest functional_correctness
        combos = df.groupby(['agent', 'style']).agg({
            'functional_correctness': 'mean',
            'line_coverage': 'mean',
            'total_tokens': 'mean',
            'maintainability_mi': 'mean',
            'bloat_ratio': 'mean'
        }).reset_index()
        
        # Find the best combination
        best_combo_row = combos.loc[combos['functional_correctness'].idxmax()]
        
        # Calculate efficiency for this best combo
        efficiency = (best_combo_row['functional_correctness'] / best_combo_row['total_tokens']) * 1000 if best_combo_row['total_tokens'] > 0 else 0
        
        best_results.append({
            "Model": model,
            "Best Combo": f"{best_combo_row['agent']} + {best_combo_row['style']}",
            "Correctness": best_combo_row['functional_correctness'],
            "Coverage": best_combo_row['line_coverage'],
            "Efficiency (1k)": efficiency,
            "Maintainability": best_combo_row['maintainability_mi'],
            "Bloat Ratio": best_combo_row['bloat_ratio'],
            "Avg Tokens": best_combo_row['total_tokens']
        })

if not best_results:
    print("No data found!")
    exit()

best_df = pd.DataFrame(best_results)

# Create a combined comparison plot
plt.style.use('ggplot')
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# 1. Functional Correctness
sns.barplot(x='Model', y='Correctness', data=best_df, ax=axes[0, 0], palette='viridis')
axes[0, 0].set_title('Best Case: Functional Correctness')
axes[0, 0].set_ylim(0, 1.05)

# 2. Line Coverage
sns.barplot(x='Model', y='Coverage', data=best_df, ax=axes[0, 1], palette='magma')
axes[0, 1].set_title('Best Case: Line Coverage')
axes[0, 1].set_ylim(0, 105)

# 3. Token Efficiency
sns.barplot(x='Model', y='Efficiency (1k)', data=best_df, ax=axes[1, 0], palette='rocket')
axes[1, 0].set_title('Best Case: Token Efficiency (Score/1k tokens)')

# 4. Maintainability Index
sns.barplot(x='Model', y='Maintainability', data=best_df, ax=axes[1, 1], palette='cubehelix')
axes[1, 1].set_title('Best Case: Maintainability Index')

for ax in axes.flat:
    ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('scratch/best_case_comparison.png')
print("Best-case analysis complete. Chart saved as scratch/best_case_comparison.png")

# Print detailed summary
print("\nBest Combination Comparison for each Model:")
print(best_df[["Model", "Best Combo", "Correctness", "Coverage", "Efficiency (1k)", "Avg Tokens"]].sort_values("Correctness", ascending=False).to_string(index=False))
