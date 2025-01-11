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

def linear (n, x):
    return n * x

def polynomial (n, x):
    return x ** n

def exponential (n, x):
    return n ** x

parser = argparse.ArgumentParser (description='Plot functions.')
parser.add_argument ('--linear', action='store_true')
parser.add_argument ('--polynomial', action='store_true')
parser.add_argument ('--exponential', action='store_true')
parser.add_argument ('number', type=int)
args = parser.parse_args ()

x = np.linspace (0, 10, 100)

if args.linear:
    y = linear (args.number, x)
    plt.figure ()
    plt.plot (x, y)
    plt.title ('Linear function')
    plt.xlabel ('x')
    plt.ylabel ('y')
    plt.savefig ('linear.png')

if args.polynomial:
    y = polynomial (args.number, x)
    plt.figure ()
    plt.plot (x, y)
    plt.title ('Polynomial function')
    plt.xlabel ('x')
    plt.ylabel ('y')
    plt.savefig ('polynomial.png')

if args.exponential:
    y = exponential (args.number, x)
    plt.figure ()
    plt.plot (x, y)
    plt.title ('Exponential function')
    plt.xlabel ('x')
    plt.ylabel ('y')
    plt.savefig ('exponential.png')