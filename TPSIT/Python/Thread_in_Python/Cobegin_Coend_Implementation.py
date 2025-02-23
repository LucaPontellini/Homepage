import threading

# Funzione per calcolare l'espressione 3 e aggiungere il risultato alla lista
def calculate_expression_3(result):
    result.append((3 + 2) * (5 - 2) * (8 - 3))

# Funzione per calcolare l'espressione 4 con i valori x e y e aggiungere il risultato alla lista
def calculate_expression_4(result, x, y):
    result.append((2 + x) * (3 + x) * (7 + y + 4) - 10)

if __name__ == "__main__":
    # Input dall'utente
    x = int(input("Inserisci il valore per x: "))
    y = int(input("Inserisci il valore per y: "))
    
    result_3 = []  # Lista per memorizzare il risultato dell'espressione 3
    result_4 = []  # Lista per memorizzare il risultato dell'espressione 4
    
    # Creazione dei thread
    thread_3 = threading.Thread(target=calculate_expression_3, args=(result_3,))
    thread_4 = threading.Thread(target=calculate_expression_4, args=(result_4, x, y))
    
    # Avvio dei thread
    thread_3.start()
    thread_4.start()
    
    # Attesa del completamento dei thread
    thread_3.join()
    thread_4.join()
    
    # Stampa dei risultati
    print("Risultato dell'Espressione 3:", result_3[0])
    print("Risultato dell'Espressione 4:", result_4[0])