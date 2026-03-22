# 🎯 Project Finale: Implementation Roadmap

This document outlines the final strategy to conclude the project with scientifically unassailable results. We have transformed the framework into a modular system where **Architecture** and **Reasoning** are now independent building blocks.

---

## 🏗️ Current Agent Status
The framework includes **11 different architectures**, but for the final phase, we are focusing on the **5 most promising ones**. Here is the complete taxonomy and the reasoning for selection.

### 🔝 The "Essential 5" (High Priority)
These agents have demonstrated the best quality/price/stability ratio:
1.  **`baseline`**: Indispensable as a scientific control (reference standard).
2.  **`swarm`**: Fundamental for diversity. Multiple agents covering different code branches.
3.  **`actor_critic`**: The core of iterative optimization. Real-time error correction.
4.  **`adversarial`**: Our "secret weapon" for robustness (Red Team vs Blue Team).
5.  **`hybrid`**: The most advanced, using genetic logic to fuse the best of multiple worlds.

### 📦 "Shelved" Agents (Archived)
These agents are implemented but excluded from the final runs for specific technical reasons:
6.  **`competitive`**: Similar to Swarm but less efficient. Swarm with an `Aggregator` produces better results than pure competition.
7.  **`coa` (Chain of Agents)**: Too linear. If one agent in the chain fails, the error propagates. `Actor-Critic` is superior as it includes feedback.
8.  **`soa` (Select of Agents)**: Highly dependent on Orchestrator quality. On 8B models, the orchestrator often makes poor choices.
9.  **`consensus`**: Requires too many calls (Debate) and often ends in infinite loops or consumes too many tokens without real gain over Hybrid.
10. **`self_healing`**: Already implicitly integrated into `Actor-Critic`. Having a separate file is redundant.
11. **`atomic_swarm`**: A "micro" version of Swarm. We preferred boosting the main `Swarm` by making it modular.

### 🧠 Reasoning Styles (Applicable to all nodes)
*   **`zero_shot`**: Direct response.
*   **`cot`**: Chain of Thought (Free reasoning).
*   **`scot`**: Structured CoT (Step 1, Step 2, Step 3).
*   **`few_shot`**: Learning through examples.

---

## 🚀 The "Final Boss" Runs (Action Plan)

These are the 3 conclusive runs that will generate the data for your final report.

### Run A: The Reasoning Showdown (Pure Precision)
*Objective*: See if A-C or Hybrid can close the gap with 70B using CoT.
`python experiment_runner.py --agents baseline:70b baseline:cot:8b actor_critic:cot:8b hybrid:cot:8b --n 20`

### Run B: The Swarm Evolution (Maximum Coverage)
*Objective*: Test if Swarm (multiple heads) beats single CoT (single thinking head) on coverage problems.
`python experiment_runner.py --agents baseline:cot:8b swarm:8b swarm:cot:8b --n 20`

### Run C: The Adversarial Stress-Test (Robustness)
*Objective*: Challenge the Adversarial agent to find bugs that 70B doesn't see.
`python experiment_runner.py --agents baseline:70b adversarial:cot:8b --n 20`

---

## 🧪 Modularity Test (Completed)
Successfully tested the loading of styles:
`python experiment_runner.py --agents swarm:cot:8b actor_critic:cot:8b baseline:cot:8b --n 2`

---
*Roadmap updated on 15/03/2026 - The framework is now ready for glory.*
