#Esercizio: scrivere un programma che passati in input un numero non definito a priori di voti, ne calcoli la media. Il programma terminerà con l'iterazione degli input quando inseriamo un valore <=0. Non si considerino ai fini della media, i voti >10.

sum_of_votes = 0
number_of_vote = 0
i = 0

for i in range (number_of_vote):
    vote = int (input ("Enter a vote: '"))
    average = sum_of_votes / number_of_vote
    print (f"The average is: {average}")

    i += 1
    
    if vote <= 0:
        i == 0
        print ("No valid values have been entered")