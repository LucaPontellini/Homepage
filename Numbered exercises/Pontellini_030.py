#Esercizio: sulla base di quanto visto a lezione sul modulo random realizzare un programma che implementi il gioco della tombola o del bingo.
#Al fine di far ciò, lo studente implementi le seguenti funzioni:
#1) def genera_cartella (id: int <str>) -> dict:
#La funzione genera una cartella della tombola/bingo e la restituisce come dizionario. Dare un id alla cartella.
#N.B.
#La cartella ha le seguenti caratteristiche:
#1) 3 righe e 9 colonne
#2) 15 numeri in totale (5 per riga)
#3) ogni colonna ha solo i numeri della decina di riferimento: la prima dall'1 al 10, la seconda dal 11 al 20....l'ultima dall'81 al 90

#2) def estrai_numero (numeri_estratti: list []) -> int:
#La funzione estrae un nuovo numero, lo inserisce nella lista passata come parametro, controllando che non sia duplicato, e restituisce tale numero come intero.

#3) def controlla_cartella (cartella: dict, numeri_estratti []) -> list [bool]:
#Data come parametro una cartella e la lista di numeri estratti restituisca lo stato di tale cartella.
#Potrebbe restituire una lista di bool dove l'elemento 0 si riferisce all'ambo, l'1 al terno fino ad arrivare al 4 che si riferisce alla tombola/bingo.
#es.
#[True, True, False, False, False] per una cartella che ha fatto terno (naturalmente per fare terno bisogna aver fatto anche ambo....)

#Realizzare un programma che implementi la logica di funzionamento:
#a) Utilizzando le opportune variabili di stato (es. una lista di cartelle, la lista dei numeri estratti, lo stato del gioco(ambo, terno,....))
#b) Utilizzando le funzioni precedentemente definite al fine di gestire le varie fasi del gioco.

import random
    
    #crea una lista con le caratteristiche della cartella da cui si prende in modo casuale un numero per ogni colonna
    #usa un random per pescare i numeri da mettere nella tabella
    #trova un modo per stampare ordinatamente la cartella con tutti i numeri all'interno tramite un ciclo che varia con il numero delle cartelle

#La cartella ha le seguenti caratteristiche:
#1) 3 righe e 9 colonne
#2) 15 numeri in totale (5 per riga)
#3) ogni colonna ha solo i numeri della decina di riferimento: la prima dall'1 al 10, la seconda dal 11 al 20....l'ultima dall'81 al 90

#random.randint (1, 90) #usalo per pescare 15 numeri
#total_number = 90

import random

def generate_folder (id_: int, number_of_the_folders: int) -> list:

    folder = []

    for y in range (15):
        while True:

            num = random.randint (1, 90)

            if num not in folder:
                folder.append (num)
                break

    folder.sort ()

    print (f"This is your game folder: {id_}: {folder}")
    return folder

number_of_the_folders = int(input("Enter the number of folder you want to have during the game: '"))

for id_ in range(number_of_the_folders):
    generate_folder(id_, number_of_the_folders)

#trova un modo per disporre i numeri in tre liste in modo tale da formare una sorta di tabella:
#[                          ]
#[                          ]
#[                          ]
#una cosa così deve risultare in output

def drawn_numbers (billboard: list, numbers_drawn: list) -> list:
    
    while len (numbers_drawn) < 90:

        num = random.choice (billboard)
        billboard.remove (num)
        numbers_drawn.append (num)

        print ("--------------------------------------------------")
        print (f"The drawn number is: {num}.\nThe total drawn numbers are: {len (numbers_drawn)}")
        print ("--------------------------------------------------")
    
    return numbers_drawn

list_1 = [1,2,3,4,5,6,7,8,9,10]
list_2 = [11,12,13,14,15,16,17,18,19,20]
list_3 = [21,22,23,24,25,26,27,28,29,30]
list_4 = [31,32,33,34,35,36,37,38,39,40]
list_5 = [41,42,43,44,45,46,47,48,49,50]
list_6 = [51,52,53,54,55,56,57,58,59,60]
list_7 = [61,62,63,64,65,66,67,68,69,70]
list_8 = [71,72,73,74,75,76,77,78,79,80]
list_9 = [81,82,83,84,85,86,87,88,89,90]
    
billboard = list_1 + list_2 + list_3 + list_4 + list_5 + list_6 + list_7 + list_8 + list_9
numbers_drawn = []
    
drawn_numbers (billboard, numbers_drawn)

#massimo = 3 numeri per ogni lista
#minimo = 1 numero per ogni lista         
#pesca 15 numeri dal dizionario dict_ contenente le liste

#dei 90 numeri, tramite un ciclo, ne peschi 15 a caso e li metti nella cartella
#dizionario = chiave, valore