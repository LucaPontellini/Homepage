import threading
import random
from threading import Thread, BoundedSemaphore

# Creazione oggetto semaforo con un valore massimo di threads simultanei
nrThread = 1
semaforo = BoundedSemaphore(value=nrThread)

# Variabili globali
dato = 0

def set_dato(valore):
    global dato
    dato = valore  # Imposta il valore della variabile globale 'dato'

def get_dato():
    return dato  # Restituisce il valore della variabile globale 'dato'

class Produttore(Thread):
    def __init__(self, nome):
        Thread.__init__(self)  # Inizializzazione della classe Thread
        self.nome = nome

    def run(self):
        semaforo.acquire()  # Acquisisce il semaforo
        buffer = random.randint(10, 99)  # Genera un valore casuale tra 10 e 99
        set_dato(buffer)  # Imposta il valore generato nella variabile globale 'dato'
        print(f"prodotto {buffer}")  # Stampa il valore prodotto
        semaforo.release()  # Rilascia il semaforo

class Consumatore(Thread):
    def __init__(self, nome):
        Thread.__init__(self)  # Inizializzazione della classe Thread
        self.nome = nome

    def run(self):
        semaforo.acquire()  # Acquisisce il semaforo
        buffer = get_dato()  # Ottiene il valore dalla variabile globale 'dato'
        print(f"consumato {buffer}")  # Stampa il valore consumato
        set_dato(0)  # Reimposta la variabile globale 'dato' a 0
        semaforo.release()  # Rilascia il semaforo

# Esempio di esecuzione
produttore = Produttore("Produttore")  # Crea un thread produttore
consumatore = Consumatore("Consumatore")  # Crea un thread consumatore

produttore.start()  # Avvia il thread produttore
consumatore.start()  # Avvia il thread consumatore

produttore.join()  # Attende il completamento del thread produttore
consumatore.join()  # Attende il completamento del thread consumatore

print("Fine esecuzione")  # Stampa il messaggio di fine esecuzione