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
from src.agents.reasoning_agents import setup_reasoning_graph
from src.utils.executor      import run_tests
from src.utils.model_registry import get_model, get_token_usage, reset_token_usage

DATA_DIR    = Path("data/evalplus_subset")
RESULTS_DIR = Path("results")

_csv_lock = threading.Lock()

def safe_invoke(agent_fn, prompt, overrides, timeout=300, max_retries=3):
    start_t = time.time()
    for attempt in range(max_retries):
        try:
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
                time.sleep((attempt + 1) * 25); continue
            return f"# ERROR: {e}", {"prompt_tokens":0, "completion_tokens":0, "total_tokens":0}
    return "", {"prompt_tokens":0, "completion_tokens":0, "total_tokens":0}

# ── Runners Coerenti con 0118ef1 ──
def run_baseline(p, o={}): return setup_baseline_graph(model=o.get("model"), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p})["test_code"]
def run_actor_critic(p, o={}): return setup_actor_critic_graph(driver_model=o.get("model"), navigator_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "test_code": "", "feedback": "", "iterations": 0})["test_code"]
def run_adversarial(p, o={}): return setup_adversarial_graph(tester_model=o.get("model"), hacker_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "source_code": p, "test_code": "", "mutated_code": "", "mutation_caught": False})["test_code"]
def run_competitive(p, o={}): return setup_competitive_graph(model_a=o.get("model"), model_b=o.get("model2", o.get("model")), judge_model=o.get("model2", o.get("model"))).invoke({"problem": p, "test_a": "", "test_b": "", "best_test": ""})["best_test"]
def run_hybrid(p, o={}): return setup_hybrid_graph(generate_model=o.get("model"), evolve_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "population": [], "best_test": ""})["best_test"]
def run_coa(p, o={}): return setup_coa_graph(manager_model=o.get("model"), worker_model=o.get("model2", o.get("model"))).invoke({"problem": p, "segments": [], "test_code": ""})["test_code"]
def run_soa(p, o={}): return setup_soa_graph(orchestrator_model=o.get("model"), specialist_model=o.get("model2", o.get("model"))).invoke({"problem": p, "expertise": "", "test_code": ""})["test_code"]
def run_swarm(p, o={}): return setup_swarm_graph(n=o.get("n", 3), worker_model=o.get("model"), aggregator_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "results": [], "final_suite": ""})["final_suite"]
def run_consensus(p, o={}): return setup_consensus_graph(generation_model=o.get("model"), debate_model=o.get("model2", o.get("model"))).invoke({"problem": p, "proposals": [], "final_test": ""})["final_test"]
def run_self_healing(p, o={}): return setup_self_healing_graph(model=o.get("model")).invoke({"problem": p, "test_code": "", "error_message": "", "iteration": 0}).get("test_code", "")
def run_atomic_swarm(p, o={}): return setup_atomic_swarm_graph(model=o.get("model")).invoke({"problem": p, "test_cases": [], "final_suite": ""}).get("final_suite", "")
def run_few_shot(p, o={}): return setup_reasoning_graph("few_shot", model=o.get("model")).invoke({"problem": p}).get("test_code", "")
def run_cot(p, o={}): return setup_reasoning_graph("cot", model=o.get("model")).invoke({"problem": p}).get("test_code", "")
def run_scot(p, o={}): return setup_reasoning_graph("scot", model=o.get("model")).invoke({"problem": p}).get("test_code", "")

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

def run_experiment(agents, n, overrides={}, start=0, workers=50):
    problems = sorted(DATA_DIR.glob("*.json"), key=lambda x: int(re.search(r"(\d+)", x.name).group(1)) if re.search(r"(\d+)", x.name) else 0)[start:start+n]
    problems = [json.loads(p.read_text(encoding="utf-8")) for p in problems]
    
    def run_task(prob, agent_full):
        base_agent = agent_full.split(":")[0]; o = overrides.get(agent_full, {})
        model_slug = o.get("model", "default")
        target_dir = RESULTS_DIR / model_slug
        (target_dir / "tests").mkdir(parents=True, exist_ok=True)
        csv_path = target_dir / "results.csv"

        test_code, usage = safe_invoke(AGENT_FNS[base_agent], prob["prompt"], o)
        save_test_file(target_dir / "tests", prob["task_id"], agent_full, test_code, prob["prompt"])
        
        m = run_tests(prob["prompt"] + prob["canonical_solution"], test_code)
        res = {
            "task_id": prob["task_id"], "agent": base_agent, "config_label": o.get("_label", "default"),
            "passed": m["passed"], "failed": m["failed"], "errors": m["errors"], "total": m["total"],
            "functional_correctness": m["functional_correctness"], "line_coverage": m["line_coverage"],
            "branch_coverage": m["branch_coverage"], "mutation_score": m.get("mutation_score", 0),
            "complexity_cc": m["complexity_cc"], "maintainability_mi": m["maintainability_mi"],
            "bloat_ratio": m["bloat_ratio"], "similarity_score": m["similarity_score"],
            "prompt_tokens": usage["prompt_tokens"], "completion_tokens": usage["completion_tokens"], "total_tokens": usage["total_tokens"]
        }
        with _csv_lock:
            import pandas as pd
            pd.DataFrame([res]).to_csv(csv_path, mode='a', index=False, header=not csv_path.exists())
            print(f"   [DONE] {prob['task_id']} x {agent_full}", flush=True)

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(run_task, p, a): (p, a) for p in problems for a in agents}
        for f in concurrent.futures.as_completed(futures):
            try: f.result(timeout=300)
            except Exception as e: print(f"   [TIMEOUT/ERROR] {e}", flush=True)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agents", nargs="+", default=["tsunami"])
    parser.add_argument("--n", type=int, default=25)
    parser.add_argument("--workers", type=int, default=50)
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
    
    run_experiment(requested, args.n, final_overs, workers=args.workers)

if __name__ == "__main__":
    main()
