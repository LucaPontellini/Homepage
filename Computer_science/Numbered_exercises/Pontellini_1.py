#Esercizio 1
#Manipolazione di una lista (lista di frutti)
#1. Crea una lista con i tuoi frutti preferiti (mele, banana, uva, melone, ecc...)
#2. Stampa la lista a video utilizzando un ciclo for e non direttamente una print
#3. Aggiungi un nuovo frutto alla lista (es. kiwi)
#4. Stampa la lista aggiornata come al punto 2
#5. Rimuovi un frutto dalla lista (es. banana)
#6. Stampa la lista aggiornata come al punto 2
#7. Accedi al terzo eleemento della lista e stamapalo a video

import os

list_of_fruits = list ()

print("1. Create a list with your favorite fruits\n"
      "2. Print the list on the screen\n"
      "3. Add a new fruit to the list (e.g. kiwi)\n"
      "4. Print the updated list\n"
      "5. Remove a fruit from the list\n"
      "6. Print the updated list\n"
      "7. Go to the third item in the list and print it on the screen")

choice = str(input("Choose the one you want:"))

match choice:
    
    case '1':
        print("Create a list with your favorite fruits")

        number_of_fruit = int(input("How many fruits do you want to add to the list? '"))

        for x in range (number_of_fruit):
        
            fruit = str(input("Insert a fruit:"))

            list_of_fruits.append(fruit)
    
    case '2':
        print("Print the list on the screen")

        for fruit in list_of_fruits:
            print(list_of_fruits)
    
    case '3':
        print("Add a new fruit to the list (e.g. kiwi)")

        new_fruit = str(input("Add a new fruit to the list: '"))

        list_of_fruits.append(new_fruit)
    
    case '4':
        print("Print the updated list")
        
        for fruit in list_of_fruits:
            print(list_of_fruits)
    
    case '5':
        print("Remove a fruit from the list")

        fruit_removed = str(input("Insert the fruit to be removed: '"))

        if fruit_removed in list_of_fruits:
        
            list_of_fruits.remove(fruit_removed)

        else: print("The fruit you want to remove is not on the list")
    
    case '6':
        print("Print the updated list")
        
        for fruit in list_of_fruits:
            print(list_of_fruits)
    
    case '7':
        print("Go to the third item in the list and print it on the screen")

        third_element = str(input("Enter the index with which you can search for the fruit you want: '"))

        if third_element == 3:
        
            print(list_of_fruits[3])
        
        else: print("The table of contents you entered is invalid")

    case _:
        input("Press enter to continue")