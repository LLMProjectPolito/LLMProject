import os, re, subprocess
from pathlib import Path

# FILE ORIGINALE (Gemma-4b Atomic Swarm)
SRC_RAW = Path("results/DEBUG_SAMPLE.py").read_text(encoding="utf-8")

# SEPARAZIONE LOGICA vs TEST
# Sappiamo che HumanEval ha 'def function_name(args):'
# Cerchiamo la seconda occorrenza (quella dell'agente)
lines = SRC_RAW.splitlines()
func_def_indices = [i for i, l in enumerate(lines) if l.strip().startswith("def ") and "(" in l and "):" in l]

if len(func_def_indices) >= 2:
    # La parte dell'agente inizia all'indice della seconda funzione 'def'
    logic_start = func_def_indices[1]
    
    # Ma prima cerchiamo dove iniziano i test
    test_start = next((i for i, l in enumerate(lines) if l.strip().startswith("def test_")), len(lines))
    
    logic_code = "\n".join(lines[logic_start:test_start])
    test_code = "from agent_logic import *\n\nimport pytest\n" + "\n".join(lines[test_start:])
    
    # SCRITTURA FILE TEMPORANEI (Isolated)
    Path("agent_logic.py").write_text(logic_code, encoding="utf-8")
    Path("test_logic.py").write_text(test_code, encoding="utf-8")
    
    print("\n--- METODO 1: SEPARAZIONE NUCLEARE (Pytest + Cov) ---")
    res = subprocess.run(
        ["python", "-m", "pytest", "test_logic.py", "--cov=agent_logic", "--cov-branch", "--cov-report=term-missing"],
        capture_output=True, text=True
    )
    print(res.stdout)
    print(res.stderr)
else:
    print("ERRORE: Impossibile separare logica e test dal file.")
