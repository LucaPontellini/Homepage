from threading import Thread, Lock

# Creazione dell'oggetto Lock
mutex = Lock()

# Classe ThreadConcorrenzi che eredita dalla classe Thread
class ThreadConcorrenzi(Thread):
    def __init__(self, nome):
        # Inizializzazione del thread e assegnazione del nome
        Thread.__init__(self)
        self.nome = nome

    def run(self):
        # Acquisizione del Lock per garantire l'accesso esclusivo alla sezione critica
        mutex.acquire()
        print("\n Inizio Thread " + self.nome)
        print("Attività svolta dal thread")
        print("\n Fine Thread " + self.nome)
        # Rilascio del Lock per consentire ad altri thread di accedere alla sezione critica
        mutex.release()

# Creazione e avvio dei thread
thread1 = ThreadConcorrenzi("Pippo")
thread2 = ThreadConcorrenzi("Pluto")

# Avvio dei thread
thread1.start()
thread2.start()

# Attesa della terminazione dei thread
thread1.join()
thread2.join()

# Stampa del messaggio di fine esecuzione
print("\nFine esecuzione")