#Esercizio: lancia una moneta e stampa se esce testa o croce.

import random

user_input = str (input ("Do you want to play? '"))

if user_input == "Yes":

    choise = str (input ("Do you choose heads or tails?\nEnter 'heads' if you want to choose the one or 'cross' if you choose the other: '"))

    coin = ["head" , "cross"]

    coin [0] = "0"
    coin [1] = "1"

    print ("It has been released:")
    print (random.choice (coin))

    print ("--------------------")

    print ("0 = head")
    print ("1 = cross")

    print ("--------------------")

else: print ("You won't play")