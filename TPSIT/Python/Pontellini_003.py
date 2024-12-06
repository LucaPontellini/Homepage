import threading

def processo1():
    for i in range(10):
        print(i)

# Creazione del thread
thread = threading.Thread(target=processo1)

# Avvio del thread
thread.start()

# Attesa che il thread termini
thread.join()

# Messaggio di fine
print("Ho finito")