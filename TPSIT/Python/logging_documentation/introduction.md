# Introduzione alla Libreria `logging`

La libreria `logging` in Python è come un diario di bordo per i tuoi programmi. Ti consente di registrare ciò che accade durante l'esecuzione del codice, rendendo più facile diagnosticare problemi e monitorare eventi in modo organizzato e professionale.

---

## Perché usare il `logging`?

1. **Debug più semplice**: Aiuta a localizzare i bug e a capire meglio cosa succede nel programma.
2. **Controllo completo**: Monitora lo stato del programma mentre è in esecuzione, anche in tempo reale.
3. **Chiarezza e ordine**: Fornisce un'alternativa più professionale e organizzata rispetto a `print()`.
4. **Adattabilità**: Può essere configurato per script semplici o applicazioni complesse.

---

## Come funziona `logging`?

Ecco i tre elementi chiave del `logging`:

### **Messaggi di log**
Sono informazioni su eventi specifici. Possono includere indicazioni generali, errori o avvisi. Esempi di messaggi:
- "Programma avviato."
- "Attenzione: operazione lenta."
- "Errore: impossibile connettersi al server."

### **Livelli di gravità**
Ogni messaggio di log è classificato in base alla sua importanza:
- `DEBUG`: Dettagli utili per il debugging (per sviluppatori).
- `INFO`: Informazioni generali sul funzionamento del programma.
- `WARNING`: Avvisi su potenziali problemi.
- `ERROR`: Problemi gravi che interrompono alcune funzionalità.
- `CRITICAL`: Errori critici che richiedono attenzione immediata.

### **Destinazioni dei messaggi**
I messaggi di log possono essere inviati a:
- **Console**: Vengono stampati direttamente sullo schermo.
- **File**: Salvati in un file per una revisione futura.
- **Server remoti**: Utilizzati in sistemi distribuiti per monitorare applicazioni.

---

## Esempio rapido: Sostituire `print()` con `logging`

Un confronto tra `print()` e `logging`:

```python
# Con print()
print("Programma avviato.")

# Con logging
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Programma avviato.")
```

## Primi passi con logging
Ecco un piccolo esempio per capire quanto è semplice iniziare:

```python
# Passo 1: Importare la libreria
import logging  # Importa la libreria necessaria per il logging

# Passo 2: Configurare il "diario" di log
logging.basicConfig(level=logging.INFO)  # Configura il livello minimo di log (INFO in questo caso)

# Passo 3: Scrivere messaggi
logging.info("Benvenuto! Questo è il tuo primo messaggio di log.")  # Un messaggio informativo
logging.warning("Attenzione: qualcosa potrebbe non andare.")  # Un avviso per qualcosa di potenzialmente problematico
logging.error("Errore! C'è un problema serio.")  # Segnala un errore critico
```