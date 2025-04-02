# Multithreading e Logging

Quando un'applicazione utilizza il multithreading, il logging può diventare più complesso. La libreria `logging` di Python supporta nativamente il multithreading, garantendo la registrazione corretta dei messaggi anche in ambienti concorrenti.

---

## Sfide del Logging in Multithreading

1. **Ordine dei messaggi**: I messaggi di log potrebbero apparire fuori sequenza a causa dell'esecuzione simultanea dei thread.
2. **Accesso concorrente**: Più thread potrebbero tentare di scrivere nello stesso file contemporaneamente, causando conflitti.
3. **Performance**: Un utilizzo inefficiente del logging può rallentare l'applicazione, soprattutto con numerosi thread attivi.

---

## Esempio di Logging con Thread

Ecco un esempio pratico per configurare il logging in un'applicazione multithread:

```python
import logging
import threading
import time

# Configurazione di base
logging.basicConfig(
    level=logging.INFO,
    format='%(threadName)s - %(levelname)s - %(message)s'
)

# Funzione worker eseguita da ogni thread
def worker(name):
    logging.info(f"Lavoratore {name} sta iniziando.")  # Messaggio di inizio
    time.sleep(1)  # Simulazione di lavoro
    logging.info(f"Lavoratore {name} ha terminato.")  # Messaggio di fine

# Creazione dei thread
threads = []
for i in range(3):  # Numero di thread
    t = threading.Thread(target=worker, args=(i,), name=f"Thread-{i}")
    threads.append(t)
    t.start()  # Avvia il thread

# Attendere il completamento di tutti i thread
for t in threads:
    t.join()  # Aspetta che ogni thread termini
```

## Spiegazione dell'Esempio

### **Configurazione di Base**
- **`logging.basicConfig`**:
  - **`level=logging.INFO`**: Registra i messaggi di livello `INFO` e superiori.
  - **`format='%(threadName)s - %(levelname)s - %(message)s'`**: Mostra:
    - **`%(threadName)s`**: Nome del thread che genera il messaggio.
    - **`%(levelname)s`**: Livello di gravità del messaggio.
    - **`%(message)s`**: Contenuto del messaggio.

---

### **Funzione Worker**
- **`worker(name)`**:
  - Registra un messaggio all'inizio del lavoro (con **`logging.info`**).
  - Simula un'attività con **`time.sleep(1)`**.
  - Registra un messaggio al termine del lavoro.

---

### **Creazione e Gestione dei Thread**

#### **Creazione dei Thread**
Ogni thread viene creato con **`threading.Thread`**, specificando:
- **`target=worker`**: La funzione che ogni thread deve eseguire.
- **`args=(i,)`**: Gli argomenti passati alla funzione `worker`.
- **`name=f"Thread-{i}"`**: Un nome unico per ciascun thread.

#### **Avvio dei Thread**
- Ogni thread viene avviato con **`t.start()`**.

#### **Attesa del Completamento**
- Il programma attende che tutti i thread terminino con **`t.join()`**.

---

### **Conclusione**
Utilizzare il logging con il multithreading consente di:
1. **Monitorare l'esecuzione parallela**: Ogni thread registra i propri messaggi, facilitando il debug.
2. **Evitare conflitti**: La libreria `logging` garantisce che i messaggi siano scritti in modo corretto.
3. **Migliorare la leggibilità**: I thread sono identificati chiaramente grazie al loro nome.