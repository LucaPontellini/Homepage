#Esercizio 1: Chiesti all’utente 5 voti in input dire quanti di questi sono sufficienti su quelli considerati validi. I voti sono considerati validi se compresi tra 1 e 10.

vote_1 = int (input ("Enter your first vote: '"))
vote_2 = int (input ("Enter your second vote: '"))
vote_3 = int (input ("Enter your third vote: '"))
vote_4 = int (input ("Enter your fourth vote: '"))
vote_5 = int (input ("Enter your fifth vote: '"))

if vote_1 <= 1 and vote_1 >= 10:
    print ("Error: the vote does not satisfy the condition")
elif vote_2 <= 1 and vote_2 >= 10:
    print ("Error: the vote does not satisfy the condition")
elif vote_3 <= 1 and vote_3 >= 10:
    print ("Error: the vote does not satisfy the condition")
elif vote_4 <= 1 and vote_4 >= 10:
    print ("Error: the vote does not satisfy the condition")
elif vote_5 <= 1 and vote_5 >= 10:
    print ("Error: the vote does not satisfy the condition")
else: print ("Error")

if vote_1 >= 6:
    print ("Your vote is sufficient")
elif vote_2 >= 6:
    print ("Your vote is sufficient")
elif vote_3 >= 6:
    print ("Your vote is sufficient")
elif vote_4 >= 6:
    print ("Your vote is sufficient")
elif vote_5 >= 6:
    print ("Your vote is sufficient")
else:
    print ("Your vote is insufficent")