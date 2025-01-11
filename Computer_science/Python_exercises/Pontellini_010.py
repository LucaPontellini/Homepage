#Esercizio: dati in input il voto in trentesimi e il numero di crediti di tre esami, calcolare la media ponderata. Nota bene: fare il controllo che il voto sia da 1 a 30 e che i crediti siano da 1 a 12.

vote_1 = int (input ("Enter your first vote: '"))
vote_2 = int (input ("Enter your second vote: '"))
vote_3 = int (input ("Enter your third vote: '")) 
credits_1 = int (input ("Enter your first number of credits: '"))
credits_2 = int (input ("Enter your first number of credits: '"))
credits_3 = int (input ("Enter your first number of credits: '"))

if vote_1 < 1 and vote_1 > 30:
    print ("Error:\n You have exceeded the maximum number of votes you can obtain")
elif vote_2 < 1 and vote_2 > 30:
    print ("Error:\n You have exceeded the maximum number of votes you can obtain")
elif vote_3 < 1 and vote_3 > 30:
    ("Error:\n You have exceeded the maximum number of votes you can obtain")
else:
    ("Error:\n You have exceeded the maximum number of votes you can obtain")

average = ((vote_1 * credits_1 + vote_2 * credits_2 + vote_3 * credits_3) / (credits_1 + credits_2 + credits_3))

if average >= 1 and average <= 17:
    print (f"The vote corresponds to {average:.2f}. Your vote is insufficient")
elif average >= 18 and average <= 23:
    print (f"The vote corresponds to {average:.2f}. Your vote is enough")
elif average >= 24 and average <= 26:
    print (f"The vote corresponds to {average:.2f}. Your vote is discreet")
elif average >= 27 and average <= 30:
    print (f"The vote corresponds to {average:.2f}. Your vote is good")
else: 
    print ("Error")
