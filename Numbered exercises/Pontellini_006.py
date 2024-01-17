#Esercizio: chiedi all'utente due numeri, converti l'input dell'utente in numeri interi utilizza istruzioni if-else e operatori logici per determinare se i numeri sono entrambi pari, entrambi dispari o uno pari e uno dispari e stampa il risultato.

num1 = int (input ("Enter one number: '"))
num2 = int (input ("Enter one number: '"))

if num1 % 2 == 0 and num2 % 2 == 0:
    print ("The numbers are even")
elif num1 % 2 == 1 and num2 % 2 == 1:
    print ("The numbers are odd")
elif num1 % 2 == 1 and num2 % 2 == 0:
    print ("The first number is odd, The second number is even")
elif num1 % 2 == 0 and num2 % 2 == 1:
    print ("The first number is even, The second number is odd")
else:
    print("Impossible")