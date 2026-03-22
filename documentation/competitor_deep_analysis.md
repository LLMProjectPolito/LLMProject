# 🕵️‍♂️ Analisi Approfondita dei Competitors

Questo documento analizza le performance e le strategie dei gruppi rivali (Group 1 e Group 14) per evidenziare i punti di forza del nostro framework.

---

### 🟢 Group 1: 30LLM (Multi-Agent for Collaborative Testing)
**Benchmark**: HumanEval Standard | **Modello**: Nemotron 30B

| Strategia | Baseline (Zero-Shot) | Approccio Agentico (QA Agent) | Miglioramento |
| :--- | :--- | :--- | :--- |
| **Standard** | 48.66% | 71.76% | +23.1% |
| **Augmented** (Prompt Opt) | 98.48%* | 100.00%* | +1.52% |

**Analisi Critica**:
*   **L'Inganno del Prompt**: Il loro salto enorme (da 48% a 100%) è dovuto quasi interamente al passaggio da un prompt "base" a un prompt "ottimizzato" (Augmented Few-Shot). L'architettura multi-agente in sé ha aggiunto meno del 2% di valore.
*   **Modello**: Usano un **30B**. Il fatto che noi otteniamo risultati simili con un **8B** dimostra che il nostro approccio di ragionamento (CoT) è molto più efficiente.
*   **Benchmark**: HumanEval standard è ormai "risolto" da molti modelli per memoria. La mancanza di test extra (che noi abbiamo in Eval+) rende i loro 100% meno affidabili dei nostri 80%.

---

### 🔴 Group 14: Collaborative & Competitive Loops
**Benchmark**: Custom (6 Classi Python scolastiche) | **Modello**: GPT-OSS 120B / Llama 70B

| Strategia | Baseline (Zero-Shot) | Approccio Agentico | Consumo Token |
| :--- | :--- | :--- | :--- |
| **Single Agent** | 92.00% (Coverage) | - | 1.3k |
| **Collaborative** | - | 94.00% (Mutation Score) | 12.3k |

**Analisi Critica**:
*   **Efficienza Disastrosa**: Per ottenere un miglioramento minimo (+2% in mutation score), il loro sistema consuma **10 volte più token** della baseline. Questo è l'opposto dell'ottimizzazione.
*   **Saturazione**: Hanno scelto problemi troppo semplici. Se la baseline è già al 92%, non c'è spazio per dimostrare la superiorità degli agenti. È un errore di design sperimentale.
*   **Confusione Cognitiva**: Sui problemi più complessi del loro set, l'approccio agentico ha ottenuto risultati **peggiori** della baseline (79% vs 85%), dimostrando che troppi agenti senza una logica di ragionamento (come il CoT) portano solo rumore.

---

### 🏆 Confronto Finale vs Project A1 (Noi)

1.  **Benchmarking Rigoroso**: Noi usiamo **HumanEval+** (Subset Hard). Ogni nostra funzione ha 80+ test case. Loro ne hanno 3 o 4. Il nostro 80% è "reale", il loro 100% è spesso superficiale.
2.  **Hardware Efficiency**: Noi scaliamo verso il basso (**8B, 3B e persino 1B**). Loro scalano verso l'alto (30B, 70B, 120B). La nostra sfida è far diventare intelligente un modello piccolo, la loro è far parlare modelli enormi già intelligenti di per sé.
3.  **Modularità**: Noi possiamo attivare/disattivare il ragionamento (CoT) su ogni architettura. Loro hanno architetture "fisse" che non sanno adattarsi alla complessità del problema.

*Conclusioni: Il nostro approccio è scientificamente più avanzato perché separa il Ragionamento (Reasoning) dall'Organizzazione (Architecture), permettendo di vincere dove la forza bruta fallisce.*
