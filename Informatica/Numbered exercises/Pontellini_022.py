#Esercizio: 
#Attività 1: Creare un dizionario
#Inizia creando un dizionario. Questo dizionario dovrebbe rappresentare un libro. Utilizzare tasti come , , e , e assegnare loro i valori appropriati.title_author_year_published
#Attività 2: Aggiungere un elemento
#Aggiungere una nuova coppia chiave-valore al dizionario. La chiave dovrebbe essere e il valore dovrebbe essere qualsiasi genere a tua scelta.genre
#Attività 3: Modificare un elemento
#Modificare il valore di una delle chiavi esistenti nel dizionario. Ad esempio, è possibile modificare il valore della chiave in un anno diverso.year_published
#Attività 4: Eliminare un elemento
#Rimuovere una coppia chiave-valore dal dizionario. Ad esempio, è possibile rimuovere la chiave.author
#Attività 5: Scorrere il dizionario
#Scrivi tre cicli separati:
#Uno per stampare tutte le chiavi
#Uno per stampare tutti i valori
#Uno per stampare tutte le coppie chiave-valore (elementi) nel dizionario
#Ricorda, i metodi del dizionario di Python , , e saranno utili in questo compito.keys()values()items()

import os

book = {"title" : "there is no title",
        "author" : "unknown",
        "year_published" : "unknown"
        }

while True:

    os.system ('cls'if os.name == 'nt' else 'clear')

    print (""" 
    1) Create a dictionary
    2) Add an item
    3) Edit an item
    4) Delete an item
    5) Scroll through the dictionary""")

    choice = input ("Choose the option you want: '")

    match choice:

        case 1:
            print ("Create a dictionary")

            book = {"title" : "there is no title",
            "author" : "unknown",
            "year_published" : "unknown"
            }
        
        case 2:
            print ("Add an item")

            item = str (input ("Add a item: '"))
            book ["gender"] = item
            print (book)

        case 3:
            print ("Edit an item")

            answer_1 = str (input ("Do you want to change an item? '"))

            if answer_1 == "Yes":
                item = input ("Enter the item: ")

                if item in book:

                    new_tile = str (input ("Enter the title: "))
                    new_author = str (input ("Enter the author: "))
                    new_year_published = int (input ("Enter the year published: "))

                    new_key_1 = book.get ("title")
                    new_tiles = book ["title"] = new_tile

                    new_key_2 = book.get ("author")
                    new_authors = book ["author"] = new_author

                    new_key_3 = book.get ("year_published")
                    new_years_published = book ["year_published"] = new_year_published

                    print (book) 
                else: print("Item not found.")

            elif answer_1 == "No":
                    print (book) 
            else: print ("Error")
        
        case 4:
            print ("Delete an item")

            answer_2 = str (input ("Do you want to change an item? '"))

            if answer_2 == "Yes":
                item = input ("Enter the item: ")

                if item in book:
                    title_to_remove = str (input ("Enter the title: "))
                    author_to_remove = str (input ("Enter the author: "))
                    year_published_to_remove = int (input ("Enter the year published: "))
                    
                    new_key_1 = book.get ("title")
                    new_key_2 = book.get ("author")
                    new_key_3 = book.get ("year_published")

                    book.pop ("title")
                    book.pop ("author")
                    book.pop ("year_published")

                    print(book)

                else: print("Item not found.")

            elif answer_2 == "No":
                    print (book) 
            else: print ("Error")

        case 5:
            print ("Scroll through the dictionary")
        
            print (book)
        
        case _: print("Invalid choice.")
    input("Press enter to continue...")