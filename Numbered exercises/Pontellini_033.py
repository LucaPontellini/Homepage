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
},
]

def check_file_exist ():
    
    with open ("file_json.json","w") as file_json:

        try: mylist = json.load (file_json)
        except: mylist = []

    mylist.append (invoices)

    with open ("file_json.json","w") as file_json:
        json.dump (mylist,file_json,indent = 4)

return file_json

def creating_a_new_invoice () -> list | None:

    bills = []

    number = int (input ("How many invoices do you want to create? "))
    
    if number == 0:
        return None
    
    elif number != 0:

        for x in range (number):

            user = {"id": None,
                    "amount": None,
                    "invoice discount": None
                    }

            id = str (input ("Enter your id: "))
            amount = float (input ("Enter the amount on your invoice: "))
            invoice_discount = int (input ("Enter the discount on your invoice: "))

            discounted_amount = (amount * (100 - invoice_discount)) / 100

            user.update ({"id": id, "amount": amount, "invoice discount": invoice_discount, "discounted amount": discounted_amount})
            bills.append (user)

            print (f"{user}")

        return bills
    
    else: print ("Error")

def calculating_the_discounted_amount (bills: list [dict]) -> list [float] | None:

    if bills == []:
        return None
    
    elif bills != []:

        total_amount = 0
        total_discounted_amount = 0

        for bill in bills:

            total_amount += bill ["amount"]
            total_discounted_amount += bill ["discounted amount"]

        print (f"The total amounts are: {total_amount}.\nThe total discounted amounts are: {total_discounted_amount}")
    
    else: print ("Error")

bills = creating_a_new_invoice ()
calculating_the_discounted_amount (bills)