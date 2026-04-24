# Slides 19-21: Technical Metrics Explained
Our evaluation goes beyond simple "Pass/Fail." We use four dimensions of quality:
1.  **Functional Correctness (Pass@1)**: Verified via execution on EvalPlus. Does the test case accurately identify the function's contract?
2.  **Code Coverage (Line/Branch)**: Using `coverage.py` to ensure the agents aren't just testing the "happy path" but also exploring conditional branches and error handling.
3.  **Mutation Score (Robustness)**: We inject "mutants" (artificial bugs like changing `>` to `>=`) into the source code. A high score means our generated tests are "strong" enough to detect these changes.
4.  **Token Efficiency**: Performance normalized by cost. Crucial for understanding the "Agentic Tax"—the trade-off between higher quality and increased inference cost.

---

# Slides 21-22: Core Conclusions & Insights
*   **The Agentic Advantage**: Multi-agent collaboration (especially Actor-Critic and Hybrid) consistently outperforms single-prompt generation by **15-40%** in complex tasks.
*   **Prompting Matters**: SCoT (Structured CoT) is the most reliable way to stabilize LLM output for formal tasks like code generation.
*   **Model Maturity**: We are reaching a point where parameter count is less important than **Architecture**. Small models (2b/4b) in a multi-agent setup can outperform much larger models in a zero-shot setup.
*   **The Regression Warning**: Newer models (Gemma-4 series) show incredible gains but can be sensitive to specific prompting styles, requiring careful tuning of the "Instruction Following" vs. "Reasoning" balance.

---

# Slide 23: Future Work & Next Horizons
*   **RLM (Reasoning Language Models)**: Moving from prompt-based reasoning to test-time computation (inference-time scaling), allowing agents to "think" longer before generating a test.
*   **JEPA Architectures**: Integrating World Models (like Yann LeCun's JEPA) to allow agents to predict the execution path of code without actually running it, reducing the need for expensive execution loops.
*   **Cross-Model Swarms**: Evaluating collaboration between heterogeneous models (e.g., using a high-precision model like Gemma-31b as a Critic for a faster model like Gemma-4-4b).
*   **Self-Improving Agents**: Using the generated test results to fine-tune the agents themselves via DPO (Direct Preference Optimization).
