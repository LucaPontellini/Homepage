#Esercizio: dato in input un numero scritto con sistema di numerazione decimale (intero), calcolare la sua conversione in binario. Dato che la stampa a video del numero deve avvenire in ordine inverso da quello del calcolo, usare una lista per stampare il valore corretto.

number = int (input ("Enter a number: '"))
binary_number = []
result_1 = number

while not (result_1 == 0):
   
   rest = result_1 % 2
   result_1 = result_1 // 2
   binary_number.append (rest)
   print (binary_number)
   
binary_number.reverse ()

for x in binary_number:
   print (x, end= '')

print (f"The number you entered is: {number}. Its conversion to binary is: {binary_number}")