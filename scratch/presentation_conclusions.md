# Conclusioni per la Presentazione Progetto A1
**Progetto**: LLM Agents for Collaborative Test Case Generation

## Slide 3: Prompting Techniques Comparison
*   **Structured Chain of Thought (SCoT)**: Risulta la tecnica più efficace e stabile. Aiuta il modello a non "perdersi" in ragionamenti circolari, imponendo una struttura logica (es. Analisi -> Requisiti -> Implementazione Test).
*   **Few-Shot**: Fondamentale per i modelli più piccoli (1b, 4b) per fornire il contesto necessario. Nei modelli grandi (31b) il guadagno è marginale rispetto a Zero-Shot.
*   **Zero-Shot**: Il baseline. Spesso superato del 10-20% dalle tecniche agentiche, confermando che la collaborazione tra agenti aggiunge valore reale.
*   **CoT (standard)**: Sorprendentemente meno efficace di SCoT, talvolta degradando le performance se il modello "allucina" passaggi intermedi.

## Slide 4-7: Agents Architecture & Roles
### 1. Actor-Critic
*   **Ruolo Actor**: Genera il test case iniziale basandosi sul codice sorgente.
*   **Ruolo Critic**: Esegue una "peer review" statica, controllando la sintassi e la pertinenza dei test.
*   **Pseudocodice**:
    ```python
    test = Actor.generate(source_code)
    feedback = Critic.review(test)
    if feedback.has_issues:
        refined_test = Actor.refine(test, feedback)
    ```

### 2. Adversarial
*   **Ruolo Generator**: Crea test per far passare il codice.
*   **Ruolo Adversary**: Cerca di generare input che facciano fallire il codice o rivelino bug (Edge Cases).
*   **Obiettivo**: Massimizzare la robustezza dei test generati.

### 3. Hybrid / Swarm
*   **Architettura**: Pipeline modulare dove più agenti specializzati (es. uno per gli edge cases, uno per il path coverage) collaborano.
*   **Risultato**: È la configurazione che ha portato Gemma-31b al top della correttezza (0.97).

## Slide 8-15: Results Analysis
### Modelli Top (Vincitori)
*   **Gemma-31b**: Il "King" della correttezza funzionale (0.976). Ideale per generazioni critiche dove la precisione è tutto.
*   **Gemma-4-26b**: Il miglior bilanciamento. Ottiene 0.90 di correttezza ma con il **96.3% di Code Coverage**, rendendolo il migliore per testare codice complesso in modo esaustivo.
*   **Gemma-27b**: Il campione di efficienza. Ottimo rapporto performance/token.

### Casi Critici (Regresioni)
*   **Gemma-4-4b**: Ha mostrato cali drastici (-73% in `baseline+scot`) rispetto alla versione precedente (Gemma-4b). Possibile causa: i nuovi pesi potrebbero essere meno ricettivi a prompt strutturati molto rigidi, preferendo istruzioni più dirette.

### Metriche Chiave
*   **Functional Correctness**: Sale significativamente con architetture multi-agente.
*   **Code Coverage**: Gli agenti specializzati (es. Hybrid) riescono a coprire rami di codice che il baseline ignora.
*   **Efficiency**: L'uso di agenti aumenta il consumo di token (specialmente in Gemma-4-26b), ma il guadagno in qualità giustifica il costo.

## Conclusioni Finali
1.  **La collaborazione paga**: Le architetture multi-agente superano sistematicamente il singolo prompt.
2.  **SCoT è lo standard**: Per la generazione di test, una struttura di pensiero guidata è superiore al ragionamento libero.
3.  **Il modello conta**: Non sempre la versione più nuova è migliore per ogni task (vedi caso 4-4b), la scelta del modello deve essere validata empiricamente.
