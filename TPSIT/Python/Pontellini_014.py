import threading
import math
import logging

# Configurazione del logging
logging.basicConfig(level=logging.DEBUG, format="%(threadName)s: %(message)s")

# Funzione per calcolare il fattoriale
def calcola_fattoriale(numero, lock):
    if numero < 0:
        with lock:
            print("Il fattoriale non è definito per numeri negativi.")
    else:
        fattoriale = math.factorial(numero)
        with lock:
            print(f"Il fattoriale di {numero} è {fattoriale}")
        logging.debug("Fattoriale calcolato correttamente")

# Funzione per calcolare la radice quadrata
def calcola_radice_quadrata(numero, lock):
    if numero < 0:
        with lock:
            print("La radice quadrata non è definita per numeri negativi.")
    else:
        radice = math.sqrt(numero)
        with lock:
            print(f"La radice quadrata di {numero} è {radice:.2f}")
        logging.debug("Radice quadrata calcolata correttamente")

if __name__ == "__main__":
    try:
        # Gestione dell'input
        numero = int(input("Inserisci un numero: "))
    except ValueError:
        print("Per favore, inserisci un numero intero valido.")
        exit()

    # Creazione del lock per sincronizzare l'accesso alle risorse condivise
    lock = threading.Lock()

    # Creazione dei thread
    thread_fattoriale = threading.Thread(target=calcola_fattoriale, args=(numero, lock), name="Thread-Fattoriale")
    thread_radice_quadrata = threading.Thread(target=calcola_radice_quadrata, args=(numero, lock), name="Thread-Radice")

    # Avvio dei thread
    thread_fattoriale.start()
    thread_radice_quadrata.start()

    # Attesa della terminazione dei thread
    thread_fattoriale.join()
    thread_radice_quadrata.join()