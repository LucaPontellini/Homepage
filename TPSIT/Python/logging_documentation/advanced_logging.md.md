# Logging Avanzato

Una volta padroneggiati i concetti di base, puoi sfruttare le funzionalità avanzate della libreria `logging` per ottimizzare il logging in applicazioni complesse e distribuite.

---

## Argomenti Avanzati

### **1. Logger Gerarchici**
- Configurare logger che ereditano impostazioni da un logger principale.
- Consente una gestione centralizzata delle configurazioni.

### **2. Multipli Handler e Formatter**
- Permette di diversificare le destinazioni dei log, come console, file o altre piattaforme.
- Consente la personalizzazione del formato dei messaggi per ogni destinazione.

### **3. Configurazione Tramite File**
- Utilizza file di configurazione `.ini` o `.yaml` per centralizzare e semplificare la gestione delle impostazioni.

### **4. Logging Asincrono**
- Garantisce un logging non bloccante, essenziale per applicazioni ad alte prestazioni.

---

## Esempio: Multipli Handler

Di seguito un esempio pratico per configurare handler multipli e personalizzare i formati dei messaggi:

```python
import logging

# Creazione di un logger
logger = logging.getLogger('advanced_logger')  # Nome del logger
logger.setLevel(logging.DEBUG)  # Livello minimo di severità

# Handler per la console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Mostra solo messaggi INFO e superiori

# Handler per il file
file_handler = logging.FileHandler('advanced.log')
file_handler.setLevel(logging.DEBUG)  # Registra tutti i messaggi, inclusi DEBUG

# Formatter personalizzato
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)  # Applica il formato al console handler
file_handler.setFormatter(formatter)  # Applica il formato al file handler

# Aggiunta degli handler al logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Messaggi di log
logger.debug("Questo messaggio è visibile solo nel file.")
logger.info("Questo messaggio è visibile nella console e nel file.")
```

## Spiegazione dell'Esempio

### Creazione di un Logger
- **`logger = logging.getLogger('advanced_logger')`**: Crea un logger con il nome `advanced_logger`.
- **`logger.setLevel(logging.DEBUG)`**: Imposta il livello minimo di severità su `DEBUG`, garantendo che tutti i messaggi vengano processati.

---

### Handler
Gli handler determinano dove inviare i messaggi di log:

#### **Console Handler**
- **`console_handler`**: Mostra i messaggi nella console. Configurato con:
  - **`StreamHandler()`**: Specifica che l'output sarà inviato alla console.
  - **`setLevel(logging.INFO)`**: Mostra solo messaggi con livello `INFO` o superiore.

#### **File Handler**
- **`file_handler`**: Salva i messaggi in un file chiamato `advanced.log`. Configurato con:
  - **`FileHandler('advanced.log')`**: Specifica il file di destinazione.
  - **`setLevel(logging.DEBUG)`**: Registra tutti i messaggi, compresi quelli di livello `DEBUG`.

---

### Formatter
- **`Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')`**:
  - **`%(asctime)s`**: Mostra il timestamp del messaggio.
  - **`%(name)s`**: Nome del logger.
  - **`%(levelname)s`**: Livello di severità.
  - **`%(message)s`**: Il contenuto del messaggio.

---

### Aggiunta degli Handler
- **`logger.addHandler(console_handler)`**: Aggiunge l'handler per la console al logger.
- **`logger.addHandler(file_handler)`**: Aggiunge l'handler per il file al logger.

---

### Messaggi di Log
- **`logger.debug("Questo messaggio è visibile solo nel file.")`**: Il messaggio di livello `DEBUG` appare solo nel file.
- **`logger.info("Questo messaggio è visibile nella console e nel file.")`**: Il messaggio di livello `INFO` appare sia nella console che nel file.

---

### Conclusione
Utilizzare funzionalità avanzate del modulo `logging` consente di:
1. **Gestire applicazioni complesse** con un logging efficace e centralizzato.
2. **Adattare il comportamento del logging** a diverse destinazioni.
3. **Semplificare il debug e il monitoraggio** in scenari multi-thread o distribuiti.