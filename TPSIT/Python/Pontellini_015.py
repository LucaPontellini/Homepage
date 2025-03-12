import threading
import time

# Variabile condivisa
lock = threading.Lock()
turn = "DIN"  # Determina chi deve eseguire
shared_list = []  # Lista condivisa per memorizzare i risultati

# Funzione per il thread "DIN"
def din():
    global turn
    for _ in range(10):  # Numero di iterazioni
        with lock:
            if turn == "DIN":
                if len(shared_list) > 0:
                    shared_list.pop()  # Rimuovi l'elemento precedente
                shared_list.append("DIN")  # Aggiungi il nuovo elemento
                print(shared_list)
                turn = "DON"  # Passa il turno
        time.sleep(0.5)  # Pausa

# Funzione per il thread "DON"
def don():
    global turn
    for _ in range(10):  # Numero di iterazioni
        with lock:
            if turn == "DON":
                if len(shared_list) > 0:
                    shared_list.pop()  # Rimuovi l'elemento precedente
                shared_list.append("DON")  # Aggiungi il nuovo elemento
                print(shared_list)
                turn = "DIN"  # Passa il turno
        time.sleep(0.5)  # Pausa

# Creazione dei thread
din_thread = threading.Thread(target=din)
don_thread = threading.Thread(target=don)

# Avvio dei thread
din_thread.start()
don_thread.start()

# Aspetta che i thread finiscano
din_thread.join()
don_thread.join()

print("DIN-DON terminato!")