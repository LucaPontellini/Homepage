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
list_of_what_you_can_do = ["If you touch '1', you can see the list;\n If you touch '2', you can add items and quantities to lists;\n If you touch '3', you can modifying the quantities of an item; "]
list = 0

print ("What you want to do?")

print (shopping_list_1)
print (shopping_list_2)
print ("There is nothing on the list")

while list == 0:
   product = str (input ("Add the product you want to add to your shopping list: '"))
   quantity = int (input ("Add the product you want to add to your shopping list: '"))

   shopping_list_1.append (product)
   shopping_list_2.append (quantity)

   answer = str (input ("Do you want to edit a list? '"))

   if answer == "Yes":
      shopping_list_1 = shopping_list_1.append (product)
      print (shopping_list_1)
   elif answer == "No":
      print (shopping_list_1) 
   elif answer == "Yes":
      shopping_list_2 = shopping_list_2.append (quantity)
      print (shopping_list_2)
   elif answer == "No":
      print (shopping_list_2)
   else: print ("Error")


FANCULO