# Livelli di Logging

La libreria `logging` in Python utilizza livelli predefiniti per indicare l'importanza o la gravità dei messaggi di log. Questi livelli sono utili per classificare e filtrare i messaggi durante l'esecuzione del programma.

---

## Livelli Principali

1. **DEBUG**: Informazioni dettagliate, utili principalmente per il debugging.
2. **INFO**: Conferma che il programma sta funzionando come previsto.
3. **WARNING**: Indicazioni di potenziali problemi o situazioni inattese.
4. **ERROR**: Errori che impediscono l'esecuzione corretta di una parte del programma.
5. **CRITICAL**: Errori gravi che richiedono un intervento immediato.

---

## Come Impostare il Livello di Logging

Ecco un esempio pratico per configurare il livello di logging e filtrare i messaggi:

```python
import logging

# Configurazione del logging: Mostra solo WARNING e messaggi più gravi
logging.basicConfig(level=logging.WARNING)

# Messaggi di esempio
logging.debug("Questo messaggio non sarà visualizzato.")  # Non appare a causa del livello impostato
logging.info("Nemmeno questo.")  # Ignorato per lo stesso motivo
logging.warning("Attenzione: livello di logging attivato.")  # Viene visualizzato
logging.error("Errore rilevato nel sistema!")  # Viene visualizzato
logging.critical("Errore critico! Intervento immediato richiesto!")  # Viene visualizzato
```

## Spiegazione dell'Esempio

### Livello di Logging
- **`level=logging.WARNING`**: Configura il livello minimo di logging a `WARNING`. I messaggi di livello `DEBUG` e `INFO` non verranno mostrati.

---

### Messaggi di Log
- **`logging.debug("...")`**: Ignorato perché è sotto il livello configurato.
- **`logging.info("...")`**: Ignorato per lo stesso motivo.
- **`logging.warning("...")`**: Visualizzato perché corrisponde al livello configurato.
- **`logging.error("...")`**: Visualizzato perché è di livello superiore.
- **`logging.critical("...")`**: Visualizzato perché è il livello più alto di gravità.

---

### Conclusione
I livelli di logging consentono di:
1. **Filtrare i messaggi** per concentrarsi solo su ciò che è importante.
2. **Personalizzare il comportamento** del programma in base alle esigenze di monitoraggio.
3. **Identificare rapidamente problemi** grazie alla classificazione delle gravità.