import argparse, re, csv, json, time, concurrent.futures, threading
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

_csv_lock = threading.Lock()

from src.utils.model_registry import get_model, get_token_usage, reset_token_usage

DATA_DIR    = Path("data/evalplus_subset")
RESULTS_DIR = Path("results")

CSV_FIELDS = [
    "task_id", "agent", "config_label",
    "passed", "failed", "errors", "total",
    "functional_correctness", "line_coverage", "branch_coverage", "mutation_score",
    "complexity_cc", "maintainability_mi", "bloat_ratio", "similarity_score",
    "elapsed_s",
    "prompt_tokens", "completion_tokens", "total_tokens",
]

ALL_AGENTS = [
    "baseline", "actor_critic", "adversarial",
    "competitive", "hybrid", "coa", "soa", "swarm", "consensus",
    "self_healing", "atomic_swarm", "few_shot", "cot", "scot"
]

def safe_invoke(agent_fn, prompt, overrides, timeout=180, max_retries=3):
    usage_stats = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0, "execution_time": 0.0}
    start_t = time.time()
    for attempt in range(max_retries):
        try:
            # print(f"   [DEBUG] Calling {agent_fn.__name__} for {overrides.get('_label')}", flush=True)
            reset_token_usage()
            test_code = agent_fn(prompt, overrides)
            usage = get_token_usage()
            return test_code, {
                "prompt_tokens": usage["prompt_tokens"],
                "completion_tokens": usage["completion_tokens"],
                "total_tokens": usage["total_tokens"],
                "execution_time": round(time.time() - start_t, 2)
            }
        except Exception as e:
            err_str = str(e).lower()
            if ("429" in err_str or "rate limit" in err_str) and attempt < max_retries - 1:
                wait_time = (attempt + 1) * 20
                time.sleep(wait_time); continue
            return f"# ERROR: {e}", usage_stats
    return "", usage_stats

# Global Agent wrappers with Lazy Imports
def run_baseline(p, o={}): 
    from src.agents.baseline import setup_baseline_graph
    return setup_baseline_graph(model=o.get("model"), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p})["test_code"]

def run_actor_critic(p, o={}): 
    from src.agents.actor_critic import setup_actor_critic_graph
    return setup_actor_critic_graph(driver_model=o.get("model"), navigator_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "test_code": "", "feedback": "", "iterations": 0})["test_code"]

def run_adversarial(p, o={}): 
    from src.agents.adversarial import setup_adversarial_graph
    return setup_adversarial_graph(tester_model=o.get("model"), hacker_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "source_code": p, "test_code": "", "mutated_code": "", "mutation_caught": False})["test_code"]

def run_competitive(p, o={}): 
    from src.agents.competitive import setup_competitive_graph
    model = o.get("model", "gemma-12b")
    result = setup_competitive_graph(models=[model]).invoke({"problem": p, "generated_tests": {}, "winner": ""})
    winner = result["winner"]
    return result["generated_tests"].get(winner, "")

def run_hybrid(p, o={}): 
    from src.agents.hybrid import setup_hybrid_graph
    return setup_hybrid_graph(generate_model=o.get("model"), evolve_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "population": [], "best_test": ""})["best_test"]

def run_coa(p, o={}): 
    from src.agents.coa import setup_coa_graph
    return setup_coa_graph(manager_model=o.get("model"), worker_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "segments": [], "test_code": ""})["test_code"]

def run_soa(p, o={}): 
    from src.agents.soa import setup_soa_graph
    return setup_soa_graph(orchestrator_model=o.get("model"), specialist_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "expertise": "", "test_code": ""})["test_code"]

def run_swarm(p, o={}): 
    from src.agents.swarm import setup_swarm_graph
    return setup_swarm_graph(n=o.get("n", 3), worker_model=o.get("model"), aggregator_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "results": [], "final_suite": ""})["final_suite"]

def run_consensus(p, o={}): 
    from src.agents.consensus import setup_consensus_graph
    return setup_consensus_graph(generation_model=o.get("model"), debate_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "proposals": [], "final_test": ""})["final_test"]

def run_self_healing(p, o={}): 
    from src.agents.self_healing import setup_self_healing_graph
    return setup_self_healing_graph(model=o.get("model"), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "test_code": "", "error_message": "", "iteration": 0}).get("test_code", "")

def run_atomic_swarm(p, o={}):
    from src.agents.atomic_swarm import setup_atomic_swarm_graph
    return setup_atomic_swarm_graph(model=o.get("model"), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "test_cases": [], "final_suite": ""}).get("final_suite", "")

def run_few_shot(p, o={}): return run_baseline(p, {**o, "reasoning_style": "few_shot"})
def run_cot(p, o={}):      return run_baseline(p, {**o, "reasoning_style": "cot"})
def run_scot(p, o={}):     return run_baseline(p, {**o, "reasoning_style": "scot"})

