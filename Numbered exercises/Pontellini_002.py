#Esercizio 2: Chiesto all’utente un anno in input controllare la validità dell’input (0<anno<2100) e dire se esso è bisestile o no. A tal fine, implementare il seguente algoritmo: Un anno è bisestile se esso è divisibile per 400 altrimenti è bisestile se è divisibile per 4 e non divisibile per 100. Non è bisestile negli altri casi.
#N.B:
#L’algoritmo può essere implementato anche con un unico blocco if/else con una condizione composta.

year_1 = int (input ("Enter a number of the year: '"))

if year_1 > 0 and year_1 < 2100:
    print ("Your year is a leap year")
else: print ("Your year is not a leap year")

year_2 = year_1 / 400

if year_2 % 400:
    print ("The year is a leap year")
elif year_2 % 4:
    print ("The year is a leap year")
else: print ("The year is not a leap year")