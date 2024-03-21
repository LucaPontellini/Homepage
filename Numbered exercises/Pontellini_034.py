#Esercizio 34 - Tracciare una funzione con matplotlib e argparse.
#In questo esercizio utilizzerete il modulo per accettare gli argomenti della riga di comando e il modulo per rappresentare graficamente le funzioni matematiche.
#Si creerà uno script denominato che accetta un numero e uno o più tipi di funzioni come argomenti. I tipi di funzioni possono essere 'lineari', 'polinomiali' o 'esponenziali'.plot_functions.pyn
#Lo script dovrebbe essere in grado di essere eseguito in questo modo:

#python plot_functions.py --linear --polinomial --exponential number
#Le funzioni da rappresentare graficamente sono le seguenti:

#Lineare: y = n * x
#Polinomiale: y = x^n
#Esponenziale: y = n^x
#Per ogni funzione specificata, lo script deve generare un grafico usando matplotlib. I valori x devono essere un elenco di valori compresi tra 0 e 10 (inclusi). 
#I valori y devono essere calcolati in base al tipo di funzione e al numero di ingresso n.
#Ricordarsi di etichettare l'asse x, l'asse y e di fornire un titolo per ogni grafico. Visualizza tutti i grafici alla fine.

import argparse
import matplotlib.pyplot as plt
import numpy as np

#python plot_functions.py --linear --polinomial --exponential number    #script
#Inserisci un numero per la variabile n e poi seleziona il tipo di funzione che vuoi graficare. Puoi scegliere tra ‘lineare’, 
#‘polinomiale’ o ‘esponenziale’. A seconda della tua scelta, lo script creerà il grafico corrispondente. 
#Ricorda che il grafico verrà salvato in un file alla fine.

def linear_equation (number: float, linear: str):list [float]

number = float(input("Enter the number you want the linear equation for: '"))
        #I valori x devono essere un elenco di valori compresi tra 0 e 10 (inclusi).
        #I valori y devono essere calcolati in base al tipo di funzione e al numero di ingresso n.
values_of_x = [0,1,2,3,4,5,6,7,8,9,10]
values_of_y = []

for numbers in range (values_of_x):
    number * values_of_x
    
    return values_of_y