AGENT_FNS = {
    "baseline": run_baseline, "actor_critic": run_actor_critic, "adversarial": run_adversarial,
    "competitive": run_competitive, "hybrid": run_hybrid, "coa": run_coa, "soa": run_soa,
    "swarm": run_swarm, "consensus": run_consensus, "self_healing": run_self_healing,
    "atomic_swarm": run_atomic_swarm, "few_shot": run_few_shot, "cot": run_cot, "scot": run_scot
}

def make_run_dir():
    import sys
    args_str = "_".join(sys.argv[1:4]).replace("--", "").replace(":", "_")
    safe_name = re.sub(r'[^a-zA-Z0-9_-]', '', args_str)[:50]
    ts = datetime.now().strftime("%H%M%S")
    d = RESULTS_DIR / f"turbo_{safe_name}_{ts}"
    d.mkdir(parents=True, exist_ok=True); (d/"tests").mkdir(exist_ok=True); return d

def save_test_file(run_dir, task_id, agent, test_code, original_prompt=""):
    safe_task = task_id.replace("/", "_")
    safe_agent = agent.replace(":", "_").replace("/", "_")
    
    # ASSICURIAMO L'INTEGRITÀ DEL CODICE: Prompt + Completamento
    # Se il test_code non contiene già la firma, la aggiungiamo dal prompt
    full_code = original_prompt + "\n" + test_code
    
    (run_dir / "tests" / f"{safe_task}__{safe_agent}.py").write_text(full_code, encoding="utf-8")

def save_csv(run_dir, rows):
    path = run_dir / "results.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS); writer.writeheader(); writer.writerows(rows)
    return path

def load_problems(n, start=0):
    files = sorted(DATA_DIR.glob("*.json"), key=lambda x: int(re.search(r"(\d+)", x.name).group(1)) if re.search(r"(\d+)", x.name) else 0)[start:start+n]
    return [json.loads(f.read_text(encoding="utf-8")) for f in files]

_csv_lock = threading.Lock()

def _warmup_imports():
    """Pre-import all agent modules in the main thread to avoid GIL import-lock deadlock with many workers."""
    print(">>> Warming up agent imports...", flush=True)
    from src.agents.baseline import setup_baseline_graph
    from src.agents.actor_critic import setup_actor_critic_graph
    from src.agents.adversarial import setup_adversarial_graph
    from src.agents.competitive import setup_competitive_graph
    from src.agents.hybrid import setup_hybrid_graph
    from src.agents.coa import setup_coa_graph
    from src.agents.soa import setup_soa_graph
    from src.agents.swarm import setup_swarm_graph
    from src.agents.consensus import setup_consensus_graph
    from src.agents.self_healing import setup_self_healing_graph
    from src.agents.atomic_swarm import setup_atomic_swarm_graph
    from src.utils.executor import run_tests
    print(">>> Warmup complete. Launching workers...", flush=True)

