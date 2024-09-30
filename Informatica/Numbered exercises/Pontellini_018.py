#Esercizio: scrivi un programma che passati in input n valori popoli una lista. In seguito scorri lista con un for e ne calcoli il valore medio, il massimo e il minimo.

list_of_peoples = []
number_of_peoples_1 = input ("Enter the number of peoples '")

for peoples in number_of_peoples_1:
    list_of_peoples.append (number_of_peoples_1)
    number_of_peoples_2 = input ("Enter the number of peoples '")
    list_of_peoples.append (number_of_peoples_2)
    number_of_peoples_3 = input ("Enter the number of peoples '")
    list_of_peoples.append (number_of_peoples_3)

if number_of_peoples_1 > number_of_peoples_2 and number_of_peoples_1 > number_of_peoples_3:
    print (f"{number_of_peoples_1} This number is the largest on the list")
elif number_of_peoples_1 < number_of_peoples_2 and number_of_peoples_1 < number_of_peoples_3:
    print (f"{number_of_peoples_2} This number is the largest on the list")
elif number_of_peoples_3 > number_of_peoples_1 and number_of_peoples_3 > number_of_peoples_2:
    print (f"{number_of_peoples_2} This number is the largest on the list")