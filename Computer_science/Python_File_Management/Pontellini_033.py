#Esercizio: Scrivi un programma che letto da file JSON una lista di dizionari contenenti le fatture di n utenti così formate:

#{"id":"id_utente",
#"importo":128.54,
#"sconto_fattura":15}
#svolga le seguenti funzioni:

#1) Mostri tutte le fatture 
#2) Permetta di aggiungere ad una fattura selezionata una nuova chiave "importo_scontato" al quale associa il valore dell'importo scontato in base alla percentuale indicata alla chiave "sconto_fattura";
#3)Permetta di aggiungere una fattura alla lista (aggiornando il file JSON)

#- Definire apposite funzioni di lettura e scrittura da/sul file JSON.
#- Definire eventuali altre funzioni utili ai fini dell'esercizio.

#Si crei un file JSON di esempio copiando la seguente lista:

#fatture = [
#{"id":"Monticelli",
#"importo":245.78,
#"sconto_fattura":10
#},
#{"id":"Kola",
#"importo":325.71,
#"sconto_fattura":12
#},
#{"id":"Romagna",
#"importo":245.78,
#"sconto_fattura":8
#},
#{"id":"Bilancioni",
#"importo":245.78,
#"sconto_fattura":15
#},
#{"id":"Sanchi",
#"importo":245.78,
#"sconto_fattura":5
#},
#{"id":"Pontellini",
#"importo":245.78,
#"sconto_fattura":18
#},
#{"id":"Clementi",
#"importo":245.78,
#"sconto_fattura":20
#},
#{"id":"Arlotti",
#"importo":245.78,
#"sconto_fattura":19
#},
#{"id":"Nedria",
#"importo":245.78,
#"sconto_fattura":7
#},
#{"id":"Santini",
#"importo":245.78,
#"sconto_fattura":22
#},
#]

import os
import json

def create_a_json_file (invoices, file_name):

    """Creates a JSON file from a list of invoices"""

    with open (file_name, 'w') as f:
        json.dump (invoices, f, indent=4)

    if os.path.exists (file_name):
        print ("The JSON file has been created")
    else: print ("Failed to create the JSON file")

def read_json_file_as_list (file_name):

    """This function reads a JSON file and returns its content as a list. If there's a problem reading the file, it returns an empty list"""

    with open (file_name, "r") as json_file:
        try:
            mylist = json.load (json_file)
        except:
            mylist = []
    return mylist

def write_list_to_json_file (file_name, list_):

    """Writes a list to a JSON file"""

    with open (file_name, "w") as json_file:
        json.dump (list_, json_file, indent=4)

def show_invoices (invoices):

    """Prints all invoices in the list"""

    loop_control = False
    while not loop_control:

        answer = str (input ("Do you want to see all the invoices? "))

        if answer == "Yes":
            print ("Below are the invoices:\n")
            for invoice in invoices:
                print (invoice)
            break

        elif answer == "No":
            print ("You won't be able to see your invoices")
            while True:

                confirmation = str (input ("Are you sure you don't want to see them? "))
                if confirmation == "No":
                    print ("Understood, you will now be able to see your invoices")
                    break

                elif confirmation == "Yes":
                    print ("You won't be able to see your invoices")
                    loop_control = True
                    break

                else: print ("Error: Invalid response. Enter 'Yes' or 'No'")
        else: print ("Error: Invalid response. Enter 'Yes' or 'No'")

def add_invoice (invoices, file_name):

    """Adds a new invoice to the list and writes the list to a JSON file"""

    loop_control = False

    while not loop_control:

        print ()
        answer = str (input ("Do you want to add a new invoice? "))

        if answer == "Yes":
            number_of_invoices_to_add = int (input ("How many invoices do you want to add? "))

            for _ in range (number_of_invoices_to_add):
                id_ = str (input ("Enter the ID: "))
                amount = float (input ("Enter the amount: "))
                invoice_discount = int (input ("Enter the discounted amount: "))
                invoice_to_add = {"id": id_, "amount": amount, "invoice_discount": invoice_discount}
                invoices.append (invoice_to_add)
            write_list_to_json_file (file_name, invoices)
            break

        elif answer == "No":
            print ("You won't be able to add a new invoice")

            while True:
                confirmation = str (input ("Are you sure you don't want to add a new invoice? "))

                if confirmation == "No":
                    print ("Understood, you will now be able to add a new invoice")
                    break

                elif confirmation == "Yes":
                    print ("You won't be able to add a new invoice")
                    loop_control = True
                    break

                else: print ("Error: Invalid response. Enter 'Yes' or 'No'")
        else: print ("Error: Invalid response. Enter 'Yes' or 'No'")
    return invoices

def add_discounted_amount (invoices):

    """Adds a discounted amount to an invoice in the list"""

    loop_control = False

    while not loop_control:

        print ()
        answer = str (input ("Do you want to add a discounted amount to an invoice? "))

        if answer == "Yes":
            user_id = input ("Enter the user ID for which you want to add the discounted amount: ")

            for invoice in invoices:
                if invoice ['id'] == user_id:

                    invoice ["discounted_amount"] = invoice ["amount"] - (invoice ["amount"] * invoice ["invoice_discount"] / 100)
                    print (f"The invoice for {user_id} has been updated: {invoice}")

                    loop_control = True
                    break
            else: print ("Error: Invalid ID. Enter a valid ID")

        elif answer == "No": 
            print ("You won't be able to add a discounted amount to an invoice")

            while True:
                confirmation = str (input ("Are you sure you don't want to add a discounted amount? "))

                if confirmation == "No":
                    print ("Understood, you will now be able to add a discounted amount")
                    break

                elif confirmation == "Yes":
                    print ("You won't be able to add a discounted amount")
                    loop_control = True
                    break

                else: print ("Error: Invalid response. Enter 'Yes' or 'No'")
        else: print ("Error: Invalid response. Enter 'Yes' or 'No'")
    return invoices

def main ():

    """Main function that reads invoices from a JSON file, shows them, adds a new invoice, adds a discounted amount to the first invoice, and writes the updated list back to the file"""

    file_name = "exercise_033.json"
    
    invoices = [
    {"id":"Monticelli", "amount":245.78, "invoice_discount":10},
    {"id":"Kola", "amount":325.71, "invoice_discount":12},
    {"id":"Romagna", "amount":245.78, "invoice_discount":8},
    {"id":"Bilancioni", "amount":245.78, "invoice_discount":15},
    {"id":"Sanchi", "amount":245.78, "invoice_discount":5},
    {"id":"Pontellini", "amount":245.78, "invoice_discount":18},
    {"id":"Clementi", "amount":245.78, "invoice_discount":20},
    {"id":"Arlotti", "amount":245.78, "invoice_discount":19},
    {"id":"Nedria", "amount":245.78, "invoice_discount":7},
    {"id":"Santini", "amount":245.78, "invoice_discount":22},
    ]
    
    create_a_json_file (invoices, file_name)
    invoices = read_json_file_as_list (file_name)
    show_invoices (invoices)
    invoices = add_discounted_amount(invoices)
    invoices = add_invoice (invoices, file_name)
    write_list_to_json_file (file_name, invoices)

if __name__ == "__main__":
    main ()