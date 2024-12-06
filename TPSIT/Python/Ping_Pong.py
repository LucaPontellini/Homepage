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