import argparse, re, csv, json, time, concurrent.futures, threading, os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Imports coerenti con lo schema originale
from src.agents.baseline     import setup_baseline_graph
from src.agents.actor_critic import setup_actor_critic_graph
from src.agents.adversarial  import setup_adversarial_graph
from src.agents.competitive  import setup_competitive_graph
from src.agents.hybrid       import setup_hybrid_graph
from src.agents.coa          import setup_coa_graph
from src.agents.soa          import setup_soa_graph
from src.agents.swarm        import setup_swarm_graph
from src.agents.consensus    import setup_consensus_graph
from src.agents.self_healing import setup_self_healing_graph
from src.agents.atomic_swarm import setup_atomic_swarm_graph
# Rimossa dipendenza non esistente: src.agents.reasoning_agents
from src.utils.executor      import run_tests
from src.utils.generation_errors import classify_generation_error, compute_retry_delay
from src.utils.model_registry import get_model, get_token_usage, reset_token_usage

DATA_DIR = Path("data/evalplus_subset")
DEFAULT_RESULTS_DIR = Path("results")

_csv_lock = threading.Lock()

def safe_invoke(agent_fn, prompt, overrides, timeout=300, max_retries=5):
    start_t = time.time()
    for attempt in range(1, max_retries + 1):
        try:
            reset_token_usage()
            test_code = agent_fn(prompt, overrides)
            usage = get_token_usage()
            return test_code, {
                "prompt_tokens": usage["prompt_tokens"],
                "completion_tokens": usage["completion_tokens"],
                "total_tokens": usage["total_tokens"],
                "execution_time": round(time.time() - start_t, 2),
                "generation_status": "ok",
                "generation_error_type": "",
                "generation_error_message": "",
                "generation_attempts": attempt,
            }
        except Exception as e:
            usage = get_token_usage()
            error_info = classify_generation_error(e)
            if error_info["retryable"] and attempt < max_retries:
                time.sleep(compute_retry_delay(attempt))
                continue
            return f"# ERROR: {e}", {
                "prompt_tokens": usage["prompt_tokens"],
                "completion_tokens": usage["completion_tokens"],
                "total_tokens": usage["total_tokens"],
                "execution_time": round(time.time() - start_t, 2),
                "generation_status": "error",
                "generation_error_type": error_info["type"],
                "generation_error_message": error_info["message"],
                "generation_attempts": attempt,
            }
    return "", {
        "prompt_tokens": 0,
        "completion_tokens": 0,
        "total_tokens": 0,
        "execution_time": round(time.time() - start_t, 2),
        "generation_status": "error",
        "generation_error_type": "unknown_error",
        "generation_error_message": "Generation failed without a captured exception.",
        "generation_attempts": max_retries,
    }


def generation_failure_metrics(message: str) -> dict:
    return {
        "passed": 0, "failed": 0, "errors": 1, "total": 1,
        "functional_correctness": 0, "line_coverage": None, "branch_coverage": None,
        "mutation_score": 0, "complexity_cc": 0, "maintainability_mi": 0,
        "bloat_ratio": 0, "similarity_score": 0,
        "unique_inputs_count": 0, "edge_case_count": 0, "test_type_count": 0,
        "duplication_ratio": 1.0, "diversity_score": 0,
        "raw_output": message,
    }

# ── Runners Coerenti con 0118ef1 ──
def run_baseline(p, o={}): return setup_baseline_graph(model=o.get("model"), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p})["test_code"]
def run_actor_critic(p, o={}): return setup_actor_critic_graph(driver_model=o.get("model"), navigator_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "test_code": "", "feedback": "", "iterations": 0})["test_code"]
def run_adversarial(p, o={}): return setup_adversarial_graph(tester_model=o.get("model"), hacker_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "source_code": p, "test_code": "", "mutated_code": "", "mutation_caught": False})["test_code"]
def run_competitive(p, o={}):
    models = [o.get("model")]
    alt_model = o.get("model2", o.get("model"))
    if alt_model and alt_model != models[0]:
        models.append(alt_model)
    final_state = setup_competitive_graph(models=models).invoke({"problem": p, "generated_tests": {}, "winner": ""})
    return final_state["generated_tests"][final_state["winner"]]
