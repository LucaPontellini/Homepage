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

import json

invoices = [
{"id":"Monticelli",
"amount": 245.78,
"invoice_discount": 10
},
{"id":"Kola",
"amount": 325.71,
"invoice_discount": 12
},
{"id":"Romagna",
"amount": 245.78,
"invoice_discount": 8
},
{"id":"Bilancioni",
"amount": 245.78,
"invoice_discount": 15
},
{"id":"Sanchi",
"amount": 245.78,
"invoice_discount": 5
},
{"id":"Pontellini",
"amount": 245.78,
"invoice_discount": 18
},
{"id":"Clementi",
"amount": 245.78,
"invoice_discount": 20
},
{"id":"Arlotti",
"amount": 245.78,
"invoice_discount": 19
},
{"id":"Nedria",
"amount": 245.78,
"invoice_discount": 7
},
{"id":"Santini",
"amount": 245.78,
"invoice_discount": 22
}
]

def read_json_file_as_list (file_name: str) -> list:

    '''This function reads a JSON file and returns its content as a list. If there's a problem reading the file, it returns an empty list.'''

    with open (file_name, "r") as json_file:
        try:
            mylist = json.load (json_file)
        except:
            mylist = []
    return mylist

def write_list_to_json_file (file_name: str, list_: list) -> None:
    
    """Writes a list to a JSON file"""

    with open (file_name, "w") as json_file:

        json.dump (list_, json_file, indent=4)

def show_invoices (list_: list) -> None:

    """Prints all invoices in the list"""

    for invoice in list_:
        print (invoice)

def add_invoice (invoices: list, file_name: str) -> list:

    """Adds a new invoice to the list and writes the list to a JSON file"""

    invoice_to_add = {"id": "Quattrocchi", "amount": 128.54, "invoice_discount": 15}
    invoices.append (invoice_to_add)
    write_list_to_json_file (file_name, invoices)
    return invoices

def add_discounted_amount (invoices: list, idx: int) -> list:

    """Adds a discounted amount to an invoice in the list"""

    invoices [idx]["discounted_amount"] = invoices [idx]["amount"] - (invoices [idx]["amount"] * invoices [idx]["invoice_discount"] / 100)
    return invoices

def main ():
    
    """Main function that reads invoices from a JSON file, shows them, adds a new invoice, adds a discounted amount to the first invoice, and writes the updated list back to the file"""

    file_name = "exercise_033.json"
    invoices = read_json_file_as_list (file_name)
    show_invoices (invoices)
    invoices = add_invoice (invoices, file_name)
    invoices = add_discounted_amount (invoices, 0)
    write_list_to_json_file (file_name, invoices)

if __name__ == "__main__":
    main ()