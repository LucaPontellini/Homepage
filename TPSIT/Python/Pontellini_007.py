import threading

valore_somma = 5 + 3
valore_sottrazione = 4 - 2

def calcola_somma(result, valore):
    result.append(valore)

def calcola_sottrazione(result, valore):
    result.append(valore)

def main():
    risultato_somma = []
    risultato_sottrazione = []

    thread_somma = threading.Thread(target=calcola_somma, args=(risultato_somma, valore_somma))
    thread_sottrazione = threading.Thread(target=calcola_sottrazione, args=(risultato_sottrazione, valore_sottrazione))

    thread_somma.start()
    thread_sottrazione.start()

    thread_somma.join()
    thread_sottrazione.join()

    print(f"Risultato della somma (5 + 3): {risultato_somma[0]}")
    print(f"Risultato della sottrazione (4 - 2): {risultato_sottrazione[0]}")

    risultato_finale = risultato_somma[0] * risultato_sottrazione[0]
    print(f"Il risultato dell'operazione ({risultato_somma[0]} * {risultato_sottrazione[0]}) è: {risultato_finale}")

if __name__ == "__main__":
    main()