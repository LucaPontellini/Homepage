#Esercizio: Scrivere una funzione che gestisca l'input di n valori (con n scelto dall'utente) e li restituisca in una lista.

def input_n () -> list [int]:

    num = int (input ("Enter the number of values: '"))

    numbers = []

    for x in range (num):

        number = int (input ("Enter the value: '"))

        numbers.append (number)

    return numbers

def print_numbers (numbers: list [int]) -> None:
    
    for number in numbers:
        print (number)

numbers = input_n ()
print_numbers (numbers)