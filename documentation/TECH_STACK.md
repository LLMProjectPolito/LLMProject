# 🛠️ Technical Stack & Architecture

## 🚀 Core Technologies
- **Orchestration**: `LangGraph` (Stateful Multi-Agent Workflows) 📈
- **LLM Engine**: `Google Vertex AI` / `Google AI Studio` (Gemma 1.1 Model Registry) 💎
- **Data Engineering**: `Pandas` (Matrix consolidation of 4.400 tasks) 🛡️
- **Evaluation System**: `EvalPlus` (Augmented HumanEval test cases) 🧪

## 🧬 Custom Analysis Engine
We implemented a proprietary **AST-Trace Instrumentation Pipeline** to overcome limitations in standard coverage tools on Windows:
- **`sys.settrace` Integration**: Real-time bytecode execution tracking. 🏹
- **AST Parsing**: Structural logic density and branch point identification. 🏝️
- **Safe Isolation**: Multi-process execution with hardware timeouts to prevent infinite LLM loops. 🛡️

## 🏛️ Project Structure
- `src/agents/`: Logic for 11 distinct agentic workflows (Swarm, CoA, SCA, etc.). 🏘️
- `data/evalplus_subset/`: Curated dataset of 25 Python-logic benchmarks. 🏰
- `documentation/`: Academic reports and PDF thesis materials. 🏟️
