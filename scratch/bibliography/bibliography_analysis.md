# Academic Analysis of Agent Performance and Task Alignment

This document analyzes the experimental results of the 11 agent architectures, providing academic justifications for both the high-performing and under-performing configurations.

## 1. The "Task-Agent Mismatch" Phenomenon
A core finding of this project is that agent effectiveness is not universal but highly dependent on **task granularity**. While many multi-agent patterns are successful in general reasoning or long-context tasks, they may fail in the high-precision domain of unit test generation.

## 2. Analysis of Under-Performing Agents

### A. Chain of Agents (CoA) - *Context Overhead*
- **Reference:** Zhang et al. (2024), *Chain of Agents: Large Language Models Collaborating on Long-Context Tasks.*
- **Justification for Failure:** CoA was explicitly designed to handle long-context aggregation (e.g., summarizing 100k+ tokens). In unit test generation (short-context, high-logic tasks), the sequential passing of information introduces **communication noise**. The overhead of multi-step delegation dilutes the model's focus on logic, leading to the observed lower performance.

### B. Self-Healing - *The Hallucination Spiral*
- **Reference:** Charalambous et al. (2025).
- **Justification for Failure:** Self-healing requires a "repair" step that is significantly more robust than the initial "generation" step. In this project, especially for mid-range models (4b-12b), the models entered a **hallucination spiral**: each attempt to fix a syntax error introduced new logical errors, preventing convergence on a correct solution.

### C. Atomic Swarm - *Coherence Loss*
- **Reference:** Chen et al. (2023), *AgentVerse.*
- **Justification for Failure:** Atomic decomposition breaks a task into extremely fine-grained sub-tasks (e.g., inputs vs. assertions). Academic research shows that for coding tasks, this can lead to **loss of global coherence**. The agent writing the assertions loses the full context of the setup prepared by the input agent, resulting in syntactically correct but logically disjointed test suites.

### D. Consensus (Majority Voting) - *The Convergence of Errors*
- **Reference:** Wang et al. (2022), *Self-Consistency.*
- **Justification for Failure:** Consensus works on the premise that wrong answers are diverse, while correct answers are consistent. However, in unit test generation, models often share the same **systemic biases** (e.g., forgetting specific edge cases). This leads to a "majority error" where the most frequent result chosen by the agent is consistently incorrect.

## 3. Analysis of High-Performing Agents

### A. Actor-Critic (CodeRL) - *The Review Advantage*
- **Source:** Le et al. (2023), *CodeRL.*
- **Justification for Success:** Unlike Swarm or CoA, the Actor-Critic model provides a **directional feedback loop**. The Critic does not just aggregate or decompose; it evaluates and guides. This "internal dialogue" mimics the human peer-review process, which is historically the most effective way to produce high-quality code.

### B. Hybrid - *Strategy Ensemble*
- **Justification for Success:** Hybrid architectures benefit from **architectural diversity**. By combining sequential and parallel strategies, they can mitigate the individual weaknesses of each approach, proving more robust across different model sizes (Gemma 3 vs 4).

## Conclusion
The results demonstrate that **simpler, tighter loops (Actor-Critic)** outperform **complex, fragmented architectures (Swarm, CoA)** when applied to high-density logical tasks like test generation for Python programs.
