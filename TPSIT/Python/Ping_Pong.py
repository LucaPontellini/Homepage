import threading
import time

# Creazione di un oggetto Lock per sincronizzare i thread
lock = threading.Lock()

# Variabile condivisa per alternare i thread
turn = 0

def print_letter(letter, thread_id):
    global turn
    while True:
        with lock:
            if turn % 2 == thread_id:
                print(letter, end='', flush=True)
                turn += 1
                break
        time.sleep(0.1)

def print_ping_pong():
    ping_pong = "PING PONG"
    for i, letter in enumerate(ping_pong):
        print_letter(letter, i % 2)
        time.sleep(1)

# Creazione dei thread
thread_ping_pong = threading.Thread(target=print_ping_pong)

# Avvio dei thread
thread_ping_pong.start()

# Attesa che il thread termini
thread_ping_pong.join()

#Funzionamento:
#1. Utilizza una variabile 'turn' di tipo intero per alternare tra i thread.
#2. Stampa le lettere della stringa "PING PONG" alternando tra i thread.
#3. Non ha un numero fisso di iterazioni, ma si basa sulla lunghezza della stringa "PING PONG".
#4. Utilizza un ritardo di 0.1 secondi all'interno del ciclo while e un ritardo di 1 secondo tra la stampa di ciascuna lettera.