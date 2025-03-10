#Esercizio: #sono disponibili tre elenchi: #"prodotti", "prezzi" e "quantità". 
#L'elenco "prodotti" contiene i nomi di diversi prodotti, l'elenco "prezzi" contiene i prezzi corrispondenti di ciascun prodotto e l'elenco "quantità" contiene le quantità di ciascun prodotto.
#Il tuo compito è quello di scrivere un programma Python che esegua le seguenti operazioni:

#1. Visualizza l'inventario corrente dei prodotti con i loro prezzi e quantitativi.
#2. Chiedi all'utente un prodotto, un prezzo e una quantità. Aggiungi il prodotto, il suo prezzo e la sua quantità rispettivamente agli elenchi di prodotti, prezzi e quantità. Se il prodotto esiste già nell'elenco dei prodotti, aggiornarne il prezzo e la quantità rispettivamente negli elenchi prezzi e quantità.
#3. Chiedi all'utente un prodotto da rimuovere dall'inventario. Rimuovere il prodotto, il relativo prezzo e la relativa quantità rispettivamente dagli elenchi dei prodotti, dei prezzi e delle quantità.
#4. Visualizza l'inventario aggiornato dei prodotti con i loro prezzi e quantitativi.
#5. Calcola l'inventario totale sommando le quantità di tutti i prodotti.
#6. Calcola il valore totale delle scorte moltiplicando il prezzo di ogni prodotto per la sua quantità e sommando i risultati.

#Nota: assicurati di gestire il caso in cui l'utente tenti di rimuovere un prodotto che non esiste nell'inventario.

import os

products = []
prizes = []
quantities = []

while True:

    os.system('cls'if os.name == 'nt' else 'clear')

    print ("""
    1) View the inventory of products with their prices and quantities
    2) Add a product, a price and a quantity
    3) Remove a product from inventory
    4) View updated inventory
    5) Sum of all quantities of all products in inventory
    6) Total value of inventory""")

    choice = input ("Choose the option you want: '")

    match choice:

        case '1':
            print ("View the inventory of products with their prices and quantities")

            for product , prize , quantity in zip (products , prizes , quantities):
                print(f"{product} : €{prize} : {quantity}")

            else: print ("The inventory is empty")

        case '2':
            print ("Add a product, a price and a quantity")

            product = str (input ("Add a product: '"))
            prize = float (input ("Add a prize: '"))
            quantity = int (input ("Add a quantities: '"))

            products.append (product)
            prizes.append (prize)
            quantities.append (quantity)

        case '3':
            print ("Remove a product from inventory")

            answer_1 = str (input ("Do you want to remove a product? '"))

            if answer_1 == "Yes":
                product = input ("Enter the product: ")
                if product in products:
                    index = products.index (product)
                    products.pop (index)
                else: print("Item not found.")

            elif answer_1 == "No":
                    print (products , prizes , quantities) 
            else: print ("Error")
        
        case '4':
            print ("View updated inventory")

            for product , prize , quantity in zip (products , prizes , quantities):
                print(f"{product} : €{prize} : {quantity}")
        
        case '5':
            print ("Sum of all quantities of all products in inventory")

            for product in zip (products):
                sum_of_all_quantities_of_all_products = products + quantities
                print (f"The sum of all quantities of all products in inventory is: {sum_of_all_quantities_of_all_products}")
        
        case '6':
            print ("Total value of inventory")

            for prize , quantity in zip (prizes , quantities):
                total_value_of_inventory = float (prize * quantity) + (prize + quantity)
                print (f"The total value of inventory is: €{total_value_of_inventory}")

        case _: print("Invalid choice.")
    input("Press enter to continue...")                