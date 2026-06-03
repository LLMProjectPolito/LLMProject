import os
import pandas as pd
import json
from pathlib import Path
from src.utils.executor import run_tests

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    results_dir = os.path.abspath(os.path.join(base_dir, "..", "..", "results"))
    data_dir = os.path.abspath(os.path.join(base_dir, "..", "..", "data", "evalplus_subset"))
    
    print(f"Results Directory: {results_dir}")
    print(f"Data Directory: {data_dir}")
    
    # Pre-load all tasks to map task_id to prompt and canonical_solution
    task_cache = {}
    for f in os.listdir(data_dir):
        if f.endswith('.json'):
            path = os.path.join(data_dir, f)
            with open(path, 'r', encoding='utf-8') as json_file:
                prob = json.load(json_file)
                task_cache[prob['task_id']] = prob
                
    for model in os.listdir(results_dir):
        model_path = os.path.join(results_dir, model)
        if not os.path.isdir(model_path):
            continue
            
        csv_path = os.path.join(model_path, 'results.csv')
        if not os.path.exists(csv_path):
            continue
            
        print(f"\nProcessing model: {model}")
        try:
            df = pd.read_csv(csv_path)
        except Exception as e:
            print(f"Error reading CSV for {model}: {e}")
            continue
            
        updated_rows = []
        changes_count = 0
        
        for idx, row in df.iterrows():
            task_id = row['task_id']
            agent = row['agent']
            config_label = row['config_label']
            
            # Apply post-hoc mutation score correction unconditionally
            if row['functional_correctness'] < 1.0 and row['mutation_score'] != 0.0:
                row['mutation_score'] = 0.0
                changes_count += 1

            # Find the generated file
            safe_task = task_id.replace("/", "_")
            prompt_style = config_label.split(':')[-1] if isinstance(config_label, str) and ':' in config_label else str(config_label)
            agent_full = f"{agent}:{model}:{prompt_style}"
            safe_agent = agent_full.replace(":", "_")
            
            filename = f"{safe_task}__{safe_agent}.py"
            test_file_path = os.path.join(model_path, 'tests', filename)
            
            # Fallback check if file exists
            if not os.path.exists(test_file_path):
                tests_dir = os.path.join(model_path, 'tests')
                found = False
                if os.path.exists(tests_dir):
                    prefix = f"{safe_task}__{agent}_"
                    for f_name in os.listdir(tests_dir):
                        if f_name.startswith(prefix) and f_name.endswith('.py'):
                            test_file_path = os.path.join(tests_dir, f_name)
                            found = True
                            break
                if not found:
                    updated_rows.append(row)
                    continue
            
            # If we found the file, let's load it and run only if it contains dummy imports
            if task_id in task_cache:
                prob = task_cache[task_id]
                prompt = prob['prompt']
                canonical_solution = prob['canonical_solution']
                source_code = prompt + canonical_solution
                
                try:
                    with open(test_file_path, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                        
                    # Check if file actually contains dummy module placeholders
                    dummies = ['your_module', 'my_module', 'some_module', 'module_name', 'your_file', 'your_code']
                    if any(dummy in file_content for dummy in dummies):
                        # Extract test_code by skipping the prompt
                        if file_content.startswith(prompt):
                            test_code = file_content[len(prompt):].strip()
                        else:
                            test_code = file_content.strip()
                            
                        # Run tests (it will use the updated _ensure_only_code)
                        res = run_tests(source_code, test_code)
                        
                        # Post-hoc correction logic: if correctness < 1.0, mutation score must be 0.0
                        if res['functional_correctness'] < 1.0:
                            res['mutation_score'] = 0.0
                        
                        # Check if the metrics changed
                        changed = False
                        fields_to_check = ['passed', 'failed', 'errors', 'total', 'functional_correctness', 'line_coverage', 'mutation_score']
                        for field in fields_to_check:
                            orig = row[field]
                            new_val = res[field]
                            if pd.isna(orig) and new_val is None:
                                continue
                            if orig != new_val:
                                if isinstance(orig, float) and isinstance(new_val, float) and abs(orig - new_val) < 1e-4:
                                    continue
                                changed = True
                                
                        if changed:
                            changes_count += 1
                            for k, v in res.items():
                                if k in df.columns:
                                    row[k] = v
                                    
                except Exception as e:
                    print(f"Error processing test file {test_file_path}: {e}")
            
            updated_rows.append(row)
            
        # Save back to CSV if there were changes
        if changes_count > 0:
            print(f"  Applied {changes_count} changes to {model}'s results.")
            updated_df = pd.DataFrame(updated_rows)
            # Preserve original column order
            updated_df = updated_df[df.columns]
            updated_df.to_csv(csv_path, index=False)
        else:
            print(f"  No changes needed for {model}.")

if __name__ == '__main__':
    main()
