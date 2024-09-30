#Esercizio: dati in input il voto in trentesimi e il numero di crediti di tre esami, calcolare la media ponderata. Nota bene:fare il controllo che il voto sia da 1 a 30 e che i crediti siano da 1 a 12.

vote = int (input ("Enter your vote"))
credits = int (input ("Enter your number of credits"))

average = vote

if average == range (1-17):
    print (f"The vote corresponds to {vote}. Your vote is insufficient")
elif average == range (18-23):
    print (f"The vote corresponds to {vote}. Your vote is enough")
elif average == range (24-26):
    print (f"The vote corresponds to {vote}. Your vote is discreet")
elif average == range (27-30):
    print (f"The vote corresponds to {vote}. Your vote is good")

