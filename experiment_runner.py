import argparse
import re
import csv
import json
import time
import concurrent.futures
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from langchain_community.callbacks import get_openai_callback

load_dotenv()

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
from src.utils.executor      import run_tests

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
    "self_healing", "atomic_swarm", "few_shot", "cot", "scot", "consistency", "tot"
]

def safe_invoke(agent_fn, prompt, overrides, timeout=180, max_retries=3):
    """
    Calls an agent function and tracks tokens.
    """
    usage_stats = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    for attempt in range(max_retries):
        try:
            with get_openai_callback() as cb:
                test_code = agent_fn(prompt, overrides)
                usage_stats = {
                    "prompt_tokens": cb.prompt_tokens,
                    "completion_tokens": cb.completion_tokens,
                    "total_tokens": cb.total_tokens
                }
                return test_code, usage_stats
        except Exception as e:
            err_str = str(e).lower()
            if ("429" in err_str or "rate limit" in err_str) and attempt < max_retries - 1:
                wait_time = (attempt + 1) * 30
                print(f"   [!] Rate limit (429) hit. Waiting {wait_time}s...")
                time.sleep(wait_time)
                continue
            print(f"   [!] Error: {e}")
            return f"# ERROR: {e}", usage_stats
    return "", usage_stats

# Agent runners
def run_baseline(p, o={}): 
    return setup_baseline_graph(model=o.get("model"), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p})["test_code"]

def run_actor_critic(p, o={}): 
    return setup_actor_critic_graph(driver_model=o.get("model"), navigator_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "test_code": "", "feedback": "", "iterations": 0})["test_code"]

def run_adversarial(p, o={}): 
    return setup_adversarial_graph(tester_model=o.get("model"), hacker_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "source_code": p, "test_code": "", "mutated_code": "", "mutation_caught": False})["test_code"]

def run_competitive(p, o={}): 
    return setup_competitive_graph(model_a=o.get("model"), model_b=o.get("model2", o.get("model")), judge_model=o.get("model2", o.get("model"))).invoke({"problem": p, "test_a": "", "test_b": "", "best_test": ""})["best_test"]

def run_hybrid(p, o={}): 
    return setup_hybrid_graph(generate_model=o.get("model"), evolve_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "population": [], "best_test": ""})["best_test"]

def run_coa(p, o={}): 
    return setup_coa_graph(manager_model=o.get("model"), worker_model=o.get("model2", o.get("model"))).invoke({"problem": p, "segments": [], "test_code": ""})["test_code"]

def run_soa(p, o={}): 
    return setup_soa_graph(orchestrator_model=o.get("model"), specialist_model=o.get("model2", o.get("model"))).invoke({"problem": p, "expertise": "", "test_code": ""})["test_code"]

def run_swarm(p, o={}): 
    return setup_swarm_graph(n=o.get("n", 3), worker_model=o.get("model"), aggregator_model=o.get("model2", o.get("model")), reasoning_style=o.get("reasoning_style", "zero_shot")).invoke({"problem": p, "results": [], "final_suite": ""})["final_suite"]

def run_consensus(p, o={}): 
    return setup_consensus_graph(generation_model=o.get("model"), debate_model=o.get("model2", o.get("model"))).invoke({"problem": p, "proposals": [], "final_test": ""})["final_test"]

def run_self_healing(p, o={}): 
    return setup_self_healing_graph(model=o.get("model")).invoke({"problem": p, "test_code": "", "error_message": "", "iteration": 0}).get("test_code", "")

def run_atomic_swarm(p, o={}): 
    return setup_atomic_swarm_graph(model=o.get("model")).invoke({"problem": p, "test_cases": [], "final_suite": ""}).get("final_suite", "")

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
    ts = datetime.now().strftime("%Y%m%d_%H%M%S"); d = RESULTS_DIR / f"run_{ts}"; d.mkdir(parents=True, exist_ok=True); (d/"tests").mkdir(exist_ok=True); return d

def save_test_file(run_dir, task_id, agent, test_code):
    safe_task = task_id.replace("/", "_"); safe_agent = agent.replace(":", "_").replace("/", "_")
    (run_dir / "tests" / f"{safe_task}__{safe_agent}.py").write_text(test_code, encoding="utf-8")

def save_csv(run_dir, rows):
    path = run_dir / "results.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS); writer.writeheader(); writer.writerows(rows)
    return path

def save_metadata(run_dir, agents, n, rows, start_ts, end_ts):
    meta = {"start_ts": start_ts, "end_ts": end_ts, "agents": agents, "n_problems": n, "total_runs": len(rows)}
    (run_dir / "metadata.json").write_text(json.dumps(meta, indent=2), encoding="utf-8"); return run_dir / "metadata.json"

