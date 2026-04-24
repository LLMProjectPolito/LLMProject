# Slides 10-18: Model Results Deep Dive
For each model, we analyze the performance of its top 10 and bottom 5 combinations, measured against the `baseline-zero_shot` (highlighted in **BLUE**).

## 1. Gemma-31b: The State-of-the-Art
*   **Best Combination**: `hybrid - zero_shot` (**0.976**) - Achieved near-perfect functional correctness.
*   **Observation**: High-capacity models like 31b benefit most from structured role-play (Hybrid) rather than just more reasoning tokens (CoT).
*   **Key Metrics**: Mutation Score was exceptionally high, indicating that the tests generated were capable of catching most artificial bugs.

## 2. Gemma-4-26b: The Coverage Master
*   **Best Combination**: `baseline - few_shot` (**0.905**) - A massive leap for the 26b parameter class.
*   **Efficiency vs Quality**: While it consumes significant tokens (~23k avg), it produces the most exhaustive test suites.
*   **Code Coverage**: Reached **96.3% Line Coverage**, the highest in our entire study. It excels at path exploration.

## 3. Gemma-27b: The Balance of Power
*   **Best Combination**: `hybrid - scot` (**0.81**).
*   **Insight**: This model acts as the "Efficiency Sweet Spot." It provides high-tier results with much lower latency than the 31b or 4-26b models.

## 4. Gemma-12b: The Mid-Tier Standard
*   **Best Combination**: `actor_critic - cot` (**0.72**).
*   **Analysis**: This model relies heavily on the "Critic" feedback to fix logical errors in test cases. Without agents, its performance drops significantly.

## 5. Gemma-4-2b / 4-4b: The New Generation Small Models
*   **Performance**: Both models reached ~0.71 correctness.
*   **Comparison**: A **+366%** improvement over the previous generation (Gemma-1b). 
*   **Takeaway**: Modern "small" models are now as capable as previous "medium" models (12b).

## 6. The Curious Case of Gemma-4-4b (Regression)
*   **The Issue**: Significant drop in performance when using `scot` prompting (-73% vs. baseline).
*   **Why?**: Newer models are sometimes "over-refined" for chat, making them less capable of following strict, multi-step structural prompts like SCoT, which they might perceive as "noise" compared to direct instructions.

---

### Quantitative Metric Summary (Top Performers)
| Model | Correctness | Line Coverage | Efficiency (Score/1k) |
| :--- | :--- | :--- | :--- |
| **Gemma-31b** | **0.976** | 81.1% | 0.116 |
| **Gemma-4-26b** | 0.905 | **96.3%** | 0.096 |
| **Gemma-4b** | 0.770 | 83.6% | **0.475** |
| **Gemma-27b** | 0.807 | 82.2% | 0.269 |
