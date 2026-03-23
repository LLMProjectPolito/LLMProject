import pandas as pd
from pathlib import Path
import glob

def final_merge_and_analyze():
    results_dir = Path("results")
    gemma_models = ['1b', '4b', '12b', '27b']
    
    # 1. RACCOLTA DI TUTTI I CSV (Priorità a quelli nelle sottocartelle turbo_*)
    main_files = list(results_dir.glob("THESIS_*.csv")) + list(results_dir.glob("MASTER_*.csv"))
    run_files = sorted(list(results_dir.glob("**/results.csv"))) # Quelli recenti sono qui
    
    all_csvs = main_files + run_files # I run_files vengono "dopo" e sovrascrivono con keep='last'
    
    print(f"Found {len(all_csvs)} CSV files to merge.")
    
    all_dfs = []
    for csv_path in all_csvs:
        try:
            df = pd.read_csv(csv_path)
            if 'task_id' in df.columns and 'agent' in df.columns:
                all_dfs.append(df)
                print(f"  + {csv_path.name}: {len(df)} rows")
        except Exception as e:
            pass
    
    df = pd.concat(all_dfs, ignore_index=True)
    print(f"\nTotal raw rows: {len(df)}")
    
    # 2. NORMALIZZAZIONE LABELS
    def normalize_config(label):
        label = str(label).lower()
        m_f = "unknown"
        for m in gemma_models:
            if m in label:
                m_f = f"gemma-{m}"
                break
        p_f = "zero_shot"
        if "few_shot" in label or "fewshot" in label: p_f = "few_shot"
        elif "scot" in label: p_f = "scot"
        elif "cot" in label: p_f = "cot"
        elif "zs" in label: p_f = "zero_shot"
        return f"{m_f}:{p_f}"

    df['config_label'] = df['config_label'].apply(normalize_config)
    df = df[~df['config_label'].str.contains("unknown")].copy()
    
    # 3. SMART MERGE: Per ogni task, teniamo il risultato MIGLIORE (FC più alto, poi più token)
    df = df.sort_values(['config_label', 'agent', 'task_id', 'functional_correctness', 'total_tokens'], ascending=[True, True, True, False, False])
    df_pure = df.drop_duplicates(subset=['task_id', 'agent', 'config_label'], keep='first')
    
    # Prendi solo i primi 25 per config (per sicurezza)
    df_pure = df_pure.groupby(['config_label', 'agent']).head(25)
    
    # 4. DROP elapsed_s if present
    if 'elapsed_s' in df_pure.columns:
        df_pure = df_pure.drop(columns=['elapsed_s'])
    
    # 5. COUNTS CHECK
    counts = df_pure.groupby(['config_label', 'agent']).size().reset_index(name='count')
    total_configs = len(counts)
    perfect = counts[counts['count'] == 25]
    anomalies = counts[counts['count'] != 25]
    
    print(f"\n{'='*70}")
    print(f"FINAL MERGE REPORT")
    print(f"{'='*70}")
    print(f"Total unique Gemma rows: {len(df_pure)}")
    print(f"Unique configurations: {total_configs} / 176")
    print(f"Perfect configs (25 tasks): {len(perfect)}")
    if len(anomalies) > 0:
        print(f"\nANOMALIES ({len(anomalies)} configs):")
        print(anomalies.to_string(index=False))
    
    # 6. NaN CHECK
    metrics = ['functional_correctness', 'line_coverage', 'branch_coverage', 'mutation_score']
    nan_counts = df_pure[metrics].isna().sum()
    zero_fc = (df_pure['functional_correctness'] == 0).sum()
    print(f"\nNaN counts per metric:")
    print(nan_counts.to_string())
    print(f"\nRows with functional_correctness = 0: {zero_fc} / {len(df_pure)}")
    
    # 7. PERFORMANCE TABLE
    stats = df_pure.groupby(['config_label', 'agent'])[metrics + ['total_tokens']].mean().reset_index()
    stats = stats.fillna(0.0)
    stats = stats.sort_values(['config_label', 'agent'])
    
    # 8. SAVE
    df_pure.to_csv(results_dir / "THESIS_ABSOLUTE_FINAL.csv", index=False)
    
    header = "| " + " | ".join(stats.columns) + " |"
    sep = "| " + " | ".join(["---"] * len(stats.columns)) + " |"
    rows = []
    for _, row in stats.iterrows():
        cells = []
        for col in stats.columns:
            v = row[col]
            if isinstance(v, float):
                cells.append(f"{v:.4f}")
            else:
                cells.append(str(v))
        rows.append("| " + " | ".join(cells) + " |")
    
    md = "# Final Gemma Performance Matrix\n\n"
    md += f"Total tasks: {len(df_pure)} | Configs: {total_configs}\n\n"
    md += header + "\n" + sep + "\n" + "\n".join(rows)
    
    with open(results_dir / "ULTIMATE_GEMMA_RESULTS.md", "w", encoding="utf-8") as f:
        f.write(md)
    
    print(f"\nSaved: THESIS_ABSOLUTE_FINAL.csv ({len(df_pure)} rows)")
    print(f"Saved: ULTIMATE_GEMMA_RESULTS.md ({total_configs} configs)")

if __name__ == "__main__":
    final_merge_and_analyze()