def run_hybrid(p, o={}): return setup_hybrid_graph(generate_model=o.get("model"), evolve_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "population": [], "best_test": ""})["best_test"]
def run_coa(p, o={}): return setup_coa_graph(manager_model=o.get("model"), worker_model=o.get("model2", o.get("model"))).invoke({"problem": p, "segments": [], "test_code": ""})["test_code"]
def run_soa(p, o={}): return setup_soa_graph(orchestrator_model=o.get("model"), specialist_model=o.get("model2", o.get("model"))).invoke({"problem": p, "expertise": "", "test_code": ""})["test_code"]
def run_swarm(p, o={}): return setup_swarm_graph(n=o.get("n", 3), worker_model=o.get("model"), aggregator_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "results": [], "final_suite": ""})["final_suite"]
def run_consensus(p, o={}): return setup_consensus_graph(generation_model=o.get("model"), debate_model=o.get("model2", o.get("model"))).invoke({"problem": p, "proposals": [], "final_test": ""})["final_test"]
def run_self_healing(p, o={}): return setup_self_healing_graph(model=o.get("model")).invoke({"problem": p, "test_code": "", "error_message": "", "iteration": 0}).get("test_code", "")
def run_atomic_swarm(p, o={}): return setup_atomic_swarm_graph(model=o.get("model")).invoke({"problem": p, "test_cases": [], "final_suite": ""}).get("final_suite", "")
def run_few_shot(p, o={}): return setup_baseline_graph(model=o.get("model"), reasoning_style="few_shot").invoke({"problem": p}).get("test_code", "")
def run_cot(p, o={}):      return setup_baseline_graph(model=o.get("model"), reasoning_style="cot").invoke({"problem": p}).get("test_code", "")
def run_scot(p, o={}):     return setup_baseline_graph(model=o.get("model"), reasoning_style="scot").invoke({"problem": p}).get("test_code", "")

AGENT_FNS = {
    "baseline": run_baseline, "actor_critic": run_actor_critic, "adversarial": run_adversarial,
    "competitive": run_competitive, "hybrid": run_hybrid, "coa": run_coa, "soa": run_soa,
    "swarm": run_swarm, "consensus": run_consensus, "self_healing": run_self_healing,
    "atomic_swarm": run_atomic_swarm, "few_shot": run_few_shot, "cot": run_cot, "scot": run_scot
}

def save_test_file(target_dir, task_id, agent_name, test_code, prompt):
    safe_task = task_id.replace("/", "_"); safe_agent = agent_name.replace(":", "_")
    full_content = f"{prompt}\n{test_code}"
    (target_dir / f"{safe_task}__{safe_agent}.py").write_text(full_content, encoding="utf-8")

