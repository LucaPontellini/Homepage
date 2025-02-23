import threading

class Buffer:
    def __init__(self):
        # Inizializza l'area condivisa con il valore 0
        self.areaCondivisa = 0
        # Inizializza i lock per il produttore e il consumatore
        self.produttore_lock = threading.Lock()
        self.consumatore_lock = threading.Lock()
        # Il lock del consumatore viene acquisito all'inizio
        self.consumatore_lock.acquire()

    def set_areaCondivisa(self, value, name):
        # Acquisisce il lock del produttore
        self.produttore_lock.acquire()
        # Imposta il valore dell'area condivisa
        self.areaCondivisa = value
        # Stampa il valore impostato insieme al nome del produttore
        print(f'{name}: {value} (1 di 4)')
        # Rilascia il lock del consumatore
        self.consumatore_lock.release()

    def get_areaCondivisa(self, name):
        # Acquisisce il lock del consumatore
        self.consumatore_lock.acquire()
        # Ottiene il valore dell'area condivisa
        value = self.areaCondivisa
        # Stampa il valore ottenuto insieme al nome del consumatore
        print(f'{name}: {value} (1 di 4)')
        # Rilascia il lock del produttore
        self.produttore_lock.release()
        return value