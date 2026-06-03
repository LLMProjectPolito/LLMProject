import os
import pandas as pd

def fix_mutation_scores():
    results_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "results"))
    print(f"Scanning results directory: {results_dir}")
    
    for model in os.listdir(results_dir):
        model_path = os.path.join(results_dir, model)
        if os.path.isdir(model_path):
            csv_path = os.path.join(model_path, 'results.csv')
            if os.path.exists(csv_path):
                try:
                    df = pd.read_csv(csv_path)
                    if 'mutation_score' in df.columns and 'functional_correctness' in df.columns:
                        before = df['mutation_score'].mean()
                        # Apply correction: if code is not 100% correct, mutation score must be 0.0
                        df.loc[df['functional_correctness'] < 1.0, 'mutation_score'] = 0.0
                        after = df['mutation_score'].mean()
                        
                        if before != after:
                            print(f"Updated {model}: Mean mutation score changed from {before:.4f} to {after:.4f}")
                            df.to_csv(csv_path, index=False)
                        else:
                            print(f"Skipped {model}: No changes needed (already correct).")
                except Exception as e:
                    print(f"Error updating {model}: {e}")

if __name__ == "__main__":
    fix_mutation_scores()
