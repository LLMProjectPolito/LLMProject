# Analisi del Confronto Scientifico: Small (8B) vs Large (70B)

In questa run abbiamo cercato di effettuare un confronto "testa a testa" tra modelli piccoli e grandi, testando contemporaneamente le nuove metriche (Mutation Score, Branch Coverage).

## ⚠️ Nota Tecnica: Rate Limiting
La run è terminata prematuramente con errori **429 (Rate Limit Exceeded)** da parte di Groq. 
Lanciare contemporaneamente 4 configurazioni (Baseline e Consensus sia in Small che in Large) ha saturato istantaneamente la soglia di token al minuto permessa. 

### Risultati Parziali Rilevati:
Per l'unico problema completato prima del crash (**HumanEval/0**):
- **Baseline (Small/8B)**: Ha ottenuto un ottimo **0.917** di correttezza funzionale iniziale, ma con un tempo di esecuzione di 3.75s.
- **Tutti gli altri**: Falliti per errori di rete/quota.

## 🛠️ Cosa abbiamo testato con successo
Nonostante i limiti dell'API, il sistema ha dimostrato che:
1.  **Le Etichette Funzionano**: Il CSV ora separa correttamente `agent` (es. `baseline`) da `config_label` (es. `small`).
2.  **Report Grafico V2**: Il sistema ha generato un report a 4 quadranti (sebbene con dati incompleti causa errori).
3.  **Nuove Metriche**: Branch coverage e Mutation score sono stati iniettati correttamente nella logica.

## 💡 Strategia per la Run Correttiva
Per avere dati reali senza crash:
- **Ridurre il parallelismo**: Non lanciare tutti e 4 insieme, ma uno alla volta.
- **Aggiungere un delay**: Inserire un piccolo `time.sleep()` tra un'agente e l'altro nel loop di `experiment_runner.py`.

---
*Documento generato il 13 Marzo 2026.*
