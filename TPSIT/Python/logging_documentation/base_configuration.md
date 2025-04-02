# Configurazione Base del Logging in Python

Il modulo `logging` di Python consente di tracciare eventi durante l'esecuzione di un programma. La configurazione iniziale può essere realizzata facilmente con `logging.basicConfig`.

---

## Parametri Principali di `basicConfig`

### **`level`**
Definisce il livello minimo di severità dei messaggi da registrare. I livelli disponibili sono:
- **`DEBUG`**: Informazioni dettagliate, usato principalmente per il debugging.
- **`INFO`**: Messaggi generali di funzionamento.
- **`WARNING`**: Avvisi su potenziali problemi.
- **`ERROR`**: Errori che interrompono il corretto funzionamento.
- **`CRITICAL`**: Errori gravi che richiedono attenzione immediata.

### **`format`**
Specifica il formato del messaggio di log utilizzando stringhe di formattazione. Placeholder utili:
- **`%(asctime)s`**: Timestamp del log (quando è stato generato il messaggio).
- **`%(levelname)s`**: Livello di severità (DEBUG, INFO, ecc.).
- **`%(message)s`**: Il contenuto del messaggio di log.
- **`%(name)s`**: Nome del logger utilizzato.
- **`%(module)s`**: Nome del modulo Python che ha generato il messaggio di log.

### **`filename`** *(opzionale)*
Specifica un file in cui salvare i messaggi di log. Se non impostato, i messaggi saranno visualizzati sulla console.

### **`filemode`** *(opzionale)*
Determina come il file sarà aperto:
- `'w'`: Sovrascrive il file ad ogni esecuzione.
- `'a'`: Aggiunge i nuovi messaggi alla fine del file.

---

## Esempio di Implementazione

Di seguito un esempio pratico di configurazione e utilizzo del logging:

```python
import logging

# Configurazione di base
logging.basicConfig(
    level=logging.DEBUG,  # Livello minimo di severità
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  # Formato del log
    filename='app.log',  # Salva i log in un file
    filemode='w'  # Sovrascrive il file ad ogni esecuzione
)

# Esempio di messaggi di log
logging.debug("Questo è un messaggio di debug.")  # Informazioni utili per il debugging
logging.info("Questo è un messaggio informativo.")  # Informazioni generali sul funzionamento
logging.warning("Questo è un avviso.")  # Segnalazioni su possibili problemi
logging.error("Questo è un errore.")  # Messaggi di errore
logging.critical("Questo è un errore critico.")  # Errori che richiedono attenzione immediata
```

## Spiegazione dell'Esempio

### Configurazione di Base

- **`level=logging.DEBUG`**: Registra tutti i messaggi dal livello `DEBUG` in su.
- **`format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'`**: Mostra il timestamp, il nome del logger, il livello e il messaggio.
- **`filename='app.log'`**: Salva tutti i messaggi in un file chiamato `app.log`.
- **`filemode='w'`**: Sovrascrive il file `app.log` ogni volta che il programma viene eseguito.

---

### Messaggi di Log

Ogni messaggio rappresenta un evento nel programma:
- **`logging.debug()`**: Per dettagli utili durante lo sviluppo.
- **`logging.info()`**: Per notifiche sul corretto funzionamento.
- **`logging.warning()`**: Per avvisi che meritano attenzione.
- **`logging.error()`**: Per errori che impediscono l'esecuzione corretta.
- **`logging.critical()`**: Per errori gravi che necessitano di intervento immediato.

---

### Vantaggi della Configurazione in File

Salvare i log in un file consente di:
1. **Analizzare eventi passati**: Utile per il debug in programmi complessi.
2. **Monitorare il comportamento**: Permette di tenere traccia delle attività nel tempo.
3. **Creare documentazione**: Fornisce una cronologia utile per migliorare il programma.