def run_experiment(agents, n, overrides={}, start=0, workers=50, results_dir: Path = DEFAULT_RESULTS_DIR):
    problems = sorted(DATA_DIR.glob("*.json"), key=lambda x: int(re.search(r"(\d+)", x.name).group(1)) if re.search(r"(\d+)", x.name) else 0)[start:start+n]
    problems = [json.loads(p.read_text(encoding="utf-8")) for p in problems]
    
    def is_already_done(task_id, config_label, csv_path):
        if not csv_path.exists(): return False
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                return any(row.get('task_id') == task_id and row.get('config_label') == config_label for row in reader)
        except: return False

    def run_task(prob, agent_full):
        base_agent = agent_full.split(":")[0]; o = overrides.get(agent_full, {})
        model_slug = o.get("model", "default")
        label = o.get("_label", "default")
        target_dir = results_dir / model_slug
        csv_path = target_dir / "results.csv"

        if is_already_done(prob["task_id"], label, csv_path):
            print(f"   [SKIP] {prob['task_id']} x {agent_full}", flush=True)
            return

        (target_dir / "tests").mkdir(parents=True, exist_ok=True)
        test_code, usage = safe_invoke(AGENT_FNS[base_agent], prob["prompt"], o)
        save_test_file(target_dir / "tests", prob["task_id"], agent_full, test_code, prob["prompt"])

        if usage["generation_status"] == "error":
            m = generation_failure_metrics(usage["generation_error_message"])
        else:
            m = run_tests(prob["prompt"] + prob["canonical_solution"], test_code)
        
        res = {
            "task_id": prob["task_id"], "agent": base_agent, "config_label": label,
            "passed": m["passed"], "failed": m["failed"], "errors": m["errors"], "total": m["total"],
            "functional_correctness": m["functional_correctness"], "line_coverage": m["line_coverage"],
            "branch_coverage": m["branch_coverage"], "mutation_score": m.get("mutation_score", 0),
            "complexity_cc": m["complexity_cc"], "maintainability_mi": m["maintainability_mi"],
            "bloat_ratio": m["bloat_ratio"], "similarity_score": m["similarity_score"],
            "unique_inputs_count": m["unique_inputs_count"], "edge_case_count": m["edge_case_count"],
            "test_type_count": m["test_type_count"], "duplication_ratio": m["duplication_ratio"],
            "diversity_score": m["diversity_score"],
            "prompt_tokens": usage["prompt_tokens"], "completion_tokens": usage["completion_tokens"], "total_tokens": usage["total_tokens"],
            "execution_time": usage["execution_time"], "generation_status": usage["generation_status"],
            "generation_error_type": usage["generation_error_type"], "generation_error_message": usage["generation_error_message"],
            "generation_attempts": usage["generation_attempts"],
        }
        with _csv_lock:
            import pandas as pd
            pd.DataFrame([res]).to_csv(csv_path, mode='a', index=False, header=not csv_path.exists())
            print(f"   [DONE] {prob['task_id']} x {agent_full}", flush=True)

    # SHUFFLE WORK: Mischiamo i task per evitare ingorghi su un singolo modello o task
    import random
    work_items = [(p, a) for p in problems for a in agents]
    random.shuffle(work_items)

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(run_task, p, a): (p, a) for p, a in work_items}
        for f in concurrent.futures.as_completed(futures):
            try: f.result(timeout=300)
            except Exception as e: print(f"   [TIMEOUT/ERROR] {e}", flush=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agents", nargs="+", default=["tsunami"])
    parser.add_argument("--n", type=int, default=25)
    parser.add_argument("--workers", type=int, default=50)
    parser.add_argument("--output-root", type=str, default=str(DEFAULT_RESULTS_DIR))
    args = parser.parse_args()

    if "tsunami" in args.agents:
        m = ['gemma-1b', 'gemma-4b', 'gemma-12b', 'gemma-27b']
        p = ['zero_shot', 'cot', 'scot', 'few_shot']
        a = ['baseline', 'actor_critic', 'adversarial', 'competitive', 'hybrid', 'coa', 'soa', 'swarm', 'consensus', 'self_healing', 'atomic_swarm']
        requested = [f"{ag}:{mo}:{pr}" for mo in m for pr in p for ag in a]
    else: requested = args.agents

    final_overs = {}
    for entry in requested:
        parts = entry.split(":")
        if len(parts) >= 2:
            mo = parts[1]; st = parts[2] if len(parts)==3 else "zero_shot"
            final_overs[entry] = {"reasoning_style": st, "model": mo, "_label": f"{mo}:{st}"}
    
    run_experiment(
        requested,
        args.n,
        final_overs,
        workers=args.workers,
        results_dir=Path(args.output_root),
    )

if __name__ == "__main__":
    main()
