from threading import Thread  # Importa la classe Thread dal modulo threading
from time import sleep  # Importa la funzione sleep dal modulo time

def codice_thread(arg):  # Definisce una funzione che accetta un argomento
    for x in range(arg):  # Cicla dal valore 0 fino a 'arg' (non incluso)
        print("sto contando:", x)  # Stampa il valore corrente di 'x'
        sleep(1)  # Attende per 1 secondo

# Creazione e avvio del thread
thread = Thread(target=codice_thread, args=(4,))  # Crea un oggetto Thread per eseguire la funzione 'codice_thread' con l'argomento 4
thread.start()  # Avvia l'esecuzione del thread
# Attendere il completamento del thread
thread.join()  # Attende che il thread termini l'esecuzione
print("thread terminato: fine programma!")  # Stampa un messaggio alla fine del programma