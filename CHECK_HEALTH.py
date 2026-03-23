import os, glob
from pathlib import Path

# Configurazione
results_dir = Path("results")
py_files = list(results_dir.glob("gemma-*/tests/*.py"))

print(f"Checking {len(py_files)} files for API Errors...")

failed_count = 0
for f in py_files:
    try:
        if not f.exists(): continue
        content = f.read_text(encoding="utf-8")
        if "No API key was provided" in content or "ERROR:" in content or "ModuleNotFoundError" in content:
            failed_count += 1
            f.unlink()
    except Exception: pass

print(f"\nTOTAL_FAILED_FILES_DELETED: {failed_count}")
print(f"HEALTHY_FILES_REMAINING: {len(py_files) - failed_count}")

if failed_count > 0:
    print("WARNING: Many files had API Errors. Ensure GOOGLE_API_KEY is set in GitHub Secrets!")
else:
    print("SUCCESS: All files appear healthy and complete.")
