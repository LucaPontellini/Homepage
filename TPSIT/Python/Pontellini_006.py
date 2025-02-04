import threading

def calcola_operazione_positivi(numeri, results):
    numeri_positivi = [numero for numero in numeri if numero > 0]
    risultato = sum(numeri_positivi)
    results.append(risultato)

def calcola_operazione_dispari(numeri, results):
    numeri_dispari = [numero for numero in numeri if numero % 2 != 0]
    risultato = sum(numeri_dispari)
    results.append(risultato)

def main():
    # Richiesta del vettore in input
    numeri = []
    for _ in range(2):
        try:
            numero = int(input("Inserisci numero: "))
            numeri.append(numero)
        except ValueError:
            print("Input non valido. Per favore, inserisci un numero intero.")
            return

    # Lista per memorizzare i risultati
    results = []

    # Creazione dei thread
    thread1 = threading.Thread(target=calcola_operazione_positivi, args=(numeri, results))
    thread2 = threading.Thread(target=calcola_operazione_dispari, args=(numeri, results))

    # Avvio dei thread
    thread1.start()
    thread2.start()

    # Attesa del completamento dei thread
    thread1.join()
    thread2.join()

    # Stampa dei risultati
    print("Risultati:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()