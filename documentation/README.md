# 🤖 Project A1: EvalPlus Agentic Framework

Un framework avanzato per testare e confrontare architetture di agenti LLM sul benchmark **HumanEval+**. Il progetto dimostra come architetture intelligenti possano portare modelli piccoli (8B) a performance competitive con modelli giganti (70B).

---

## 🏗️ Struttura del Progetto

### 📂 Root Directory
*   `experiment_runner.py`: Il cuore del progetto. Gestisce l'esecuzione parallela (fino a 10 thread), i rate limit delle API e il salvataggio automatico dei risultati in CSV.
*   `requirements.txt`: Dipendenze (LangGraph, Radon, Pytest, LangChain).
*   `.env`: Chiavi API (Groq, Cerebras, OpenRouter).

### 📂 `src/agents/` (Le Architetture Core)
Ogni file implementa una diversa strategia di collaborazione tra agenti:
*   `baseline.py`: Chiamata singola diretta.
*   `actor_critic.py`: Un **Driver** scrive il codice e un **Navigator** fornisce feedback per migliorarlo (loop iterativo).
*   `swarm.py`: Più **Worker** generano test indipendenti che vengono poi fusi da un **Aggregator**.
*   `adversarial.py`: Un **Hacker** inserisce bug nel codice e un **Tester** deve scrivere test capaci di trovarli.
*   `hybrid.py`: Approccio evolutivo che genera una popolazione di test e li fonde geneticamente.

### 📂 `src/utils/` (Utility di Sistema)
*   `prompts.py`: Contiene la logica dei **Reasoning Styles**. Modularizza il "modo di pensare" degli agenti.
*   `model_registry.py`: Gestisce i provider (Groq, Cerebras, etc.) con un sistema di **fallback automatico**.
*   `executor.py`: Esegue i test tramite `pytest` in ambiente protetto (con timeout anti-loop) e calcola le metriche Radon.
*   `parser.py`: Estrae in modo robusto il codice Python dai blocchi Markdown degli LLM.

---

## 🧠 Reasoning Styles
Il framework permette di iniettare diversi stili di ragionamento in qualunque architettura:

1.  **Zero-Shot (`zero_shot`)**: Risposta diretta, massima velocità.
2.  **Chain of Thought (`cot`)**: Il modello ragiona ad alta voce sui casi limite prima di scrivere il codice.
3.  **Structured CoT (`scot`)**: Ragionamento diviso in fasi rigide (Analisi, Piano, Codice).
4.  **Few-Shot (`few_shot`)**: Apprendimento contestuale tramite esempi di alta qualità.

---

## 🚀 Come Eseguire gli Esperimenti

La sintassi è modulare: `--agents agente:stile:modello`

### Esempi di comandi:

**Run Standard (8B CoT)**
```bash
python experiment_runner.py --agents baseline:cot:llama3-8b --n 10
```

**Run Complessa (Swarm con Ragionamento)**
```bash
python experiment_runner.py --agents swarm:cot:llama3-8b --n 5
```

**Confronto Scientifico (8B vs 70B)**
```bash
python experiment_runner.py --agents baseline:70b baseline:cot:8b --n 20
```

---

## 📊 Metriche calcolate
Per ogni run, il sistema genera automaticamente un report con:
*   **Functional Correctness**: Quanti test passano.
*   **Line/Branch Coverage**: Quanto è profondo il test.
*   **Radon Metrics**: Complessità Ciclomatica e Manutenibilità del codice generato.
*   **Token Usage**: Analisi dei costi e dell'efficienza.

*   `model_registry.py`: Gestisce i provider (Google Gemini, Groq, Cerebras, etc.) con supporto nativo per **Gemma 3 (1B/4B/12B/27B)**.

---

*Ultimo aggiornamento: 17/03/2026*