def try_plot_radar(run_dir):
    import subprocess, sys
    subprocess.run([sys.executable, "scripts/plot_v2.py", "--csv", str(run_dir / "results.csv"), "--out", str(run_dir)], check=False)

def load_problems(n, start=0):
    files = sorted(DATA_DIR.glob("*.json"), key=lambda x: int(re.search(r"(\d+)", x.name).group(1)) if re.search(r"(\d+)", x.name) else 0)[start:start+n]
    return [json.loads(f.read_text(encoding="utf-8")) for f in files]

def run_experiment(agents, n, overrides={}, start=0):
    start_ts = datetime.now().isoformat(); run_dir = make_run_dir(); problems = load_problems(n, start)
    print(f"Run dir: {run_dir}\nAgents: {agents}\n")
    rows = []

    def run_task_for_agent(prob, agent_name):
        task_id = prob["task_id"]; source = prob["prompt"] + prob["canonical_solution"]
        base_agent = agent_name.split(":")[0]; agent_overrides = overrides.get(agent_name, {})
        t0 = time.time()
        try:
            print(f"   [{agent_name}] generating...", flush=True)
            test_code, usage = safe_invoke(AGENT_FNS[base_agent], prob["prompt"], agent_overrides)
            save_test_file(run_dir, task_id, agent_name, test_code)
            metrics = run_tests(source, test_code)
            elapsed = round(time.time() - t0, 2)
            print(f"   [DONE] {task_id} x {agent_name} -> FC={metrics['functional_correctness']:.2f}", flush=True)
            return {
                "task_id": task_id, "agent": base_agent, "config_label": agent_overrides.get("_label", "default"),
                "passed": metrics["passed"], "failed": metrics["failed"], "errors": metrics["errors"],
                "total": metrics["total"], "functional_correctness": metrics["functional_correctness"],
                "line_coverage": metrics["line_coverage"], "branch_coverage": metrics["branch_coverage"],
                "mutation_score": metrics.get("mutation_score", 0), "complexity_cc": metrics["complexity_cc"],
                "maintainability_mi": metrics["maintainability_mi"], "bloat_ratio": metrics["bloat_ratio"],
                "similarity_score": metrics["similarity_score"], "elapsed_s": elapsed,
                "prompt_tokens": usage["prompt_tokens"], "completion_tokens": usage["completion_tokens"], "total_tokens": usage["total_tokens"]
            }
        except Exception as e:
            print(f"   [FATAL] {agent_name} on {task_id}: {e}", flush=True); return None

    for prob in problems:
        print(f"── {prob['task_id']} (Parallel Agents) ──")
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(len(agents), 10)) as executor:
            futures = [executor.submit(run_task_for_agent, prob, a) for a in agents]
            for future in concurrent.futures.as_completed(futures):
                res = future.result()
                if res: rows.append(res); save_csv(run_dir, rows)

    save_metadata(run_dir, agents, n, rows, start_ts, datetime.now().isoformat())
    try_plot_radar(run_dir)
    print(f"\n✅ Run complete. CSV -> {run_dir}/results.csv")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--agents", nargs="+", default=["all"])
    parser.add_argument("--n", type=int, default=20)
    parser.add_argument("--start", type=int, default=0)
    parser.add_argument("--overrides", type=str, default="")
    args = parser.parse_args()
    
    requested = ALL_AGENTS if "all" in args.agents else args.agents
    over_map = {}
    for part in args.overrides.split(","):
        if "=" in part and ":" in part:
            agent_full, kv = part.rsplit(":", 1)
            k, v = kv.split("=", 1)
            if agent_full not in over_map: over_map[agent_full] = {}
            over_map[agent_full][k] = int(v) if v.isdigit() else v

    final_agents = []; final_overs = {}
    for entry in requested:
        parts = entry.split(":")
        if len(parts) >= 2:
            agent_type = parts[0]
            style = parts[1] if len(parts) == 3 else "zero_shot"
            model_str = parts[2] if len(parts) == 3 else parts[1]
            
            if "/" in model_str:
                m1, m2 = model_str.split("/", 1)
                final_overs[entry] = {"reasoning_style": style, "model": m1, "model2": m2}
            else:
                final_overs[entry] = {"reasoning_style": style, "model": model_str}
        else:
            agent_type = entry
            final_overs[entry] = {"reasoning_style": "zero_shot", "model": "llama3-8b"}
            
        final_agents.append(entry)
        # Apply manual overrides on top
        if entry in over_map:
            final_overs[entry].update(over_map[entry])
        
        # Add label for results
        final_overs[entry]["_label"] = ":".join(parts[1:]) if len(parts) > 1 else "default"
        
    run_experiment(final_agents, args.n, final_overs, args.start)

if __name__ == "__main__":
    main()
