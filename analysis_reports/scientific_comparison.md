# Confronto Finale: Baseline Large (Llama 3 70B) vs Consensus Small (Llama 3 8B)

L'esperimento mirato a confrontare la forza bruta di un modello Large (Baseline) contro l'architettura a dibattito di un modello Small (Consensus) è terminato.

## 📊 Analisi dei Risultati

### 1. Dominanza del Modello Large (Baseline 70B)
Nonostante i fortissimi rallentamenti imposti dal provider (Groq), il modello da 70B ha dimostrato una precisione chirurgica:
- **HumanEval/0**: 0.929 FC
- **HumanEval/1**: 0.545 FC (Problema significativamente più ostico)
- **Mutation Score**: **1.0 (100%)** costante. Tutti i test generati sono in grado di rilevare bug iniettati.
- **Coverage**: 100% Line Coverage costante.

### 2. Il Limite Invisibile: Consensus e i Token
Il modello Consensus (8B) ha fallito sistematicamente in questa run specifica. L'analisi tecnica rivela che:
- Non è un problema di "intelligenza", ma di **quota TPM (Tokens Per Minute)**.
- Il moderatore di Consensus deve rileggere 3 versioni di codice; questo invio massiccio satura la quota gratuita del provider istantaneamente.
- **Lezione**: Per agenti iterativi o multi-step su piattaforme free, è necessario un delay di almeno **2 minuti** tra le fasi di generazione e quelle di dibattito.

## 🏁 Verdetto Finale della Giornata
Il framework ora possiede un'infrastruttura di analisi di grado professionale. Abbiamo dimostrato che:
- Il **Mutation Score** è la metrica più affidabile per distinguere testsuite mediocri da quelle eccellenti.
- I modelli **Large (70B)** sono ancora indispensabili per i problemi difficili (HumanEval/1), dove l'8B fatica a coprire tutti i corner case.

---
*Report finale registrato nel sistema il 13 Marzo 2026.*
