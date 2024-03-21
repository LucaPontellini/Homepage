#Esercizio 4
#Gestione lista di dizionari
#1. Crea una lista di dizionari (gestione di una lista di contatti)
#2. Stampa la lista dei conatti. Sempre con un for, al fine di formattare meglio la stampa a video
#3. Aggiungi un nuovo contatto alla lista
#4. Modifica il numero di telefono di un contatto esistente. Fai scegliere il contatto da modificare all'utente in base al nome e al cognome passato in input
#5. Stampa la lista dei contatti aggiornata

import os

contacts = []
contact = dict()

print("1. Create a list of dictionaries (manage a contact list)\n"
      "2. Print the contact list\n"
      "3. Add a new contact to the list\n"
      "4. Change an existing contact's phone number\n"
      "5. Print the updated list and contacts")

choice = str(input("Choose the one you want: '"))

match choice:
    
    case '1':
        print("Create a list of dictionaries (manage a contact list)")

        number_of_contact = int(input("Enter the number of contacts: '"))

        for x in range (number_of_contact):

            name = str(input("Enter the name: '"))
            surname = str(input("Enter the surname: '"))
            phone_number = int(input("Enter the phone number: '"))

            contact.update()
            
            contacts.append(contact)
    
    case '2':
        print("Print the contact list")

        for contact in contacts:
            print(f"{contact}")
    
    case '3':
        print("Add a new contact to the list")

        name_ = str(input("Enter the name: '"))
        surname_ = str(input("Enter the surname: '"))
        phone_number_ = int(input("Enter the phone number: '"))

        contact.update()
    
    case '4':
        print("Change an existing contact's phone number")

        names = contact.get("name")
        surnames = contact.get("surname")
        phone_numbers = contact.get("phone_number")

        name__ = str(input("Enter the name: '"))
        surname__ = str(input("Enter the surname: '"))

        if name__ in contacts and surname__ in contacts:
            phone_number_changed = int(input("Enter the phone number you want to change: '"))

            contact.update()
        
        else: print("The contact does not exist")
    
    case '5':
        print("Print the updated list and contacts")

        for contact in contacts:
            print(f"{contacts}")
    
    case _:
        input("Press enter to continue")