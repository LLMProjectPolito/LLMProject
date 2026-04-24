# Slide 5: Prompting Strategies - From Zero-Shot to SCoT
Effective agent communication starts with the prompt structure. We compared four main strategies:
*   **Zero-Shot**: Direct instruction. Tests the model's raw capability.
*   **Few-Shot**: Contextual learning using 3-5 high-quality examples.
*   **Chain of Thought (CoT)**: Encourages the model to output its reasoning before the code.
*   **Structured CoT (SCoT)**: Enforces a strict 3-step reasoning template (Analysis -> Strategy -> Implementation).

---

# Slides 6-9: The 11 Agent Architectures

## 1. Baseline
Single-turn generation without any feedback or iteration.
```python
def baseline(source):
    return llm.generate(f"Write test for: {source}")
```

## 2. Actor-Critic
The **Actor** generates code, while the **Critic** provides technical feedback for refinement.
```python
def actor_critic(source):
    test = actor.generate(source)
    for _ in range(MAX):
        feedback = critic.review(test)
        if feedback.is_pass(): break
        test = actor.refine(test, feedback)
    return test
```

## 3. Adversarial
The **Adversary** searches for inputs that "break" the function, forcing the **Generator** to create more robust tests.
```python
def adversarial(source):
    test = gen.generate(source)
    bug = adversary.find_bug(source, test)
    return gen.patch(test, bug)
```

## 4. Self-Healing
A closed-loop system that executes the generated code and uses the compiler/test error to fix itself.
```python
def self_healing(source):
    code = llm.generate(source)
    while error := executor.run(code).error:
        code = llm.fix(code, error)
    return code
```

## 5. Consensus
Generates $N$ independent samples and selects the most consistent logic through a majority vote or judge.
```python
def consensus(source):
    samples = [llm.generate(source) for _ in range(N)]
    return judge.select_most_consistent(samples)
```

## 6. Hybrid
Combines multiple paradigms (e.g., SCoT reasoning with an Actor-Critic loop) for high-stakes generation.

## 7. Swarm
A collaborative group of agents working on the same context without strict hierarchy.
```python
def swarm(source):
    context = {"source": source}
    for agent in agents_pool:
        context = agent.contribute(context)
    return context.final_test
```

## 8. Atomic Swarm
Breaks down the test generation into extremely granular tasks (e.g., one agent only for imports, one for mock objects, one for assertions).
```python
def atomic_swarm(source):
    parts = {"setup": agent_a, "logic": agent_b, "assert": agent_c}
    return merge([a.solve(source) for a in parts.values()])
```

## 9. SOA (Swarm of Agents)
A hierarchical swarm where "Lead" agents coordinate sub-swarms for different modules of the test suite.

## 10. COA (Chain of Agents)
A sequential pipeline where each agent adds a specific layer of quality (e.g., Security -> Performance -> Coverage).
```python
def coa(source):
    return agent_coverage(agent_perf(agent_security(source)))
```

## 11. Competitive
Multiple models generate independent solutions, and a "Referee" model picks the winner based on a scoring rubric.
```python
def competitive(source):
    solutions = [m.generate(source) for m in models]
    return referee.rank_and_pick(solutions)
```
