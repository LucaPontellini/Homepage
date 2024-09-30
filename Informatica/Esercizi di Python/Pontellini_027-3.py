#Esercizio: Scrivere una funzione che data in input una lista, calcoli la somma dei quadrati dei numeri pari presenti nella lista e restituisca tale valore.

def input_n () -> list [int]:

    num = int (input ("Enter the number of values: '"))

    list_of_values = []

    for x in range (num):

        number = int (input ("Enter the value: '"))

        list_of_values.append (number)

    return list_of_values
    
def sum_squares (list_of_values: list [int]) -> int:

    sum = 0

    for number in list_of_values:

        if number % 2 == 0:
            sum += number ** 2

    return sum

list_of_values = input_n ()
print (sum_squares (list_of_values))