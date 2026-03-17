"""
Load a subset of HumanEval+ from EvalPlus and save to data/evalplus_subset/.

Each problem is saved as a JSON file:
  data/evalplus_subset/HumanEval_0.json
  ...

Run:
  python scripts/load_dataset.py --n 20
"""
import argparse
import json
from pathlib import Path


def load_and_save(n: int = 20):
    try:
        from evalplus.data import get_human_eval_plus
    except ImportError:
        raise ImportError("Install evalplus: pip install evalplus")

    dataset = get_human_eval_plus()
    out_dir = Path(__file__).parent.parent / "data" / "evalplus_subset"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Take first N problems, sorted by task_id for reproducibility
    problems = sorted(dataset.items())[:n]

    for task_id, prob in problems:
        safe_name = task_id.replace("/", "_")
        out_file  = out_dir / f"{safe_name}.json"
        out_file.write_text(
            json.dumps({
                "task_id":            task_id,
                "entry_point":        prob["entry_point"],
                "prompt":             prob["prompt"],
                "canonical_solution": prob["canonical_solution"],
            }, indent=2),
            encoding="utf-8",
        )
        print(f"  Saved {safe_name}.json")

    print(f"\nDone: {len(problems)} problems saved to {out_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=20, help="Number of problems to load")
    args = parser.parse_args()
    load_and_save(args.n)
