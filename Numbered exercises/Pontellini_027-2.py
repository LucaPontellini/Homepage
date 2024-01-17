#Esercizio: Scrivere una funzione alla quale passato un numero intero restituisca True se esso è pari e False in caso contrario.

def is_pari (num: int) -> bool:

    num = int (input ("Enter one number: '"))

    return num

def verify (num: int) -> bool:

    if num % 2 == 0:
        return True
    
    elif num % 2 == 1:
        return False
    
    else: return "Error"

num = is_pari ()
print (verify (num))