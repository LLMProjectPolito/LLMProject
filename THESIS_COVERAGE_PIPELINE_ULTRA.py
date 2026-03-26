import ast, os, sys, re, shutil, multiprocessing, pandas as pd, time
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor, as_completed

RESULTS_DIR    = Path("results")
BACKUP_DIR     = Path("results_backup")
OUTPUT_CSV     = Path("DATABASE_TESI_FINAL.csv")

# ──────────────────────────────────────────────
# CORE ANALYSIS ENGINE (Runs in child process)
# ──────────────────────────────────────────────

def count_ast_branches(code: str) -> int:
    try:
        tree = ast.parse(code)
        count = 0
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.ExceptHandler, ast.Try)):
                count += 2
            elif isinstance(node, ast.BoolOp):
                count += len(node.values)
        return count
    except: return 0

def extract_last_func(code: str, name: str) -> str:
    try:
        tree = ast.parse(code)
        defs = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name == name]
        if not defs: return ""
        lines = code.splitlines(keepends=True)
        return "".join(lines[defs[-1].lineno - 1 : defs[-1].end_lineno])
    except: return ""

def run_trace(code: str):
    hit = set()
    def tracer(f, e, a):
        if e == "line": hit.add(f.f_lineno)
        return tracer
    old = sys.gettrace()
    try:
        sys.settrace(tracer)
        ns = {"__name__": "__main__"}
        exec(compile(code, "<ag>", "exec"), ns)
        for n, f in list(ns.items()):
            if n.startswith("test_") and callable(f): f()
    except: pass
    finally: sys.settrace(old)
    return hit

def worker_analyze(py_path_str):
    p = Path(py_path_str)
    res = {"ast_branch": 0.0, "ast_line": 0.0, "br_pts": 0, "a_loc": 0, "div":0, "bloat":0.0, "dens":0.0}
    try:
        c = p.read_text(encoding="utf-8")
        tree = ast.parse(c)
        
        # Diversity (Asserts)
        res["div"] = len([n for n in ast.walk(tree) if isinstance(n, ast.Assert)])
        
        a_defs = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and not n.name.startswith("test_")]
        t_defs = [n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")]
        
        if not a_defs: return res
        
        l_def = a_defs[-1]
        res["a_loc"] = l_def.end_lineno - l_def.lineno
        t_loc = sum(n.end_lineno - n.lineno for n in t_defs)
        res["bloat"] = round(t_loc / res["a_loc"], 2) if res["a_loc"] > 0 else 0.0
        
        # Decision points
        br = 0
        for n in ast.walk(l_def):
            if isinstance(n, (ast.If, ast.While, ast.For, ast.BoolOp)): br += 1
        res["dens"] = round(br / res["a_loc"], 2) if res["a_loc"] > 0 else 0.0
        
        # Coverage
        res["br_pts"] = count_ast_branches(extract_last_func(c, a_defs[0].name))
        hit = run_trace(c)
        f_rows = set(range(l_def.lineno, l_def.end_lineno + 1))
        h_rows = hit & f_rows
        
        res["ast_line"] = round(len(h_rows) / len(f_rows), 4) if f_rows else 0.0
        res["ast_branch"] = round(min(1.0, len(h_rows) / max(res["br_pts"], 1)), 4)
    except: pass
    return res

# ──────────────────────────────────────────────
# MAIN PIPELINE
# ──────────────────────────────────────────────

if __name__ == "__main__":
    if not BACKUP_DIR.exists(): shutil.copytree(RESULTS_DIR, BACKUP_DIR)
    
    csvs = list(RESULTS_DIR.glob("gemma-*/results.csv"))
    main_df = pd.concat([pd.read_csv(p) for p in csvs], ignore_index=True)
    main_df = main_df.drop_duplicates(subset=["task_id", "config_label", "agent"], keep="last")
    
    # Pre-map paths
    paths = []
    for _, row in main_df.iterrows():
        m = row["config_label"].split(":")[0]; tid = row["task_id"].replace("/", "_")
        cand = RESULTS_DIR / m / "tests" / f"{tid}__{row['agent']}_{m}_{row['config_label'].split(':')[-1]}.py"
        if not cand.exists():
            glob = list((RESULTS_DIR / m / "tests").glob(f"{tid}__{row['agent']}_*.py"))
            cand = glob[0] if glob else None
        paths.append(str(cand) if cand else None)

    results = []
    print(f"🚀 UNLEASHING ULTRA-PIPELINE (4400 tasks)... 50 workers, 10s timeout.")
    
    with ProcessPoolExecutor(max_workers=multiprocessing.cpu_count()) as ex:
        futures = {ex.submit(worker_analyze, p): i for i, p in enumerate(paths) if p}
        done = 0
        for f in as_completed(futures):
            i = futures[f]
            try:
                m = f.result(timeout=10) # FAILSAFE
                results.append((i, m))
            except:
                results.append((i, {}))
            done += 1
            if done % 100 == 0: print(f"  ... {done}/{len(main_df)} COMPLETE")

    # Map back to DF
    res_dict = {i: m for i, m in results}
    cols_map = {
        "ast_branch_coverage": "ast_branch",
        "ast_line_coverage": "ast_line",
        "ast_total_branches": "br_pts",
        "ast_total_lines": "a_loc",
        "test_diversity_asserts": "div",
        "test_code_bloat_ratio": "bloat",
        "logic_density": "dens"
    }

    for target, internal in cols_map.items():
        main_df[target] = [res_dict.get(i, {}).get(internal, 0.0) for i in range(len(main_df))]

    # Final Efficiency with long names
    main_df["fc_per_1k_total_tokens"] = round((main_df["functional_correctness"] / main_df["total_tokens"]) * 1000, 4)
    main_df["coverage_per_1k_tokens"] = round((main_df["ast_branch_coverage"] / main_df["total_tokens"]) * 1000, 4)
    main_df = main_df.replace([float('inf')], 0.0).fillna(0.0)
    
    main_df.to_csv(OUTPUT_CSV, index=False)
    print(f"\n✅ VERDICT SAVED: {OUTPUT_CSV} (ROWS: {len(main_df)})")
