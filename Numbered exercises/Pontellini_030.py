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

def generate_folder (id_: int, number_of_folders: int) -> list:
    
    """This function simulates a number of bingo cards chosen by the user"""

    folder = [[0]*9, [0]*9, [0]*9]

    for y in range (9):
        for z in range (3):
            while True:

                number = random.randint ((y*10)+1,(y+1)*10)
                number_present = False
                
                for sublist in folder:
                    if number in sublist:

                        number_present = True
                        break
                    
                if not number_present:
                    folder [z][y] = number
                    break
    
    numbers_to_remove = 12

    for t in range (numbers_to_remove):
        while True:

            row = random.randint (0,2)
            column = random.randint (0,8)

            if folder [row][column] != 0:

                folder [row][column] = 0
                break

    for y in range (9):

        column = []

        for z in range (3):

            column.append (folder [z][y])
        column.sort ()

        for z in range (3):
            folder [z][y] = column [z]

    return folder

number_of_folders = int (input ("Enter the number of folders you want to have during the game: '"))

for id_ in range (number_of_folders):

    folder = generate_folder (id_, number_of_folders)
    print (f"\nThis is your game folder: {id_}")

    for k in folder:
        print (k)

def drawn_numbers (billboard: list, numbers_drawn: list) -> list:

    """This function simulates a Tombola billboard"""
    
    while len (numbers_drawn) < 90:

        num = random.choice (billboard)
        billboard.remove (num)
        numbers_drawn.append (num)

        print ("--------------------------------------------------")
        print (f"The drawn number is: {num}.\nThe total drawn numbers are: {len (numbers_drawn)}")
        print ("--------------------------------------------------")

        while True:

            answer_1 = str (input ("Press 'Enter' to draw another number: '"))

            if answer_1 == "":
                break
            
            else: print ("Error: Invalid response. Press 'Enter' to continue")

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

#3) def controlla_cartella (cartella: dict, numeri_estratti []) -> list [bool]:
#Data come parametro una cartella e la lista di numeri estratti restituisca lo stato di tale cartella.
#Potrebbe restituire una lista di bool dove l'elemento 0 si riferisce all'ambo, l'1 al terno fino ad arrivare al 4 che si riferisce alla tombola/bingo.
#es.
#[True, True, False, False, False] per una cartella che ha fatto terno (naturalmente per fare terno bisogna aver fatto anche ambo....)

def folder_control (folder: list, numbers_drawn: []) -> list [bool]:

    for folder in range (number_of_folders):
        for z in range (3):
            while True:

                if numbers_drawn in folder:
                    if number_of_folders in folder == 2:
                        print ("You've done Ambo!")
                
                    elif number_of_folders in folder == 3:
                        print ("You've done Tern!")
                    
                    elif number_of_folders in folder == 4:
                        print ("You've done Quadruplet!")
                    
                    elif number_of_folders in folder == 5:
                        print ("You've done Five!")
                    
                    elif number_of_folders in folder == 27:
                        print ("You've done Bingo!")
                    
                    else: print ("Error")