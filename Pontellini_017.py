#Esercizio: scrivi un programma che passati in input n valori popoli una lista. In seguito chiedi all'utente di inserire un valore in modo tale da verificare che esso sia presente nella lista. Stampa a video ("Valore presente"/"Valore non presente").

list_of_peoples = []
number_of_peoples = input ("Enter the number of value '")
value = input ("Enter a value: '")

for peoples in number_of_peoples:
    list_of_peoples.append (number_of_peoples)
    print (f"The list contains {list_of_peoples} peoples")

if value is list_of_peoples:
    print (f"This {value} value is in the list")
else: print (f"This {value} value isn't in the list")