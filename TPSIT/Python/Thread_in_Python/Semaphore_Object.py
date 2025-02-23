import threading
import random

# Classe Buffer con semafori
class BufferSem:
    def __init__(self):
        self.areaCondivisa = 0  # Valore condiviso tra produttori e consumatori
        self.produttore_semaforo = threading.Semaphore(1)  # Semaforo per controllare l'accesso del produttore
        self.consumatore_semaforo = threading.Semaphore(0)  # Semaforo per controllare l'accesso del consumatore
        self.consumatore_lock = threading.Lock()  # Lock per proteggere l'accesso all'array dei consumatori
        self.consumatore_array = []  # Array per memorizzare i valori consumati

    def set_areaCondivisa(self, value, name):
        self.produttore_semaforo.acquire()  # Acquisisce il semaforo del produttore
        self.areaCondivisa = value  # Aggiorna il valore condiviso
        print(f'Prodotto {value} da {name}')
        self.consumatore_semaforo.release()  # Rilascia il semaforo del consumatore

    def get_areaCondivisa(self, name):
        self.consumatore_semaforo.acquire()  # Acquisisce il semaforo del consumatore
        value = self.areaCondivisa  # Legge il valore condiviso
        with self.consumatore_lock:  # Acquisisce il lock per accedere all'array dei consumatori
            self.consumatore_array.append(value)  # Aggiunge il valore letto all'array
        print(f'Consumato {value} da {name}')
        self.produttore_semaforo.release()  # Rilascia il semaforo del produttore
        return value

# Classe Produttore
class Produttore(threading.Thread):
    def __init__(self, nome, buffer):
        threading.Thread.__init__(self)
        self.nome = nome  # Nome del produttore
        self.buffer = buffer  # Buffer condiviso

    def run(self):
        for _ in range(4):  # Produce 4 valori casuali
            value = random.randint(10, 99)  # Genera un valore casuale
            self.buffer.set_areaCondivisa(value, self.nome)  # Imposta il valore condiviso

# Classe Consumatore
class Consumatore(threading.Thread):
    def __init__(self, nome, buffer):
        threading.Thread.__init__(self)
        self.nome = nome  # Nome del consumatore
        self.buffer = buffer  # Buffer condiviso

    def run(self):
        for _ in range(4):  # Consuma 4 valori
            self.buffer.get_areaCondivisa(self.nome)  # Legge il valore condiviso

# Creazione buffer condiviso
buffer = BufferSem()

# Creazione e avvio dei produttori e consumatori
produttore1 = Produttore("Produttore1", buffer)
produttore2 = Produttore("Produttore2", buffer)
consumatore1 = Consumatore("Consumatore1", buffer)
consumatore2 = Consumatore("Consumatore2", buffer)

produttore1.start()
produttore2.start()
consumatore1.start()
consumatore2.start()

produttore1.join()
produttore2.join()
consumatore1.join()
consumatore2.join()

# Stampa dei dati consumati memorizzati nell'array
print("\nDati consumati:", buffer.consumatore_array)

print("\nFine esecuzione")