# Future Commands Plan (Gemma 3 & Heavyweights)

This report outlines the next phases for the agentic evaluation matrix. 
**Note**: All runs use the corrected `experiment_runner.py` with 100% Lazy Loading and Google GenAI SDK (v2).

## 1. Small Gemma 3 Matrix (RUNNING NOW)
**Models**: Gemma-3 1B, 4B (All 10 Agents x 4 Prompts = 80 combinations)
**Problems**: HumanEval/139-163 (25 problems)
```bash
python -u experiment_runner.py --start 139 --n 25 --agents baseline:gemma-1b:zero_shot baseline:gemma-1b:cot baseline:gemma-1b:scot baseline:gemma-1b:few_shot actor_critic:gemma-1b:zero_shot actor_critic:gemma-1b:cot actor_critic:gemma-1b:scot actor_critic:gemma-1b:few_shot adversarial:gemma-1b:zero_shot adversarial:gemma-1b:cot adversarial:gemma-1b:scot adversarial:gemma-1b:few_shot swarm:gemma-1b:zero_shot swarm:gemma-1b:cot swarm:gemma-1b:scot swarm:gemma-1b:few_shot self_healing:gemma-1b:zero_shot self_healing:gemma-1b:cot self_healing:gemma-1b:scot self_healing:gemma-1b:few_shot coa:gemma-1b:zero_shot coa:gemma-1b:cot coa:gemma-1b:scot coa:gemma-1b:few_shot soa:gemma-1b:zero_shot soa:gemma-1b:cot soa:gemma-1b:scot soa:gemma-1b:few_shot consensus:gemma-1b:zero_shot consensus:gemma-1b:cot consensus:gemma-1b:scot consensus:gemma-1b:few_shot atomic_swarm:gemma-1b:zero_shot atomic_swarm:gemma-1b:cot atomic_swarm:gemma-1b:scot atomic_swarm:gemma-1b:few_shot hybrid:gemma-1b:zero_shot hybrid:gemma-1b:cot hybrid:gemma-1b:scot hybrid:gemma-1b:few_shot baseline:gemma-4b:zero_shot baseline:gemma-4b:cot baseline:gemma-4b:scot baseline:gemma-4b:few_shot actor_critic:gemma-4b:zero_shot actor_critic:gemma-4b:cot actor_critic:gemma-4b:scot actor_critic:gemma-4b:few_shot adversarial:gemma-4b:zero_shot adversarial:gemma-4b:cot adversarial:gemma-4b:scot adversarial:gemma-4b:few_shot swarm:gemma-4b:zero_shot swarm:gemma-4b:cot swarm:gemma-4b:scot swarm:gemma-4b:few_shot self_healing:gemma-4b:zero_shot self_healing:gemma-4b:cot self_healing:gemma-4b:scot self_healing:gemma-4b:few_shot coa:gemma-4b:zero_shot coa:gemma-4b:cot coa:gemma-4b:few_shot coa:gemma-4b:scot soa:gemma-4b:zero_shot soa:gemma-4b:cot soa:gemma-4b:scot soa:gemma-4b:few_shot consensus:gemma-4b:zero_shot consensus:gemma-4b:cot consensus:gemma-4b:scot consensus:gemma-4b:few_shot atomic_swarm:gemma-4b:zero_shot atomic_swarm:gemma-4b:cot atomic_swarm:gemma-4b:few_shot atomic_swarm:gemma-4b:scot hybrid:gemma-4b:zero_shot hybrid:gemma-4b:cot hybrid:gemma-4b:scot hybrid:gemma-4b:few_shot
```

