# Logging Personalizzato

La libreria `logging` in Python consente di personalizzare ogni aspetto del logging, permettendo di creare configurazioni specifiche per diverse esigenze. Questa flessibilità è particolarmente utile in applicazioni complesse o distribuite.

---

## Esempi di Personalizzazione

### **1. Logger Multipli**
- Creare logger separati per tracciare i log di moduli o componenti diversi.
- Consente una gestione indipendente di diversi flussi di log.

### **2. Handler**
- Inviare i messaggi di log a destinazioni specifiche, come:
  - File.
  - Console.
  - Sistemi di notifica, come email o piattaforme di monitoraggio.

### **3. Formatter**
- Personalizzare il formato dei messaggi di log per includere informazioni rilevanti, come:
  - Timestamp.
  - Livello di gravità.
  - Nome del modulo o del logger.

---

## Creazione di un Logger Personalizzato

Ecco un esempio pratico che mostra come configurare un logger personalizzato:

```python
import logging

# Creazione di un logger
logger = logging.getLogger('app_logger')  # Nome personalizzato del logger
logger.setLevel(logging.DEBUG)  # Imposta il livello di gravità

# Creazione di un handler per la console
console_handler = logging.StreamHandler()  # Invia i messaggi alla console
console_handler.setLevel(logging.DEBUG)  # Mostra i messaggi di livello DEBUG e superiori

# Creazione di un formatter personalizzato
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')  # Formato personalizzato
console_handler.setFormatter(formatter)  # Associa il formatter all'handler

# Aggiunta dell'handler al logger
logger.addHandler(console_handler)  # Aggiunge l'handler per la console al logger

# Test del logger personalizzato
logger.info("Logger personalizzato configurato correttamente.")  # Messaggio informativo
logger.debug("Questo è un messaggio di debug.")  # Messaggio di debug
logger.error("Si è verificato un errore!")  # Messaggio di errore
```

## Spiegazione dell'Esempio

### Creazione di un Logger
- **`logger = logging.getLogger('app_logger')`**: Crea un logger con il nome `app_logger`.
- **`logger.setLevel(logging.DEBUG)`**: Imposta il livello minimo di severità su `DEBUG`, includendo tutti i messaggi di log.

---

### Creazione dell'Handler
- **`console_handler = logging.StreamHandler()`**: Configura un handler per inviare i messaggi alla console.
- **`console_handler.setLevel(logging.DEBUG)`**: Mostra messaggi di livello `DEBUG` e superiori.

---

### Formatter Personalizzato
- **`formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')`**: Definisce il formato personalizzato dei messaggi:
  - **`%(name)s`**: Nome del logger.
  - **`%(levelname)s`**: Livello di gravità del messaggio.
  - **`%(message)s`**: Contenuto del messaggio.

---

### Aggiunta dell'Handler
- **`logger.addHandler(console_handler)`**: Collega l'handler per la console al logger.

---

### Messaggi di Log
- **`logger.info("Logger personalizzato configurato correttamente.")`**: Messaggio di livello `INFO` visibile in console.
- **`logger.debug("Questo è un messaggio di debug.")`**: Messaggio di livello `DEBUG` visibile in console.
- **`logger.error("Si è verificato un errore!")`**: Messaggio di livello `ERROR` visibile in console.

---

### Conclusione
La personalizzazione del logging consente di:
1. **Gestire applicazioni complesse** con configurazioni su misura.
2. **Inviare i log a diverse destinazioni** con formati specifici.
3. **Facilitare il debug e il monitoraggio**, migliorando l'efficienza complessiva dello sviluppo.