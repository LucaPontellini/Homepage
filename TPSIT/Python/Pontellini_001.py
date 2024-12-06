import threading

# Definizione della classe thread che eredita dalla classe threading.Thread
class thread(threading.Thread):
    def __init__(self, thread_name, thread_ID):
        # Inizializzazione della classe base threading.Thread
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID
    
    # Metodo run che viene eseguito quando il thread viene avviato
    def run(self):
        # Stampa il nome del thread e l'ID del thread
        print(str(self.thread_name) + "" + str(self.thread_ID))

# Creazione di due istanze della classe thread
thread_1 = thread("\nthread A", 100)
thread_2 = thread("\nthread B", 200)

# Avvio dei thread
thread_1.start()
thread_2.start()

# Attesa che i thread terminino
thread_1.join()
thread_2.join()

# Stampa del messaggio di uscita
print("\n\nExit")