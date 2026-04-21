import csv
from pathlib import Path

def deduplicate_csv(file_path):
    with open(file_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)
    
    seen = set()
    unique_rows = []
    
    for row in rows:
        # Use a tuple of (task_id, agent, config_label) as unique key
        key = (row.get('task_id'), row.get('agent'), row.get('config_label'))
        if key not in seen:
            seen.add(key)
            unique_rows.append(row)
    
    if len(unique_rows) < len(rows):
        print(f"Deduplicating {file_path}: {len(rows)} -> {len(unique_rows)}")
        # Backup the original
        backup_path = file_path.with_suffix('.csv.dup_backup')
        if not backup_path.exists():
            import shutil
            shutil.copy2(file_path, backup_path)
            
        with open(file_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(unique_rows)
    else:
        print(f"No duplicates in {file_path}")

def main():
    results_dir = Path('results')
    for csv_file in results_dir.rglob('results.csv'):
        deduplicate_csv(csv_file)

if __name__ == '__main__':
    main()
