# 🎯 Project Finale: Implementation Roadmap

Questo documento delinea la strategia finale per chiudere il progetto con risultati scientificamente inattaccabili. Abbiamo trasformato il framework in un sistema modulare dove **Architettura** e **Reasoning** sono ora mattoncini indipendenti.

---

## 🏗️ Stato Attuale degli Agenti
Il framework include **11 architetture diverse**, ma per la fase finale ci concentriamo sulle **5 più promettenti**. Ecco la tassonomia completa e il motivo della selezione.

### 🔝 Gli "Essential 5" (Priorità Alta)
Questi agenti hanno dimostrato il miglior rapporto qualità/prezzo/stabilità:
1.  **`baseline`**: Indispensabile come controllo scientifico (standard di riferimento).
2.  **`swarm`**: Fondamentale per la diversity. Più agenti che coprono diversi rami del codice.
3.  **`actor_critic`**: Il cuore dell'ottimizzazione iterativa. Correzione degli errori in tempo reale.
4.  **`adversarial`**: La nostra "arma segreta" per la robustezza (Red Team vs Blue Team).
5.  **`hybrid`**: Il più avanzato, usa logica genetica per fondere il meglio di più mondi.

### 📦 Gli Agenti "Shelved" (Scartati/Archiviati)
Questi agenti sono implementati ma esclusi dalle run finali per motivi tecnici specifici:
6.  **`competitive`**: Simile allo Swarm, ma meno efficiente. Lo Swarm con `Aggregator` produce risultati migliori rispetto alla pura competizione.
7.  **`coa` (Chain of Agents)**: Troppo lineare. Se un agente della catena sbaglia, l'errore si propaga. `Actor-Critic` è una versione superiore perché ha feedback.
8.  **`soa` (Select of Agents)**: Molto dipendente dalla qualità dell'Orchestratore. Su modelli 8B, l'orchestratore spesso sceglie male.
9.  **`consensus`**: Richiede troppe chiamate (Debate) e spesso finisce in loop infiniti o consuma troppi token senza un reale guadagno rispetto all'Hybrid.
10. **`self_healing`**: Già integrato implicitamente nell' `Actor-Critic`. Avere un file separato è ridondante.
11. **`atomic_swarm`**: Una versione "micro" dello Swarm. Abbiamo preferito potenziare lo `Swarm` principale rendendolo modulare.

### 🧠 Stili di Ragionamento (Applicabili a tutti i nodi)
*   **`zero_shot`**: Risposta diretta.
*   **`cot`**: Chain of Thought (Ragionamento libero).
*   **`scot`**: Structured CoT (Step 1, Step 2, Step 3).
*   **`few_shot`**: Apprendimento tramite esempi.

---

## 🧹 Pulizia: Run Eliminate
Ho deciso di eliminare le seguenti combinazioni perché i dati precedenti hanno dimostrato la loro inefficienza:
*   ❌ **Tutto quello che usa SCoT su 8B**: Troppo pesante, i modelli piccoli si "perdono" nella struttura.
*   ❌ **Consistency (8B) semplice**: Sostituito da **Hybrid**, che è una forma di consistency molto più potente ed evolutiva.
*   ❌ **Few-Shot base**: Spesso meno efficace di un buon CoT e consuma più token per gli esempi fissi.

---

## 🚀 Le "Final Boss" Runs (Piano d'Azione)

Queste sono le 3 run conclusive che genereranno i dati per il tuo report finale.

### Run A: The Reasoning Showdown (Precisione Pura)
*Obiettivo*: Vedere se l'A-C o l'Hybrid riescono ad azzerare il gap con il 70B usando il CoT.
`python experiment_runner.py --agents baseline:70b baseline:cot:8b actor_critic:cot:8b hybrid:cot:8b --n 20`

### Run B: The Swarm Evolution (Copertura Massima)
*Obiettivo*: Testare se lo Swarm (più teste) batte il CoT (una testa pensante) sui problemi di coverage.
`python experiment_runner.py --agents baseline:cot:8b swarm:8b swarm:cot:8b --n 20`

### Run C: The Adversarial Stress-Test (Robustezza)
*Obiettivo*: Chiedere all'agente Adversarial di scovare i bug che il 70B non vede.
`python experiment_runner.py --agents baseline:70b adversarial:cot:8b --n 20`

---

## 🧪 Test di Modularità (In corso...)
Sto lanciando un test rapido su 2 problemi per confermare che il sistema carichi correttamente gli stili:
`python experiment_runner.py --agents swarm:cot:8b actor_critic:cot:8b baseline:cot:8b --n 2`

---
*Piano aggiornato al 15/03/2026 - Il framework è ora pronto per la gloria.*
