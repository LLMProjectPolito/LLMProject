# LLM Agents for Collaborative Test Case Generation

This repository contains the implementation and evaluation framework for project **A1: LLM Agents for Collaborative Test Case Generation**. The project explores how multi-agent LLM architectures compare to single-model approaches in generating diverse, high-quality test cases for software code.

## 🚀 Project Overview

The core objective is to evaluate various multi-agent collaboration patterns (e.g., Actor-Critic, Adversarial, Swarm) against standard single-prompt baselines across different reasoning styles (Zero-shot, Chain-of-Thought, etc.) and model sizes.

### Research Questions
- How effective are LLM agents in generating comprehensive and diverse test cases?
- Does agent collaboration outperform single-model test generation?
- What patterns of collaboration lead to higher-quality test cases?

## 🏗️ Architecture

The project is structured into modular components:

- **`src/agents/`**: Implementations of various multi-agent architectures:
  - `baseline.py`: Standard single-agent generation.
  - `actor_critic.py`: Driver/Navigator pattern for iterative refinement.
  - `adversarial.py`: Tester vs. Hacker (mutation testing) pattern.
  - `competitive.py`: Multiple models competing to generate the best test.
  - `consensus.py`: Generation followed by multi-agent debate.
  - `swarm.py` / `atomic_swarm.py`: Parallel generation with aggregation.
  - `self_healing.py`: Iterative correction based on execution feedback.
- **`src/utils/`**: Core utilities for:
  - `executor.py`: Running generated tests and capturing metrics (coverage, pass rate).
  - `model_registry.py`: Interface for various LLM providers and local models.
  - `parser.py`: Robust extraction of Python code from LLM responses.
  - `mutation_check.py`: Utilities for mutation-based quality evaluation.

## 📊 Evaluation Pipeline

The evaluation is driven by `experiment_runner.py`. It automates the process of:
1. Loading problems from the dataset (EvalPlus subset).
2. Invoking the specified agent architectures.
3. Executing the generated tests.
4. Collecting metrics (Functional Correctness, Line Coverage, Mutation Score, Token Usage, etc.).
5. Storing results in CSV format for analysis.

### Running Experiments
```bash
python experiment_runner.py --agents tsunami --n 25 --workers 10
```
*(The `--agents tsunami` flag is a preset that runs a comprehensive benchmark across Gemma models and various agent configurations.)*

## 📈 Analysis & Visualization

Core utilities for processing results are located in `scripts/`:
- `rescore_results.py`: Re-evaluates existing results to ensure metric consistency.

Detailed performance plots and comparative analysis (e.g., best/worst case comparisons) are generated using specialized scripts located in the `scratch/` directories.

## 📁 Repository Structure

```text
├── data/               # Dataset subsets (EvalPlus/HumanEval)
├── scripts/            # Visualization and utility scripts
├── src/                # Core implementation
│   ├── agents/         # Agent architecture definitions
│   └── utils/          # Execution and parsing utilities
├── results/            # Raw experimental data (CSV and generated tests)
├── reports/            # Generated charts and summary reports
├── experiment_runner.py # Main entry point for benchmarks
└── requirements.txt    # Project dependencies
```

## 🛠️ Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure your environment:
   Create a `.env` file (see `.env.example`) with your API keys (e.g., OPENAI_API_KEY, ANTHROPIC_API_KEY, or local model endpoints).

## 📄 License
This project was developed as part of the "LLM for Software Engineering" course (2025-2026).
