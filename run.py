"""
CLI Runner for Project A1 - LLM Multi-Agent Test Generation

Usage examples:
  python run.py --agent baseline --model llama3-70b --problem "def add(a,b): return a+b"
  python run.py --agent adversarial --hacker-model mixtral --tester-model llama3-70b --problem "..."
  python run.py --agent competitive --models llama3-70b mixtral deepseek --problem "..."
  python run.py --agent swarm --worker-model llama3-8b --n 5 --problem "..."
  python run.py --list-models
"""
import argparse
from dotenv import load_dotenv

load_dotenv()

from src.utils.model_registry import AVAILABLE_MODELS
from src.agents.baseline        import setup_baseline_graph
from src.agents.actor_critic    import setup_actor_critic_graph
from src.agents.adversarial     import setup_adversarial_graph
from src.agents.competitive     import setup_competitive_graph
from src.agents.hybrid           import setup_hybrid_graph
from src.agents.coa             import setup_coa_graph
from src.agents.soa             import setup_soa_graph
from src.agents.swarm           import setup_swarm_graph
from src.agents.consensus       import setup_consensus_graph


def run_agent(args):
    problem = args.problem
    agent   = args.agent

    if agent == "baseline":
        graph  = setup_baseline_graph(model=args.model)
        result = graph.invoke({"problem": problem, "test_code": ""})
        print(result["test_code"])

    elif agent == "actor_critic":
        graph  = setup_actor_critic_graph(driver_model=args.driver_model, navigator_model=args.navigator_model)
        result = graph.invoke({"problem": problem, "test_code": "", "feedback": "", "iterations": 0})
        print(result["test_code"])

    elif agent == "adversarial":
        graph  = setup_adversarial_graph(hacker_model=args.hacker_model, tester_model=args.tester_model)
        result = graph.invoke({"source_code": problem, "mutated_code": "", "test_code": "", "mutation_caught": False})
        print(f"Mutation caught: {result['mutation_caught']}")
        print(result["test_code"])

    elif agent == "competitive":
        models = args.models or ["llama3-70b", "mixtral", "deepseek"]
        graph  = setup_competitive_graph(models=models)
        result = graph.invoke({"problem": problem, "generated_tests": {}, "winner": ""})
        print(f"Winner: {result['winner']}")
        print(result["generated_tests"][result["winner"]])

    elif agent == "hybrid":
        graph  = setup_hybrid_graph(generate_model=args.generate_model, evolve_model=args.evolve_model)
        result = graph.invoke({"problem": problem, "population": [], "best_test": ""})
        print(result["best_test"])

    elif agent == "coa":
        graph  = setup_coa_graph(manager_model=args.manager_model, worker_model=args.worker_model)
        result = graph.invoke({"problem": problem, "segments": [], "current_idx": 0, "test_code": ""})
        print(result["test_code"])

    elif agent == "soa":
        graph  = setup_soa_graph(orchestrator_model=args.orchestrator_model, specialist_model=args.specialist_model)
        result = graph.invoke({"problem": problem, "specialists": [], "test_code": ""})
        print(result["test_code"])

    elif agent == "swarm":
        graph  = setup_swarm_graph(n=args.n, worker_model=args.worker_model, aggregator_model=args.aggregator_model)
        result = graph.invoke({"problem": problem, "results": [], "final_suite": ""})
        print(result["final_suite"])

    elif agent == "consensus":
        graph  = setup_consensus_graph(generation_model=args.generation_model, debate_model=args.debate_model)
        result = graph.invoke({"problem": problem, "proposals": [], "final_test": ""})
        print(result["final_test"])


def main():
    parser = argparse.ArgumentParser(description="A1 Multi-Agent Test Generation CLI")
    parser.add_argument("--agent",  type=str, help="Agent to run", choices=[
        "baseline", "actor_critic", "adversarial", "competitive",
        "hybrid", "coa", "soa", "swarm", "consensus"
    ])
    parser.add_argument("--problem", type=str, help="Problem description or source code to test")
    parser.add_argument("--list-models", action="store_true", help="List all available models")

    # Generic model flags
    parser.add_argument("--model",             default="llama3-70b")
    parser.add_argument("--driver-model",      default="llama3-70b")
    parser.add_argument("--navigator-model",   default="gemini-pro")
    parser.add_argument("--hacker-model",      default="mixtral")
    parser.add_argument("--tester-model",      default="llama3-70b")
    parser.add_argument("--models",            nargs="+", default=None)
    parser.add_argument("--generate-model",    default="llama3-70b")
    parser.add_argument("--evolve-model",      default="gemini-pro")
    parser.add_argument("--manager-model",     default="gemini-pro")
    parser.add_argument("--worker-model",      default="llama3-70b")
    parser.add_argument("--orchestrator-model",default="gemini-pro")
    parser.add_argument("--specialist-model",  default="llama3-70b")
    parser.add_argument("--aggregator-model",  default="llama3-70b")
    parser.add_argument("--generation-model",  default="llama3-70b")
    parser.add_argument("--debate-model",      default="gemini-pro")
    parser.add_argument("--n", type=int, default=3, help="Number of swarm agents")

    args = parser.parse_args()

    if args.list_models:
        print("Available models:")
        for name, cfg in AVAILABLE_MODELS.items():
            print(f"  {name:<20} ({cfg['provider']})")
        return

    if not args.agent or not args.problem:
        parser.print_help()
        return

    run_agent(args)


if __name__ == "__main__":
    main()
