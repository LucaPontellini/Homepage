import threading  # Importa il modulo threading

# Definisce una classe che eredita da threading.Thread
class MyThread(threading.Thread):
    def __init__(self, thread_name, thread_ID):
        # Inizializza la classe base Thread
        threading.Thread.__init__(self)
        self.thread_name = thread_name  # Assegna il nome del thread
        self.thread_ID = thread_ID  # Assegna l'ID del thread

    # Definisce il metodo run che contiene il codice che sarà eseguito quando il thread viene avviato
    def run(self):
        # Stampa il nome del thread e l'ID
        print(f"{self.thread_name} {self.thread_ID}")

# Creazione e avvio dei thread
thread1 = MyThread("thread A", 100)  # Crea un thread con nome "thread A" e ID 100
thread2 = MyThread("thread B", 200)  # Crea un thread con nome "thread B" e ID 200

# Avvia i thread
thread1.start()  # Avvia il thread1
thread2.start()  # Avvia il thread2

# Attendere il completamento dei thread
thread1.join()  # Attende che thread1 finisca
thread2.join()  # Attende che thread2 finisca

# Stampa il messaggio di uscita dopo che i thread sono completati
print("\nExit")