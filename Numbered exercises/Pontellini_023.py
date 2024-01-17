# Esercizio: Realizzare un applicativo che permetta, mediante l'uso di dizionari e liste, la gestione del catalogo di un museo. In particolare, l'applicativo dovrà permettere di:
# 1) Creare una nuova stanza (id, denominazione, metratura)
# 2) Aggiungere un opera ad una stanza (titolo, artista, anno)
# 3) Consultare le opere presenti in una stanza
# 4) Consultare le stanze presenti
# 5) Cercare le informazioni su un opera
# 6) Cancellare un opera
# 7) Cancellare una stanza solo se vuota

# NB:
# - Progettare la struttura dati a priori in modo da garantire le funzionalità richieste.
# - Fare in modo che il museo sia inizialmente vuoto e popolabile da applicativo.
# - Realizzare un menù numerato con le varie funzionalità elencate in precedenza.
# - Controllare la presenza della stanza e/o dell'opera prima di aggiungerla.

import os

museum = []

while True:
    os.system("cls" if os.name == "nt" else "clear")

    print(
        """ 
    1) Create a new room (id, name, square footage)
    2) Add a work to a room (title, artist, year)
    3) Consult the works in a room
    4) Consult the rooms present
    5) Search for information about a work
    6) Deleting an artwork
    7) Delete a room only if it is empty"""
    )

    choice = input ("Choose the option you want: '")

    match choice:

        case "1":
            print ("Create a new room (id, name, square footage)")

            print (f"{museum}")
            
            create_new_rooms = str (input ("Do you want to create a new room? '"))
            
            if create_new_rooms == "Yes":

                number_of_rooms = int (input ("How many rooms do you want to create? '"))

                for x in range (number_of_rooms):

                    id_room_1 = int (input ("Enter the room ID: '"))
                    name_room_1 = str (input ("Enter the name of the room: '"))
                    square_footage_room_1 = float (input ("Enter the square footage of the room: '"))

                    museum.append ({"id": id_room_1, "name": name_room_1, "square": square_footage_room_1, "artworks": [],})

                    print (f"You have created {number_of_rooms} rooms")

                    for room in museum:

                        print ("-----------------------------------------------")
                        print (f"Id: {room ['id']}")
                        print (f"Name: {room ['name']}")
                        print (f"Square: {room ['square']}")
                        print (f"Artworks: {room ['artworks']}")
                        print ("-----------------------------------------------")
            
            elif create_new_rooms == "No":
                
                print (f"{museum} No rooms have been created")
                
                while True:

                    confirmation_1 = str (input ("Are you sure you don't want to create a room? '"))

                    if confirmation_1 == "No":

                        print ("You won't be able to create a room")
                        break

                    elif confirmation_1 == "Yes":

                        print ("You will be able to create a room if you press 1")
                        break

                    else: print ("Error: Invalid response. Enter 'Yes' or 'No'")
            
            else: print ("Error: Invalid response. Enter 'Yes' or 'No'")

        case "2":
            print ("Add a artwork to a room (title, artist, year)")

            artwork_to_room = str (input ("Do you want to add a artwork to a room (title, artist, year)? '"))

            if artwork_to_room == "Yes":
            
                room_id = int (input ("In which room do you want to add the artworks?\n Enter the room ID: '")) 
                print(f"{museum}")

                room_exists = False
                for room in museum:
                    if room ['id'] == room_id:
                        room_where_to_add_artwork = room
                        room_exists = True
                        break
                    
                if room_exists == False:
                    print (f"room with id {room_id} does not exists")

                elif room_exists == True:

                    while True:
                        title = input("Enter the title: ")
                        artist = input("Enter the artist: ")
                        year = int(input("Enter the year: ")) 

                        temp_artwork = {}
                        temp_artwork ["title"] = title
                        temp_artwork ["artist"] = artist
                        temp_artwork ["year"] = year

                        list_of_artworks_in_the_room = room_where_to_add_artwork ['artworks']
                        artwork_exists = False
                        for artwork in list_of_artworks_in_the_room:
                            if artwork ['title'] == title:
                                artwork_exists = True
                                break                
                            
                        if artwork_exists == False:
                            list_of_artworks_in_the_room.append (temp_artwork)
                            break
                        else: 
                            print (f"artwork with name {title} already exists")

            elif artwork_to_room == "No":
                print (f"{museum} No rooms have been created")

                while True:

                    confirmation_2 = str (input ("Are you sure you don't want to add an artwork? '"))

                    if confirmation_2 == "No":
                        print ("You won't be able to add an artwork")
                        break

                    elif confirmation_2 == "Yes":
                        print ("You will be able to add an artwork if you press 2")
                        break

                    else: 
                        print ("Error: Invalid response. Enter 'Yes' or 'No'")
                        break
            
            else: print ("Error: Invalid response. Enter 'Yes' or 'No'")

        case "3":
            print("Consult the works in a room")

            consult_works = str (input ("Do you want to consult the works in a room? '"))

            if consult_works == "Yes":

                id_room = int (input ("Enter the room ID: "))
                room_exists = False

                for room in museum:

                    if room ['id'] == id_room:
                        room_exists = True

                        print (f"Artworks in room {id_room}: {room ['artworks']}")
                        break

                if room_exists == False:
                    print (f"Room with id {id_room} does not exist")

            elif consult_works == "No":
                print ("You chose not to consult the works in a room")

                while True:

                    confirmation_3 = str (input ("Are you sure you don't want to consult the works in a room? '"))

                    if confirmation_3 == "No":
                        print ("You won't be able to consult the works in a room")
                        break

                    elif confirmation_3 == "Yes":
                        print ("You will be able to consult the works in a room if you press 3")
                        break

                    else: 
                        print ("Error: Invalid response. Enter 'Yes' or 'No'")
                        break

            else: print ("Error: Invalid response. Enter 'Yes' or 'No'")

        case "4":
            print ("Consult the rooms present")

            consult_rooms = str (input ("Do you want to consult the rooms present? '"))

            if consult_rooms == "Yes":

                print ("Rooms in the museum:")

                for room in museum:

                    print ("-----------------------------------------------")
                    print (f"Id: {room ['id']}")
                    print (f"Name: {room ['name']}")
                    print (f"Square: {room ['square']}")
                    print ("-----------------------------------------------")

            elif consult_rooms == "No":
                print ("You chose not to consult the rooms present")

                while True:

                    confirmation_4 = str (input ("Are you sure you don't want to consult the rooms present? '"))

                    if confirmation_4 == "No":
                        print("You won't be able to consult the rooms present")
                        break

                    elif confirmation_4 == "Yes":
                        print("You will be able to consult the rooms present if you press 4")
                        break

                    else:
                        print("Error: Invalid response. Enter 'Yes' or 'No'.")

            else: print("Error: Invalid response. Enter 'Yes' or 'No'.")

        case "5":
            print ("Search for information about a work")

            search_work = str (input ("Do you want to search for information about a work? "))

            if search_work == "Yes":

                title = str (input ("Enter the title of the artwork: '"))

                artwork_exists = False

                for room in museum:

                    for artwork in room ['artworks']:

                        if artwork ['title'] == title:

                            artwork_exists = True

                            print (f"Information about the artwork {title} : {artwork}")
                            break

                    if artwork_exists:
                        break

                if artwork_exists == False:

                    print (f"Artwork with title {title} does not exist")

            elif search_work == "No":

                print ("You chose not to search for information about a work")

                while True:

                    confirmation_5 = str (input ("Are you sure you don't want to search for information about a work? '"))

                    if confirmation_5 == "No":
                        print ("You won't be able to search for information about a work")
                        break

                    elif confirmation_5 == "Yes":
                        print ("You will be able to search for information about a work if you press 5")
                        break

                    else:
                        print("Error: Invalid response. Enter 'Yes' or 'No'.")

            else: print ("Error: Invalid response. Enter 'Yes' or 'No'")

        case "6":
            print ("Deleting an artwork")

            delete_artwork = str (input ("Do you want to delete an artwork? '"))

            if delete_artwork == "Yes":

                id_room = int (input ("Enter the room ID: '"))
                title = str (input ("Enter the title of the artwork: '"))

                room_exists = False

                for room in museum:

                    if room ['id'] == id_room:

                        room_exists = True
                        artwork_exists = False

                        for artwork in room ['artworks']:

                            if artwork ['title'] == title:

                                artwork_exists = True
                                room ['artworks'].remove (artwork)
                                print (f"You have deleted the artwork {title} from the room {id_room}")
                                break

                        if artwork_exists == False:

                            print (f"Artwork with title {title} does not exist in the room")
                            break

                if room_exists == False:

                    print (f"Room with id {id_room} does not exist")

            elif delete_artwork == "No":
                 
                print ("You chose not to delete an artwork")

                while True:

                    confirmation_6 = str (input ("Are you sure you don't want to delete an artwork? '"))

                    if confirmation_6 == "No":
                        print("You won't be able to delete an artwork")
                        break

                    elif confirmation_6 == "Yes":
                        print("You will be able to delete an artwork if you press 6")
                        break

                    else:
                        print("Error: Invalid response. Enter 'Yes' or 'No'.")

            else: print ("Error: Invalid response. Enter 'Yes' or 'No'")

        case "7":
            print ("Delete a room only if it is empty")

            delete_room = str (input ("Do you want to delete a room only if it is empty? '"))

            if delete_room == "Yes":

                id_room = int (input ("Enter the room ID: '"))

                room_exists = False

                for room in museum:

                    if room ['id'] == id_room:

                        room_exists = True

                        if not room ['artworks']:

                            museum.remove (room)

                            print (f"You have deleted the room {id_room}")

                        else: print("The room is not empty.")
                        break

                if room_exists == False:

                    print (f"Room with id {id_room} does not exist")

            elif delete_room == "No":

                print ("You chose not to delete a room")

                while True:

                    confirmation_7 = str (input ("Are you sure you don't want to delete a room? '"))

                    if confirmation_7 == "No":
                        print ("You won't be able to delete a room")
                        break

                    elif confirmation_7 == "Yes":
                        print ("You will be able to delete a room if you press 7")
                        break

                    else:
                        print ("Error: Invalid response. Enter 'Yes' or 'No'")

            else: print ("Error: Invalid response. Enter 'Yes' or 'No'")

        case _:
            print("Invalid choice.")
    input("Press enter to continue...")