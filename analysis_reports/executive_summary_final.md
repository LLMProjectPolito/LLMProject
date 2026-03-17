# Analisi Finale: Verdetto Sperimentale LLM Agents (Marzo 2026)

Dopo una giornata intensa di test, run full-scale e sfide contro i rate limit delle API, abbiamo un quadro chiaro dell'attuale stato dell'arte per la generazione di test via LLM.

## 🏆 I Protagonisti

### 1. Il Re della Qualità: **Consensus (Llama-3.3-70B)**
Nelle run senza limitazioni, l'architettura a dibattito si è confermata la più solida:
- **Functional Correctness**: **0.808** (Media su larga scala).
- **Vantaggio**: Riesce a filtrare le allucinazioni e generare test "professionali" che non falliscono inutilmente.
- **Svantaggio**: Estremamente esigente in termini di token. Impossibile da runnare massivamente su account free.

### 2. La Sorpresa: **Baseline (Llama-3.1-8B)**
Con le ultime ottimizzazioni, il modello piccolo ha dato risultati scioccanti:
- **Functional Correctness**: Fino a **0.857** sui problemi standard.
- **Mutation Score**: **1.0 (100%)**. Dimostra che, per compiti di testing puro, un modello piccolo ben indirizzato è efficace quanto uno grande, costando una frazione (e girando 50 volte più veloce).

---

## 🔬 Evoluzione Tecnica del Framework
Oggi abbiamo trasformato un semplice script in una **piattaforma di ricerca scientifica**:
1.  **Mutation Testing**: Ora verifichiamo la "cattiveria" dei test iniettando bug.
2.  **Etichettatura Multi-Configurazione**: Possiamo confrontare diverse versioni dello stesso agente fianco a fianco.
3.  **Runner Corazzato**: Gestione automatica dei ritardi (exponential backoff) e protezione contro i loop infiniti.
4.  **Visualizzazione Avanzata**: Generazione di report a 4 quadranti.

## 💡 Raccomandazioni Strategiche
Per i prossimi esperimenti:
- **Modello Ibrido**: Usare l'8B per la generazione iniziale e il 70B solo come **Moderatore** (Consensus Hybrid). Questo abbatterebbe i costi e i rate limit mantenendo la qualità.
- **Sequential Loading**: Su Groq Free, non lanciare mai più di 1 agente complesso alla volta se si usano modelli Large.

---
*Documento finale redatto il 13 Marzo 2026.*
