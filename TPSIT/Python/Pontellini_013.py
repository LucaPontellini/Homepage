import threading
import time
import random

# Classe ScatolaCaramelle che rappresenta la scatola condivisa di caramelle
class ScatolaCaramelle:
    def __init__(self, capacità):
        self.capacità = capacità  # Imposta la capacità massima della scatola
        self.cariche_attuali = 0  # Imposta il numero iniziale di caramelle nella scatola
        self.lock = threading.Lock()  # Crea un oggetto Lock per garantire l'accesso esclusivo alla scatola

    def aggiungi_caramelle(self, quantità):
        self.lock.acquire()  # Acquisisce il lock prima di modificare il numero di caramelle
        while self.cariche_attuali + quantità > self.capacità:
            self.lock.release()  # Rilascia il lock se la scatola è piena e attende
            time.sleep(0.1)  # Attende prima di tentare di nuovo
            self.lock.acquire()  # Riacquisisce il lock
        self.cariche_attuali += quantità  # Aggiunge la quantità di caramelle alla scatola
        print(f"Produttore aggiunge {quantità} caramelle. Caramelle attuali: {self.cariche_attuali}")
        self.lock.release()  # Rilascia il lock dopo aver terminato la modifica

    def consuma_caramelle(self, quantità):
        self.lock.acquire()  # Acquisisce il lock prima di modificare il numero di caramelle
        while self.cariche_attuali < quantità:
            self.lock.release()  # Rilascia il lock se non ci sono abbastanza caramelle e attende
            time.sleep(0.1)  # Attende prima di tentare di nuovo
            self.lock.acquire()  # Riacquisisce il lock
        self.cariche_attuali -= quantità  # Sottrae la quantità di caramelle dalla scatola
        print(f"Consumatore consuma {quantità} caramelle. Caramelle attuali: {self.cariche_attuali}")
        self.lock.release()  # Rilascia il lock dopo aver terminato la modifica

# Funzione eseguita dai produttori di caramelle
def produttore(scatola, id_produttore):
    while True:
        quantità = random.randint(1, 5)  # Quantità casuale di caramelle da aggiungere
        scatola.aggiungi_caramelle(quantità)  # Aggiunge le caramelle alla scatola
        time.sleep(random.uniform(0.5, 2.0))  # Pausa casuale tra una produzione e l'altra

# Funzione eseguita dai consumatori di caramelle
def consumatore(scatola, id_consumatore):
    while True:
        quantità = random.randint(1, 3)  # Quantità casuale di caramelle da consumare
        scatola.consuma_caramelle(quantità)  # Consuma le caramelle dalla scatola
        time.sleep(random.uniform(0.5, 2.0))  # Pausa casuale tra un consumo e l'altro

# Creazione della scatola di caramelle con capacità di 20 caramelle
scatola = ScatolaCaramelle(20)

# Creazione e avvio dei thread per i produttori
for i in range(2):
    threading.Thread(target=produttore, args=(scatola, i)).start()

# Creazione e avvio dei thread per i consumatori
for i in range(5):
    threading.Thread(target=consumatore, args=(scatola, i)).start()