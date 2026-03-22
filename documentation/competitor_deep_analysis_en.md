# 🕵️‍♂️ In-Depth Competitor Analysis

This document analyzes the performance and strategies of rival groups (Group 1 and Group 14) to highlight the strengths of our framework.

---

### 🟢 Group 1: 30LLM (Multi-Agent for Collaborative Testing)
**Benchmark**: Standard HumanEval | **Model**: Nemotron 30B

| Strategy | Baseline (Zero-Shot) | Agentic Approach (QA Agent) | Improvement |
| :--- | :--- | :--- | :--- |
| **Standard** | 48.66% | 71.76% | +23.1% |
| **Augmented** (Prompt Opt) | 98.48%* | 100.00%* | +1.52% |

**Critical Analysis**:
*   **The Prompt Illusion**: Their massive jump (from 48% to 100%) is almost entirely due to switching from a "basic" prompt to an "optimized" one (Augmented Few-Shot). The multi-agent architecture itself added less than 2% value.
*   **Model Size**: They use a **30B** model. The fact that we obtain similar results with an **8B** proves that our reasoning approach (CoT) is far more efficient.
*   **Benchmark**: Standard HumanEval is now "solved" by many models via memory. The lack of extra test cases (which we have in Eval+) makes their 100% scores less reliable than our 80% scores.

---

### 🔴 Group 14: Collaborative & Competitive Loops
**Benchmark**: Custom (6 academic Python classes) | **Model**: GPT-OSS 120B / Llama 70B

| Strategy | Baseline (Zero-Shot) | Agentic Approach | Token Usage |
| :--- | :--- | :--- | :--- |
| **Single Agent** | 92.00% (Coverage) | - | 1.3k |
| **Collaborative** | - | 94.00% (Mutation Score) | 12.3k |

**Critical Analysis**:
*   **Disastrous Efficiency**: To achieve a minimal improvement (+2% mutation score), their agentic system consumes **10 times more tokens** than the baseline. This is the opposite of optimization.
*   **Saturation**: They chose problems that were too simple. If the baseline is already at 92%, there is no room to demonstrate agent superiority. It’s an experimental design flaw.
*   **Cognitive Confusion**: On the most complex problems in their set, the agentic approach performed **worse** than the baseline (79% vs 85%), proving that too many agents without a reasoning logic (like CoT) only introduce noise.

---

### 🏆 Final Comparison vs Project A1 (Us)

1.  **Rigorous Benchmarking**: We use **HumanEval+** (Subset Hard). Each of our functions has 80+ test cases. They have 3 or 4. Our 80% is "real," while their 100% is often superficial.
2.  **Hardware Efficiency**: We scale down (**8B, 3B, and even 1B**). They scale up (30B, 70B, 120B). Our challenge is to make a small model intelligent; theirs is to make massive, already intelligent models talk to each other.
3.  **Modularity**: We can toggle reasoning (CoT) on any architecture. They have "fixed" architectures that cannot adapt to problem complexity.

*Conclusion: Our approach is scientifically more advanced because it separates Reasoning from Organization (Architecture), allowing for a win where brute force fails.*
