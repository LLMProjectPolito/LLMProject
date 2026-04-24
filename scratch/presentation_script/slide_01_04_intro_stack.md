# Slides 1-2: Introduction to LLM Agents in Software Engineering
**Title**: LLM Agents for Collaborative Test Case Generation  
**Course**: LLM for Software Engineering 2025-2026 - Politecnico di Torino  
**Team Members**:  
*   Johnprice Osagie (s344613)  
*   Deniz Eren Gencay (s339282)  
*   Matteo Gastaldello (s345026)  
*   Erestina Vreto (s345027)

## Presentation Overview:
*   **The Shift from Models to Agents**: While LLMs like Gemma are powerful code generators, their raw output often lacks the "deliberation" required for rigorous testing.
*   **The Project Goal**: We evaluate multi-agent architectures where different instances of LLMs collaborate, critique, and refine test cases to achieve higher functional correctness and code coverage.
*   **Why Testing?**: Software testing is the perfect benchmark for agentic reasoning because it requires both a deep understanding of the source code (analysis) and the ability to imagine failure modes (creativity).

---

# Slides 3-4: Tech Stack & Experimental Setup
## Technology Stack:
*   **Inference Engine**: `vLLM` for high-throughput, distributed inference, enabling us to run thousands of agentic interactions efficiently.
*   **Model Registry**: A custom-built runner capable of hot-swapping between different Gemma variants (1b to 31b) and prompting strategies.
*   **Analytical Tools**: `EvalPlus` framework for execution-based validation, `Pandas` for result aggregation, and `Matplotlib/Seaborn` for technical visualization.

## The Dataset: EvalPlus vs. HumanEval
*   **The Limitation of HumanEval**: Original benchmarks often contain weak test suites that allow buggy code to pass (False Positives).
*   **The EvalPlus Advantage**: It enhances HumanEval by adding ~80x more test cases per problem, specifically targeting edge cases (empty lists, large integers, floating-point precision).
*   **Our Benchmark**: We use **HumanEval+**, which forces our agents to generate code that is not just syntactically correct, but logically robust across a massive range of inputs.
