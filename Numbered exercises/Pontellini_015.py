#Esercizio: scrivere un programma che passati in input un numero non definito a priori di voti, ne calcoli la media. Il programma terminerà con l'iterazione degli input quando inseriamo un valore <=0. Non si considerino ai fini della media, i voti >10.

votes = int (input ("Enter a number of votes: '"))

i = 0
average = 0
vote_1 = 0

while i < votes:
    vote = int (input ("Enter a vote: '"))

    if vote <= 0:
        print ("No valid values have been entered")

    elif vote < 1 and vote > 10:
        vote / 0

    vote_1 = votes - 1
    average = vote + average

    i = i + 1
    print (f"The average is: {average / vote_1}")