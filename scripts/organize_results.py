
import os
import shutil
import json
import pandas as pd
import stat

RESULTS_DIR = "results"
OLD_DIR = os.path.join(RESULTS_DIR, "old")
os.makedirs(OLD_DIR, exist_ok=True)

# Define mapping for "useful" runs
KNOWLEDGE_MAPPING = {
    "run_20260314_210909": "benchmark_reasoning_styles_comparison",
    "run_20260314_195048": "agent_architecture_scrutiny_8b",
    "run_20260314_194413": "agent_architecture_initial_tests",
    "run_20260314_213000": "scaling_run_parallel_threads",
    "run_20260314_224557": "mini_models_qwen_performance_check",
    "run_20260315_114757": "modular_test_swarm_ac_prompts",
    "run_20260314_1826": "baseline_70b_gold_standard"
}

def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def clean_and_organize():
    run_folders = [f for f in os.listdir(RESULTS_DIR) if f.startswith("run_")]
    if not run_folders:
        print("No run folders found.")
        return

    # Preserving the 2 most recent runs to avoid interference with active experiments
    run_folders.sort()
    latest_runs = run_folders[-2:]
    others = run_folders[:-2]
    
    print(f"Preserving latest runs: {latest_runs}")
    
    for folder in others:
        folder_path = os.path.join(RESULTS_DIR, folder)
        csv_path = os.path.join(folder_path, "results.csv")
        
        # Determine if useless
        is_useless = False
        if not os.path.exists(csv_path):
            is_useless = True
        else:
            try:
                df = pd.read_csv(csv_path)
                if len(df) < 2:
                    is_useless = True
            except:
                is_useless = True
        
        # If the folder name is partially in our mapping, override useless
        mapped_name = None
        for key, val in KNOWLEDGE_MAPPING.items():
            if key in folder:
                mapped_name = val
                is_useless = False
                break
        
        if is_useless:
            print(f"Deleting useless run: {folder}")
            try:
                shutil.rmtree(folder_path, onerror=remove_readonly)
            except Exception as e:
                print(f"Could not delete {folder}: {e}")
            continue

        # Move to old
        if not mapped_name:
            mapped_name = f"{folder}_general_trial"
        
        dest_path = os.path.join(OLD_DIR, mapped_name)
        # Avoid overwriting if multiple folders match a key (unlikely but safe)
        if os.path.exists(dest_path):
            dest_path = os.path.join(OLD_DIR, f"{mapped_name}_{folder}")
            
        print(f"Moving {folder} -> old/{os.path.basename(dest_path)}")
        try:
            shutil.move(folder_path, dest_path)
        except Exception as e:
            print(f"Could not move {folder}: {e}")

if __name__ == "__main__":
    clean_and_organize()
