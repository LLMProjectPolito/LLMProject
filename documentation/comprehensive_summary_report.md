# 📋 Project Overview: LLM Agent Performance Comparison

This report summarizes all experimental runs conducted to evaluate and compare LLM agent performance on the **EvalPlus (HumanEval+)** dataset. 

## 🎯 Global Objective
To demonstrate that sophisticated agentic architectures and reasoning techniques can enable small language models (≤ 8B) to match or exceed the performance of much larger models (70B) at a fraction of the cost.

---

## 🛤️ Evolution of Experiments

### Phase 1: Establishing the "Gold Standard"
*   **Key Run**: `run_20260314_1826` (Baseline 70B)
*   **Goal**: Define the performance ceiling using a top-tier model (Llama-3 70B) in a simple Zero-Shot setting.
*   **Result**: Functional Correctness ~0.83 on early problems.
*   **Insight**: 70B models are very reliable on generic cases but have high usage costs.

### Phase 2: Agent Architecture Scrutiny
*   **Key Runs**: `run_20260314_1944` & `run_20260314_1950`
*   **Goal**: Test complex architectures (Swarm, Hybrid Evolution, Actor-Critic) on 8B models.
*   **Result**: Mixed. While coverage remained high, Functional Correctness suffered due to "hallucinated placeholders" and model fatigue in complex chains.
*   **Insight**: Complex graphs require stricter prompt constraints for smaller models to avoid losing track of the goal.

### Phase 3: Reasoning Style Optimization
*   **Key Run**: `run_20260314_2109`
*   **Goal**: Compare Zero-Shot vs. Few-Shot vs. CoT vs. SCoT on the same 8B model.
*   **Result**: 
    *   **CoT (Winner)**: 0.78 FC
    *   **Few-Shot**: 0.62 FC
    *   **SCoT**: 0.56 FC
*   **Insight**: **Chain of Thought (CoT)** is the sweet spot for 8B models. SCoT is too verbose and "exhausts" the model's reasoning capacity.

### Phase 4: Parallelization & Scaling (Current)
*   **Key Run**: `run_20260314_2132` (Ongoing)
*   **Goal**: Massively parallelized run (10 threads) comparing the best of all previous phases.
*   **Setup**: 70B Baseline vs. 8B (CoT, Swarm, Hybrid, Consistency).

---

## 📈 Aggregated Insights

| Category | Best Performer | Metric | Why it works |
| :--- | :--- | :--- | :--- |
| **Logic Reasoning** | **CoT (8B)** | 0.78 FC | Forces the model to build a mental map before coding. |
| **Collaboration** | **Swarm (8B)** | High Cov | Multiple workers catch more diverse edge cases. |
| **Efficiency** | **FS (8B)** | Low Token | Fast, but prone to imitating bad examples. |
| **Stability** | **70B (ZS)** | 0.83+ FC | High intrinsic knowledge, low prompt sensitivity. |

## 🛠️ Lessons Learned
1.  **Prompt Engineering vs. Multi-Agent**: For 8B models, a single-step CoT is often more effective than a multi-agent Swarm if those agents don't have enough "intelligence" to critique each other.
2.  **Rate Limits**: The biggest bottleneck. Our move to a **Parallel Multiprovider Fallback** system was critical to making the project viable with free API tiers.
3.  **Code Extraction**: Regex-based extraction is robust, but models need strict rules (CORE RULES) to avoid redefining functions and breaking imports.

---
*Report generated on 2026-03-14 21:30*
