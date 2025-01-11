#Esercizio: Scrivi un programma che simula una calcolatrice semplice.
#Il programma deve permettere all'utente di inserire due numeri e scegliere un'operazione
#(addizione, sottrazione, moltiplicazione, divisione).
#Il programma deve quindi visualizzare il risultato dell'operazione.

def inserisci_numeri() -> list[int]: # type: ignore
    
    """Richiede all'utente di inserire una serie di numeri interi.

    Returns:
        list[int]: Una lista di numeri interi inseriti dall'utente"""
    
    pass

def scegli_operazione() -> str: # type: ignore
    
    """Richiede all'utente di scegliere un'operazione aritmetica.

    Returns:
        str: Una stringa rappresentante l'operazione scelta dall'utente.
             Può essere "somma", "sottrazione", "moltiplicazione" o "divisione" """
    
    pass

def calcola(numeri: list[int], operazione: str) -> float: # type: ignore
    
    """Esegue l'operazione aritmetica scelta dall'utente sui numeri forniti.

    Args:
        numeri (list[int]): La lista di numeri su cui eseguire l'operazione.
        operazione (str): L'operazione aritmetica da eseguire ("somma", "sottrazione", 
                          "moltiplicazione" o "divisione").

    Returns:
        float: Il risultato dell'operazione aritmetica eseguita sui numeri"""
    
    pass

def main():
    
    """Funzione principale che coordina l'inserimento dei numeri, la scelta
    dell'operazione e il calcolo del risultato.

    Esegue il flusso di lavoro completo del programma:
    1. Richiede all'utente di inserire una lista di numeri.
    2. Richiede all'utente di scegliere un'operazione aritmetica.
    3. Calcola il risultato dell'operazione sui numeri forniti.
    4. Stampa il risultato del calcolo"""

    numeri_inseriti = inserisci_numeri()
    operazione = scegli_operazione()
    risultato = calcola(numeri_inseriti, operazione)
    print(f"Il risultato dell'operazione è: {risultato}")