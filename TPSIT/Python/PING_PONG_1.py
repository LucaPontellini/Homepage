import threading
import time

# Una variabile condivisa per gestire il ping-pong
lock = threading.Lock()
turn = "ping"  # Determina chi deve eseguire

# Funzione per il thread "ping"
def ping():
    global turn
    for _ in range(10):  # Numero di iterazioni
        with lock:
            if turn == "ping":
                print("Ping")
                turn = "pong"  # Passa il turno
        time.sleep(0.5)  # Piccola pausa per simulare il ritardo

# Funzione per il thread "pong"
def pong():
    global turn
    for _ in range(10):  # Numero di iterazioni
        with lock:
            if turn == "pong":
                print("Pong")
                turn = "ping"  # Passa il turno
        time.sleep(0.5)  # Piccola pausa per simulare il ritardo

# Creazione dei thread
ping_thread = threading.Thread(target=ping)
pong_thread = threading.Thread(target=pong)

# Avvio dei thread
ping_thread.start()
pong_thread.start()

# Aspetta che i thread finiscano
ping_thread.join()
pong_thread.join()

print("Ping-pong terminato!")

#Funzionamento:
#1. Utilizza una variabile 'turn' di tipo stringa ("ping" o "pong") per determinare quale thread deve eseguire.
#2. Stampa le stringhe "Ping" e "Pong" alternando tra i thread.
#3. Esegue un numero fisso di iterazioni (10) per ciascun thread.
#4. Utilizza un ritardo fisso di 0.5 secondi tra ogni stampa di "Ping" e "Pong".