## 2. Large Gemma 3 Matrix (NEXT STEP)
**Models**: Gemma-3 12B, 27B (All 10 Agents x 4 Prompts = 80 combinations)
```bash
python -u experiment_runner.py --start 139 --n 25 --agents baseline:gemma-12b:zero_shot baseline:gemma-12b:cot baseline:gemma-12b:scot baseline:gemma-12b:few_shot actor_critic:gemma-12b:zero_shot actor_critic:gemma-12b:cot actor_critic:gemma-12b:scot actor_critic:gemma-12b:few_shot adversarial:gemma-12b:zero_shot adversarial:gemma-12b:cot adversarial:gemma-12b:scot adversarial:gemma-12b:few_shot swarm:gemma-12b:zero_shot swarm:gemma-12b:cot swarm:gemma-12b:scot swarm:gemma-12b:few_shot self_healing:gemma-12b:zero_shot self_healing:gemma-12b:cot self_healing:gemma-12b:scot self_healing:gemma-12b:few_shot coa:gemma-12b:zero_shot coa:gemma-12b:cot coa:gemma-12b:scot coa:gemma-12b:few_shot soa:gemma-12b:zero_shot soa:gemma-12b:cot soa:gemma-12b:scot soa:gemma-12b:few_shot consensus:gemma-12b:zero_shot consensus:gemma-12b:cot consensus:gemma-12b:scot consensus:gemma-12b:few_shot atomic_swarm:gemma-12b:zero_shot atomic_swarm:gemma-12b:cot atomic_swarm:gemma-12b:scot atomic_swarm:gemma-12b:few_shot hybrid:gemma-12b:zero_shot hybrid:gemma-12b:cot hybrid:gemma-12b:scot hybrid:gemma-12b:few_shot baseline:gemma-27b:zero_shot baseline:gemma-27b:cot baseline:gemma-27b:scot baseline:gemma-27b:few_shot actor_critic:gemma-27b:zero_shot actor_critic:gemma-27b:cot actor_critic:gemma-27b:scot actor_critic:gemma-27b:few_shot adversarial:gemma-27b:zero_shot adversarial:gemma-27b:cot adversarial:gemma-27b:scot adversarial:gemma-27b:few_shot swarm:gemma-27b:zero_shot swarm:gemma-27b:cot swarm:gemma-27b:scot swarm:gemma-27b:few_shot self_healing:gemma-27b:zero_shot self_healing:gemma-27b:cot self_healing:gemma-27b:scot self_healing:gemma-27b:few_shot coa:gemma-27b:zero_shot coa:gemma-27b:cot coa:gemma-27b:scot coa:gemma-27b:few_shot soa:gemma-27b:zero_shot soa:gemma-27b:cot soa:gemma-27b:scot soa:gemma-27b:few_shot consensus:gemma-27b:zero_shot consensus:gemma-27b:cot consensus:gemma-27b:scot consensus:gemma-27b:few_shot atomic_swarm:gemma-27b:zero_shot atomic_swarm:gemma-27b:cot atomic_swarm:gemma-27b:scot atomic_swarm:gemma-27b:few_shot hybrid:gemma-27b:zero_shot hybrid:gemma-27b:cot hybrid:gemma-27b:scot hybrid:gemma-27b:few_shot
```

## 3. Llama-70B & Multi-Model Synergies
**Models**: Llama-70B, Hybrid/Synergy versions with Gemma-27B. 
Skipping identified failures (weak agents/prompts from previous rounds).
```bash
python -u experiment_runner.py --start 139 --n 25 --agents baseline:llama-70b:zero_shot actor_critic:llama-70b:zero_shot swarm:llama-70b:zero_shot self_healing:llama-70b:zero_shot actor_critic:llama-70b/gemma-27b:zero_shot swarm:llama-70b/gemma-27b:zero_shot consensus:llama-70b/gemma-27b:zero_shot coa:llama-70b/gemma-27b:zero_shot
```

## 4. GPT-OSS 120B High-End Matrix
**Models**: Chatgpt-oss (120B), combined architectures with Gemma-27B.
Focusing on stability and maximum accuracy.
```bash
python -u experiment_runner.py --start 139 --n 25 --agents baseline:chatgpt-oss:zero_shot actor_critic:chatgpt-oss:zero_shot self_healing:chatgpt-oss:zero_shot actor_critic:chatgpt-oss/gemma-27b:zero_shot swarm:chatgpt-oss/gemma-27b:zero_shot consensus:chatgpt-oss/gemma-27b:zero_shot
```
