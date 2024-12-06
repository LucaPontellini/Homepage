from threading import Thread
from time import sleep

def calcola_operazione_1(result):
    # Calcola l'operazione 5 * [(2 + 4) * (7 + 3)] - 10
    risultato = 5 * ((2 + 4) * (7 + 3)) - 10
    result.append(f"Risultato operazione 1: {risultato}")

def calcola_operazione_2(x, y, result):
    # Calcola l'operazione (3 + x) * (2 + y) * (7 * y + 3)
    risultato = (3 + x) * (2 + y) * (7 * y + 3)
    result.append(f"Risultato operazione 2: {risultato}")

def main():
    # Lettura dei valori di x e y
    x = int(input("Inserisci il valore di x: "))
    y = int(input("Inserisci il valore di y: "))

    # Lista per memorizzare i risultati
    results = []

    # Creazione dei thread
    thread1 = Thread(target=calcola_operazione_1, args=(results,))
    thread2 = Thread(target=calcola_operazione_2, args=(x, y, results))

    # Fork dei thread
    thread1.start()
    thread2.start()

    # Join dei thread per attendere il completamento
    thread1.join()
    thread2.join()

    # Stampa dei risultati
    for result in results:
        print(result)

if __name__ == "__main__":
    main()