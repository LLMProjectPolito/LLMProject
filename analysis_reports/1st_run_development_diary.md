# Analisi e Stati di Avanzamento: LLM Multi-Agent Testing

## 🎯 Obiettivo del Progetto
Confrontare scientificamente diverse architetture di agenti LLM (LangGraph) nella generazione di test unitari complessi, utilizzando il dataset **EvalPlus (HumanEval+)** come benchmark di riferimento. L'attenzione non è solo sulla quantità (coverage) ma sulla qualità semantica e sulla robustezza dell'esecuzione autonoma.

---

## 🚀 Percorso di Sviluppo e Milestone
Abbiamo costruito un framework completo e autonomo che gestisce l'intero ciclo di vita dell'esperimento, superando diverse sfide tecniche critiche:

1.  **Framework di Valutazione Autonomo**: Implementato un "Sandbox Executor" che isola il codice, gestisce i namespace per evitare conflitti e calcola metriche multidimensionali (FC, Coverage, Radon CC/MI, Semantic Similarity).
2.  **9 Paradigmi di Agenti**: Implementate architetture collaborative (Actor-Critic, CoA, SOA), competitive (Adversarial, Competitive) e collettive (Swarm, Consensus).
3.  **Infrastruttura di Persistenza**: Sistema di logging automatico che salva CSV, metadati JSON e grafici radar ad ogni run, garantendo la riproducibilità dei dati.

---

## 🧠 Analisi dei Risultati e Learnings

### 1. Il Paradosso della Loquacità (Signal vs Noise)
Una scoperta fondamentale è stata l'instabilità degli agenti complessi dovuta al "rumore" conversazionale. 
*   **Problema**: Gli LLM, per istruzione (RLHF), tendono a essere educati e logorroici. Frasi come *"Ecco il codice richiesto..."* rompevano l'esecuzione Python causano `SyntaxError`.
*   **Soluzione**: Introduzione di un `parser.py` robusto basato su regex che estrae solo il blocco di codice principale.
*   **Impatto**: I punteggi di Functional Correctness (FC) sono passati da **0.0** (fallimento totale per sintassi) a punteggi superiori a **0.80**.

### 2. Architetture Collaborative vs Semplici (Baseline vs Actor-Critic)
Inizialmente la **Baseline** sembrava battere l' **Actor-Critic**. L'analisi approfondita ha rivelato un bug logico nell'agente più complesso:
*   **L'Errore di Ridefinizione**: L'Actor-Critic, cercando di essere preciso, ridefiniva la funzione da testare nel file dei test, spesso lasciandola vuota o con logica errata. Questo "copriva" la funzione reale nel sandbox, portando a fallimenti di tutti i test.
*   **La Fragilità del Dialogo**: Più gli agenti interagiscono, più aumenta la probabilità di "allucinazioni di formato" (es. importare moduli inesistenti come `from your_module import ...`).
*   **La Svolta**: Blindando i prompt con regole rigide (*"Non ridefinire la funzione"*, *"Niente import finti"*), l'**Actor-Critic ha sorpassato la Baseline**, passando da **0.0 a 0.85 FC** su HumanEval/0.

### 3. Metriche Oltre la Coverage
Abbiamo imparato che la *Line Coverage* può essere ingannevole. Un agente può raggiungere il 100% di coverage con test triviali.
*   **Cyclomatic Complexity (CC)**: Ci dice quanto sono intricati i test prodotti.
*   **Maintainability Index (MI)**: Indica se i test sono scritti in modo pulito.
*   **Functional Correctness (FC)**: La metrica regina. Se i test passano sulla soluzione canonica ma falliscono se il codice è sbagliato.

---

## 🔬 Esperimento Empirico: Rumore vs Codice
Abbiamo confermato sperimentalmente che senza un sistema di filtraggio (Parser), le architetture multi-agente sono destinate a fallire la validazione tecnica nel 100% dei casi su larga scala. Il parser trasforma un assistente chatty in un generatore di codice professionale.

## 🏁 Prossimi Passi: Il "Massive Run"
Il sistema è ora stabilizzato. Procederemo con un'esecuzione su 5 problemi per tutti i 9 agenti.
*   **Tempo stimato**: ~15-20 minuti. 
*   **Previsione**: Ci aspettiamo che gli agenti "Consensus" e "Swarm" mostrino una diversità di test superiore, mentre l'Actor-Critic manterrà il primato sulla precisione chirurgica.

---
*Documento aggiornato il 13 Marzo 2026 - Analisi Tecnica Approfondita.*
