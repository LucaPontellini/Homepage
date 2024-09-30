#Esercizio: 
#1) Leggi il file in input
#2) Calcola il prezzo scontato e aggiungetelo al dizionario come nel precedente esercizio
#3) Ordina le fatture in ordine decrescente con il prezzo scontato come criterio di ordinamento
#4) Salva la lista nel file output_json.json

import os
import json

def read_json_file_as_list (file_name):

    if os.path.exists (file_name):

        with open (file_name, "r") as json_file:
            try:
                mylist = json.load (json_file)
            except:
                mylist = []
        return mylist
    else:
        print ("File not found. Please enter a valid file name")
        return []

def write_list_to_json_file (file_name, list_):

    with open (file_name, "w") as json_file:
        json.dump (list_, json_file, indent=4)

def calculate_discounted_price (invoices):
    for invoice in invoices:

        invoice ['discounted_price'] = invoice ['amount'] * (1 - invoice ['invoice_discount'] / 100)
    return invoices

def sort_invoices (invoices):
    invoices.sort (key=lambda x: x ['discounted_price'], reverse=True)
    return invoices

def show_invoices (invoices):

    loop_control = False

    while not loop_control:

        answer = str (input ("Do you want to see all the invoices? "))
        if answer == "Yes":

            print ("Below are the invoices:\n")

            for invoice in invoices:
                print (invoice)
            break

        elif answer == "No":

            while True:
                confirmation = str (input ("Are you sure you don't want to see them? "))

                if confirmation == "No":
                    print ("Understood, you will now be able to see your invoices")
                    break

                elif confirmation == "Yes":
                    print ("You won't be able to see your invoices")
                    loop_control = True
                    break

                else: print("Error: Invalid response. Enter 'Yes' or 'No'")
        else: print("Error: Invalid response. Enter 'Yes' or 'No'")

def main ():

    input_file_name = "exercise_033.json"
    output_file_name = "output_json.json"
    invoices = read_json_file_as_list (input_file_name)

    if invoices:
        invoices = calculate_discounted_price (invoices)
        invoices = sort_invoices (invoices)
        show_invoices (invoices)
        write_list_to_json_file (output_file_name, invoices)

if __name__ == "__main__":
    main ()