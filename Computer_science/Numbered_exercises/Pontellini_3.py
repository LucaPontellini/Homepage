#Esercizio 3
#Gestione di dizionari con campi di tipo lista (gestione di una lista di attività per ciascun giorno della settimana)
#1. Crea un dizionario per rappresentare le attività pianificate per ogni giorno della settimana. 
#I giorni sono la chiave e una lista di attività è il valore ad essa associata
#2. Stampa la pianificazione settimanale. Sempre utilizzando un for, al fine di formattare meglio la stampa
#3. Aggiungi un'attività per il sabato (es. "Escursione")
#4. Stampa la pianificazione settimanale aggiornata

import os

activitys = {}

print("1. Create a dictionary to represent the tasks scheduled for each day of the week\n"
      "2. Print the weekly schedule\n"
      "3. Add an activity for Saturday\n"
      "4. Print the updated weekly schedule\n")

choice = str(input("Choose the one you want:"))

match choice:
    
    case '1':
        print("Create a dictionary to represent the tasks scheduled for each day of the week")

        activitys = dict (monday = "None" , tuesday = "None", wednesday = "None", thursday = "None", friday = "None")
    
    case '2':
        print("Print the weekly schedule")

        print(f"{activitys}")
    
    case '3':
        print("Add an activity for Saturday")

        #number_of_activity = int(input("Enter the number of activities you want to do: '"))

        #for x in range (number_of_activity):
            
        activity_for_saturday = str(input("Enter an activity for the saturday: '"))

        activitys ["saturday"] = activity_for_saturday

        activitys.update()
    
    case '4':
        print("Print the updated weekly schedule")

        for activity in activitys:
            print(f"{activitys}")
    
    case _:
        input("Press enter to continue")