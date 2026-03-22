import csv
import glob
from collections import defaultdict

def main():
    csv_files = glob.glob(r'results\turbo_start_139_n_*\results.csv')
    
    # Store the list of completed task_ids for each combination
    progress = defaultdict(list)
    
    for file in csv_files:
        with open(file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                combo = f"{row['agent']}:{row['config_label']}"
                # task_id format is "HumanEval/139" -> extract the number for easy sorting
                task_num = int(row['task_id'].split('/')[-1])
                if task_num not in progress[combo]:
                    progress[combo].append(task_num)
                    
    print("\n=== PROGRESSO DETTAGLIATO PER COMBINAZIONE ===")
    print(f"{'Combinazione (Agente:Modello:Stile)':<50} {'N_Completati':>12}  {'Problemi Finiti (HumanEval/...)'}")
    print("-" * 110)
    
    for combo, tasks in sorted(progress.items()):
        tasks.sort()
        # Formattiamo la lista di numeri (es. 139, 140, 141)
        tasks_str = ", ".join(map(str, tasks))
        print(f"{combo:<50} {len(tasks):>12}/25  [{tasks_str}]")

if __name__ == "__main__":
    main()
