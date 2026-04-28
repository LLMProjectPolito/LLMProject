import pandas as pd
import matplotlib.pyplot as plt
import os

# Define the models to compare
models = ["gemma-12b", "gemma-4-26b", "gemma-27b", "gemma-31b"]
base_path = "results"

efficiency_data = []

for model in models:
    csv_path = os.path.join(base_path, model, "results.csv")
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        
        # Calculate averages
        avg_correctness = df['functional_correctness'].mean()
        avg_total_tokens = df['total_tokens'].mean()
        avg_prompt_tokens = df['prompt_tokens'].mean()
        avg_completion_tokens = df['completion_tokens'].mean()
        
        # Efficiency Metric: Correctness per 1000 total tokens
        # Higher is better
        efficiency = (avg_correctness / avg_total_tokens) * 1000 if avg_total_tokens > 0 else 0
        
        efficiency_data.append({
            "Model": model,
            "Avg Correctness": avg_correctness,
            "Avg Total Tokens": avg_total_tokens,
            "Avg Prompt Tokens": avg_prompt_tokens,
            "Avg Completion Tokens": avg_completion_tokens,
            "Efficiency (Score/1k Tokens)": efficiency
        })

if not efficiency_data:
    print("No data found for the specified models!")
    exit()

eff_df = pd.DataFrame(efficiency_data)

# Plotting
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax1 = plt.subplots(figsize=(12, 7))

# Bar chart for Total Tokens (Primary Y-axis)
color_tokens = '#1B3A5C'
ax1.set_xlabel('Model')
ax1.set_ylabel('Avg Total Tokens', color=color_tokens)
bars = ax1.bar(eff_df['Model'], eff_df['Avg Total Tokens'], color=color_tokens, alpha=0.6, label='Avg Total Tokens')
ax1.tick_params(axis='y', labelcolor=color_tokens)

# Line chart for Efficiency Score (Secondary Y-axis)
ax2 = ax1.twinx()
color_eff = '#D4731A'
ax2.set_ylabel('Efficiency (Score per 1k Tokens)', color=color_eff)
ax2.plot(eff_df['Model'], eff_df['Efficiency (Score/1k Tokens)'], color=color_eff, marker='o', linewidth=2, label='Efficiency Score')
ax2.tick_params(axis='y', labelcolor=color_eff)

plt.title('Token Efficiency Comparison: Gemma-12b, 4-26b, 27b, 31b')
fig.tight_layout()

# Add labels on bars
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 10,
            f'{int(height)}', ha='center', va='bottom', fontsize=10)

plt.savefig('scratch/token_efficiency.png', dpi=150, facecolor='white')
print("\n" + "="*60)
print("TOKEN EFFICIENCY ANALYSIS (Correctness per 1k Tokens)")
print("="*60)

sorted_eff = eff_df.sort_values("Efficiency (Score/1k Tokens)", ascending=False)

for i, row in sorted_eff.iterrows():
    print(f"Model: {row['Model']:<15} | Efficiency: {row['Efficiency (Score/1k Tokens)']:.<8.4f} | Avg Tokens: {row['Avg Total Tokens']:>6.0f}")

# Compare best vs worst efficiency
best_model = sorted_eff.iloc[0]
worst_model = sorted_eff.iloc[-1]
ratio = best_model['Efficiency (Score/1k Tokens)'] / worst_model['Efficiency (Score/1k Tokens)']

print(f"\nKey Finding: {best_model['Model']} is {ratio:.1f}x more efficient than {worst_model['Model']}.")
print(f"Gemma-4-26b uses ~{row['Avg Total Tokens']/sorted_eff[sorted_eff['Model']=='gemma-27b']['Avg Total Tokens'].values[0]:.1f}x more tokens than Gemma-27b.")

print("\n" + "="*60)
print("Analysis complete. Chart saved as scratch/03_token_efficiency/token_efficiency.png")
