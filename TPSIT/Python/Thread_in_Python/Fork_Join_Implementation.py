import threading

# Funzione per calcolare la prima espressione e aggiungere il risultato alla lista
def calculate_expression_1(result):
    result.append(5 * ((2 + 4) * (7 + 3)) - 10)

# Funzione per calcolare la seconda espressione con valori di x e y forniti dall'utente
def calculate_expression_2(result, x, y):
    result.append((3 + x) - (2 + y) * (7 * y + 3))

if __name__ == "__main__":
    # Input dall'utente
    x = int(input("Inserisci il valore di x: "))
    y = int(input("Inserisci il valore di y: "))
    
    # Liste per memorizzare i risultati delle due espressioni
    result_1 = []
    result_2 = []
    
    # Creazione dei thread per entrambe le espressioni
    thread_1 = threading.Thread(target=calculate_expression_1, args=(result_1,))
    thread_2 = threading.Thread(target=calculate_expression_2, args=(result_2, x, y))
    
    # Avvio dei thread
    thread_1.start()
    thread_2.start()
    
    # Attesa per il completamento di entrambi i thread
    thread_1.join()
    thread_2.join()
    
    # Output dei risultati di entrambe le espressioni
    print("Risultato dell'Espressione 1:", result_1[0])
    print("Risultato dell'Espressione 2:", result_2[0])