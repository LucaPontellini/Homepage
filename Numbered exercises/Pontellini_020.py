#Esercizio: scrivere un programma che permetta la gestione di una lista della spesa. Esso deve prevedere un menu così formato:

#Scegli l'opzione desiderata:
#1) Visualizza lista
#2) Aggiungi item e quantità
#3) Modifica quantità di un item
#4) Rimuovi item
#5) Esci
#Scelta:_
#Per la lista della spesa si consiglia l'utilizzo di due liste, una per gli elementi una per le quantità.

shopping_list_1 = []
shopping_list_2 = []

import os

option = 0

while option != 5:

   input("Press enter to continue...")

   os.system('cls'if os.name == 'nt' else 'clear')

   print ("""
   Choose the option you want:
   1) View list
   2) Add items and quantities
   3) Change the quantity of an item
   4) Remove item
   5) Exit
   """)

   choise = input ("Choose the option you want: '")
   if choise == 1:
      print ("View list")

      for product , quantity in zip (shopping_list_1 , shopping_list_2):
        print (f"{product} : {quantity}")
      
   elif choise == 2:
      print ("Add items and quantities")
      product = str (input ("Add the product you want to add to your shopping list: '"))
      quantity = int (input ("Add the quantity you want to add to your shopping list: '"))
      shopping_list_1.append(product)
      shopping_list_2.append(quantity)

   elif choise == 3:
      print ("Changing the Quantity of an Item")
      answer_1 = str (input ("Do you want to change the quantity? '"))

      if answer_1 == "Yes":
         int (input ("Enter the new quantity: "))
         if shopping_list_2 in shopping_list_2:
            index = shopping_list_2.index (shopping_list_2)
            shopping_list_2 [index] = quantity
         else: print ("Item not found.")

      elif answer_1 == "No":
         print (shopping_list_1 , shopping_list_2) 
      else: print ("Error")

   elif choise == 4:
      print ("Remove item")
      answer_2 = str (input ("Do you want to remove item? '"))

      if answer_2 == "Yes":
         product = int (input ("Enter the item: "))
         if product in shopping_list_1:
               index = shopping_list_1.index (product)
               shopping_list_1.pop (index)
               shopping_list_2.pop (index)
         else: print("Item not found.")

      elif answer_2 == "No":
        print (shopping_list_1 , shopping_list_2) 
      else: print ("Error")

   elif choise == 5: break 
   print ("Exit")

else: print ("Error")