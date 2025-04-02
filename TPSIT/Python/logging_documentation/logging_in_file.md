# Logging in File

Salvare i messaggi di log in un file è una pratica essenziale per monitorare eventi nel tempo. Questo approccio consente di:
- Analizzare i comportamenti del programma.
- Tracciare errori.
- Archiviare informazioni utili per il debugging o la gestione operativa.

---

## Configurare il Logging in File

Ecco un esempio pratico su come configurare il logging per salvare i messaggi in un file:

```python
import logging

# Configurazione del logging
logging.basicConfig(
    filename='app.log',  # Nome del file in cui salvare i log
    filemode='a',  # Modalità 'append' per aggiungere i messaggi al file esistente
    level=logging.INFO,  # Livello minimo di severità
    format='%(asctime)s - %(levelname)s - %(message)s'  # Formato dei messaggi
)

# Scrittura di messaggi nel file di log
logging.info("Messaggio registrato nel file.")
logging.error("Errore registrato nel file.")
```

## Spiegazione dell'Esempio

### **1. Configurazione del Logging**
- **`filename='app.log'`**: Specifica il nome del file in cui i log saranno salvati.
- **`filemode='a'`**: Utilizza la modalità "append" per aggiungere i nuovi messaggi al file esistente senza sovrascriverlo.
- **`level=logging.INFO`**: Imposta il livello minimo di severità a `INFO`, registrando tutti i messaggi di livello `INFO` e superiori.
- **`format='%(asctime)s - %(levelname)s - %(message)s'`**: Definisce il formato dei messaggi includendo:
  - **`%(asctime)s`**: Il timestamp del messaggio.
  - **`%(levelname)s`**: Il livello di gravità del messaggio (`INFO`, `ERROR`, ecc.).
  - **`%(message)s`**: Il contenuto del messaggio.

---

### **2. Scrittura di Messaggi**
- **`logging.info("Messaggio registrato nel file.")`**: Registra un messaggio informativo nel file.
- **`logging.error("Errore registrato nel file.")`**: Registra un messaggio di errore nel file.

---

### **Conclusione**
Salvare i log in un file offre numerosi vantaggi, tra cui:
1. **Analisi degli errori**: Facilita il debug grazie alla cronologia dei messaggi.
2. **Monitoraggio continuo**: Permette di verificare il comportamento del programma nel tempo.
3. **Gestione operativa**: Fornisce un registro documentato per tracciare eventi importanti.