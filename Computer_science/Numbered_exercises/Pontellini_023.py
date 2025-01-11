#Esercizio: Realizzare un applicativo che permetta, mediante l'uso di dizionari e liste, la gestione del catalogo di un museo. In particolare, l'applicativo dovrà permettere di:
#1) Creare una nuova stanza (id, denominazione, metratura) 
#2) Aggiungere un opera ad una stanza (titolo, artista, anno)
#3) Consultare le opere presenti in una stanza
#4) Consultare le stanze presenti
#5) Cercare le informazioni su un opera
#6) Cancellare un opera
#7) Cancellare una stanza solo se vuota
 
#NB:
#- Progettare la struttura dati a priori in modo da garantire le funzionalità richieste.
#- Fare in modo che il museo sia inizialmente vuoto e popolabile da applicativo.
#- Realizzare un menù numerato con le varie funzionalità elencate in precedenza.
#- Controllare la presenza della stanza e/o dell'opera prima di aggiungerla.

import os

museum = []

room_1 = {"ID" : "there is no room ID",
        "name" : "the name of the room is not specified",
        "square footage" : "there is no square footage of the room",
        "work" : "there is no artwork in the room"
}

rooms = []

work = {"title" : "there is no title related to the work",
        "artist" : "no artist name is present",
        "year" : "the year of the work is not present"
}

works = []

while True:

    os.system ('cls'if os.name == 'nt' else 'clear')

    print (""" 
    1) Create a new room (id, name, square footage)
    2) Add a work to a room (title, artist, year)
    3) Consult the works in a room
    4) Consult the rooms present
    5) Search for information about a work
    6) Deleting an artwork
    7) Delete a room only if it is empty""")

    choice = input ("Choose the option you want: '")

    match choice:
#trova un modo per cambiare iteratore dal dizionario delle stanze perchè si soverascrivono i valori del dizionario
        case '1':
            print ("Create a new room (id, name, square footage)")

            print (f"{rooms}")
            
            if rooms == []:
                print (f"{museum}. There are no rooms in the museum")

                answer = int (input ("How many rooms do you want to create? '"))

                for answer in range (answer):

                    answer_1 = str (input ("Are you sure you want to create a new room? '"))
            
                    if answer_1 == "Yes":
                    
                        id_room_1 = (input ("Enter the room ID: '"))
                        name_room_1 = (input ("Enter the name of the room: '"))
                        square_footage_room_1 = (input ("Enter the square footage of the room: '"))

                        room_1 ["ID"] = id_room_1
                        room_1 ["name"] = name_room_1
                        room_1 ["square footage"] = square_footage_room_1

                        rooms.append (room_1)

                        print (f"{rooms}")
                
                    elif answer_1 == "No":
                        print (f"{rooms}")
                        break

                    else: print (f"{rooms}")
                
            elif rooms != []:
                print (f"{museum}. There are rooms in the museum")
                
            else: print ("Error")

        case '2':
            print ("Add a work to a room (title, artist, year)")

            print (f"{works}")

            if works == []:
                print (f"{room_1}")

                answer_2 = int (input ("How many artworks do you want to add to a room? '"))

                for answer_2 in range (answer_2):

                    answer_3 = str (input ("Do you want to add a work to a room? '"))

                    if answer_3 == "Yes":

                        answer_9 = str (input ("In which room do you want to add the artworks?\n Enter the room ID: '"))

                        if answer_9 == room_1 ["ID"]:

                            title = input ("Enter the title: '")
                            artist = input ("Enter the artist: '")
                            year = input ("Enter the year: '")

                            work ["title"] = title
                            work ["artist"] = artist
                            work ["year"] = year

                            works.append (work)

                            print (f"{works}")
                    
                        else: print ("The room ID doesn't match or doesn't exist")

                    elif answer_3 == "No":
                        print (f"{works}")
                        break

                    else: print (f"{works}")
                
                if answer_2 == answer_2:
                        print (f"This is the list of rooms in the museum: {rooms}")

                        if answer != room_1 ["ID"] and room_1 in (museum): #il programma va in errore
                            print ("There are no rooms in the museum where you can see the works")
                        
                        elif answer == room_1 ["ID"]:

                            for answer in range (answer): #gesisci l'errore se non sono presenti dele stanze perchè blocca il programma

                                answer_4 = str (input ("Where do you want to place the works?\n Enter the name of the room: '"))

                                if room_1 in rooms:

                                    room_1.update ({"name" : answer_4})

                                    for room_1 in rooms ():
                                        room_1 ["work"] = work

                                        print (f"You added this artwork to the room: {work}")
                                        print (f"{room_1}")
                                #prendi l'ID della stanza su cui vuoi aggiungere l'opera. Dopo aver preso l'ID, aggiungi l'opera alla stanza
                                else: print ("The name of the room or the room itself does not exist.\n To check this, click on option 4 in the menu")

                        else: print ("Error")

                else: print ("Error")
                
            elif works != []:
                print (f"{room_1}")

            else: print ("Error")

#stampa tutti gli ID delle stanze per poi stampare le opere pesenti nelle stanze
        case '3':
            print ("Consult the works in a room")

            room_1 ["ID"] = id_room_1

            print (f"This is the list of rooms in the museum: {rooms}")
            print (f"This is the list of all room IDs: {id_room_1}")

            answer_5 = str (input ("In which room do you want to see the works of?\n Enter the room ID: '"))

            for id_room_1 in range (rooms): #Riformula la condizione del ciclo
                if id_room_1 == answer_5:
                    print (f"{room_1}")
                else: print ("Room not found")

        case '4':
            print ("Consult the rooms present")

            print (f"This is the list of rooms in the museum: {rooms}")
#cerca le informazioni di un'opera. Per farlo stampa tutte le opere        
        case '5':
            print ("Search for information about a work")

            print (f"This is the list of all the works: {works}")

            answer_6 = str (input ("Which work do you want to know about?\n Enter the work you want to know about: '"))
#cancella un'opera. Per farlo prendi le opere e chiedi quale vuole essere eliminata        
        case '6':
            print ("Deleting an artwork")
#elimina le stanze se sono vuote        
        case '7':
            print ("Delete a room only if it is empty")

            if rooms == []:

                answer_7 = str (input ("Are you sure you want to delete a room? '"))

                if answer_7 == "Yes":

                    print (f"This is the list of rooms in the museum: {rooms}")

                    answer_8 = str (input ("Which room do you want to delete?\n Enter the name of it: '"))

                    del rooms

        case _: print("Invalid choice.")
    input("Press enter to continue...")