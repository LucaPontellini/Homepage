#Esercizio: Scrivi un programma che passati in input n valori popoli in una lista, la ristampi a video scorrendola con un for.

list_of_peoples = []
number_of_peoples = input ("Enter the number of peoples '")

for peoples in number_of_peoples:
    list_of_peoples.append (number_of_peoples)
    print (f"The list contains {list_of_peoples} peoples")