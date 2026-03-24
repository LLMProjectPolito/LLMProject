import pandas as pd, glob, os
from pathlib import Path

# CONFIGURAZIONE
results_dir = Path("results")
csv_paths = list(results_dir.glob("gemma-*/results.csv")) + [results_dir / "mixed/results.csv"]

print(f"Loading {len(csv_paths)} results databases...")

# MERGE TOTALE
dfs = []
for p in csv_paths:
    if p.exists():
        try:
            df = pd.read_csv(p)
            # Normalizziamo le etichette per non perdere dati nel merge
            if 'config_label' not in df.columns:
                 df['config_label'] = p.parent.name
            dfs.append(df)
        except Exception: pass

if not dfs:
    print("WARNING: No results found yet. Waiting for Tsunami...")
    exit()

master_df = pd.concat(dfs, ignore_index=True)

# AGGREGAZIONE FINALE (176 configurazioni)
# Aggreghiamo per config_label (es: gemma-27b:cot) e agent
final_matrix = master_df.groupby(['config_label', 'agent']).agg({
    'functional_correctness': 'mean',
    'branch_coverage': 'mean',
    'mutation_score': 'mean',
    'prompt_tokens': 'sum',
    'completion_tokens': 'sum',
    'total_tokens': 'sum'
}).reset_index()

# CALCOLO TOKEN MEDI
final_matrix['avg_tokens_per_task'] = final_matrix['total_tokens'] / master_df.groupby(['config_label', 'agent'])['task_id'].count().values

# SALVATAGGIO MD
md_content = "# ULTIMATE GEMMA EVOLUTION MATRIX (176 Configs)\n\n"
md_content += final_matrix.to_markdown(index=False)

with open("ULTIMATE_GEMMA_RESULTS.md", "w", encoding="utf-8") as f:
    f.write(md_content)

print(f"SUCCESS: Generated matrix with {len(final_matrix)} configurations.")
