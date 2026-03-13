# Cross-Model Evolutionary Testing: Semantic Analysis & Mutation Loops

Questo progetto implementa un'architettura multi-agente basata su **LangGraph** per la generazione automatica collaborativa di casi di test (Progetto A1 per il corso LLM for Software Engineering).

Invece di limitarci alla mera misurazione della coverage, utilizziamo **EvalPlus** (un dataset molto severo sui corner cases) e il **Mutation Testing** per valutare l'efficacia dei test case generati.

## Architettura Agenti (Multi-Model):
1. **The Semantic Analyst (Gemini 1.5 Pro)**: Analizza i requisiti estraendo "boundary" e pre/post condizioni.
2. **The Fast Tester (Groq / Llama)**: Genera rapidamente e corregge il codice `pytest`.
3. **The Mutation Auditor (Gemini 1.5 Pro)**: (Opzionale/Avanzato) Analizza i mutanti sopravvissuti per suggerire nuovi test.

## Prossimi passi:
1. Copia `.env.example` in `.env` e inserisci le API keys.
2. Installa le dipendenze: `pip install -r requirements.txt`.
3. Avviare lo script `src/main.py` per un test iniziale.