def load_completed(resume_csv: str) -> set:
    """Load already-completed (task_id, agent_name) pairs from an existing CSV."""
    if not resume_csv or not Path(resume_csv).exists():
        return set()
    done = set()
    with open(resume_csv, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            # agent_name in the CSV is base_agent, config_label is model:style
            # We need to reconstruct the full agent_name key used in overrides
            # Key format: agent:model:style -> stored as config_label=model:style, agent=base_agent
            label = row.get("config_label", "")
            base  = row.get("agent", "")
            tid   = row.get("task_id", "")
            # Normalize legacy labels: if it's just a model name, it implies zero_shot
            if ":" not in label and label:
                label = f"{label}:zero_shot"
            full_key = f"{base}:{label}"
            done.add((tid, full_key))
    print(f">>> Resume: found {len(done)} completed (task_id, agent) pairs to skip.", flush=True)
    return done

def run_experiment(agents, n, overrides={}, start=0, workers=100, resume_csv=None):
    _warmup_imports()
    from src.utils.executor import run_tests
    completed = load_completed(resume_csv)
    start_ts = datetime.now().isoformat(); run_dir = make_run_dir(); problems = load_problems(n, start)
    print(f"Run dir: {run_dir}\nTasks: {len(problems) * len(agents)}\nWorkers: {workers}\n", flush=True)
    rows = []

    def run_task_for_agent(prob, agent_name):
        task_id = prob["task_id"]; source = prob["prompt"] + prob["canonical_solution"]
        base_agent = agent_name.split(":")[0]; agent_overrides = overrides.get(agent_name, {})
        try:
            test_code, usage = safe_invoke(AGENT_FNS[base_agent], prob["prompt"], agent_overrides)
            # PERCORSO FISSO PER LA TESI: results/gemma-Xb/tests/
            model_slug = agent_overrides.get("model", "default")
            target_tests_dir = RESULTS_DIR / model_slug / "tests"
            target_tests_dir.mkdir(parents=True, exist_ok=True)
            target_csv = RESULTS_DIR / model_slug / "results.csv"

            save_test_file(target_tests_dir.parent, task_id, agent_name, test_code, original_prompt=prob["prompt"])
            metrics = run_tests(source, test_code)
            res = {
                "task_id": task_id, "agent": base_agent, "config_label": agent_overrides.get("_label", "default"),
                "passed": metrics["passed"], "failed": metrics["failed"], "errors": metrics["errors"],
                "total": metrics["total"], "functional_correctness": metrics["functional_correctness"],
                "line_coverage": metrics["line_coverage"], "branch_coverage": metrics["branch_coverage"],
                "mutation_score": metrics.get("mutation_score", 0), "complexity_cc": metrics["complexity_cc"],
                "maintainability_mi": metrics["maintainability_mi"], "bloat_ratio": metrics["bloat_ratio"],
                "similarity_score": metrics["similarity_score"],
                "prompt_tokens": usage["prompt_tokens"], "completion_tokens": usage["completion_tokens"], "total_tokens": usage["total_tokens"]
            }
            with _csv_lock:
                # SALVATAGGIO INCREMENTALE NEL CSV DEL MODELLO
                pd.DataFrame([res]).to_csv(target_csv, mode='a', index=False, header=not target_csv.exists())
                rows.append(res)
                print(f"   [DONE] {task_id} x {agent_name} ({len(rows)}/{len(problems)*len(agents)})", flush=True)
            return res
        except Exception as e:
            print(f"   [FATAL] {agent_name} on {task_id}: {e}", flush=True); return None

    # FLATTEN THE WHOLE MATRIX INTO ONE LIST OF TASKS, skipping already completed
    all_tasks = [(p, a) for p in problems for a in agents
                 if (p["task_id"], a) not in completed]
                 
    # SMART PRIORITY SORTING: Fast agents first, slow multi-turn agents last
    def agent_priority(agent_name):
        if "baseline" in agent_name: return 0
        if "adversarial" in agent_name or "self_healing" in agent_name: return 1
        if any(slow in agent_name for slow in ["swarm", "consensus", "coa", "actor_critic", "hybrid"]): return 3
        return 2

    # Sort tasks by agent priority, then by task_id
    all_tasks.sort(key=lambda x: (agent_priority(x[1]), x[0]["task_id"]))

    skipped = len(problems) * len(agents) - len(all_tasks)
    if skipped: print(f">>> Skipping {skipped} already-completed tasks.", flush=True)
    print(f">>> Running {len(all_tasks)} remaining tasks with {workers} workers.", flush=True)

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        for p, a in all_tasks:
            executor.submit(run_task_for_agent, p, a)
        
    print(f"\n✅ FULL TURBO COMPLETE. CSV -> {run_dir}/results.csv")

def main():
    print(">>> TURBO EXPERIMENT RUNNER BOOTING <<<", flush=True)
    parser = argparse.ArgumentParser()
    parser.add_argument("--agents", nargs="+", default=["all"])
    parser.add_argument("--n", type=int, default=20)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--workers", type=int, default=100)
    parser.add_argument("--overrides", type=str, default="")
    parser.add_argument("--resume", type=str, default=None, help="Path to existing results.csv to resume from")
    args = parser.parse_args()
    
    if "tsunami" in args.agents:
        models = ['gemma-1b', 'gemma-4b', 'gemma-12b', 'gemma-27b']
        prompts = ['zero_shot', 'cot', 'scot', 'few_shot']
        agents = ['baseline', 'actor_critic', 'adversarial', 'competitive', 'hybrid', 'coa', 'soa', 'swarm', 'consensus', 'self_healing', 'atomic_swarm']
        requested = [f"{a}:{m}:{p}" for m in models for p in prompts for a in agents]
    elif "all" in args.agents:
        requested = ALL_AGENTS
    else:
        requested = args.agents
    over_map = {}
    for part in args.overrides.split(","):
        if "=" in part and ":" in part:
            a_f, kv = part.rsplit(":", 1); k, v = kv.split("=", 1)
            if a_f not in over_map: over_map[a_f] = {}
            over_map[a_f][k] = int(v) if v.isdigit() else v

    final_agents = []; final_overs = {}
    for entry in requested:
        parts = entry.split(":")
        model_str = "default"; style = "zero_shot"
        if len(parts) >= 2:
            agent_type = parts[0]; model_str = parts[1]
            style = parts[2] if len(parts) == 3 else "zero_shot"
            if "/" in model_str:
                m1, m2 = model_str.split("/", 1)
                final_overs[entry] = {"reasoning_style": style, "model": m1, "model2": m2}
            else:
                final_overs[entry] = {"reasoning_style": style, "model": model_str}
        else:
            final_overs[entry] = {"reasoning_style": "zero_shot", "model": "llama-70b"}
        
        final_agents.append(entry)
        if entry in over_map: final_overs[entry].update(over_map[entry])
        final_overs[entry]["_label"] = model_str + (f":{style}" if len(parts) == 3 else "")
        
    run_experiment(final_agents, args.n, final_overs, args.start, workers=args.workers, resume_csv=args.resume)

if __name__ == "__main__":
    main()
