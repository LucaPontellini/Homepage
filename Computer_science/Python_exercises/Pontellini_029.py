#Esercizio: Scrivi una funzione che ricevuta in ingresso una lista di dizionari contenenti le fatture di n utenti così formate:
#{"id":"id_utente",
#"importo":128.54,
#"sconto_fattura":15}
#svolga le seguenti funzioni:
#1) Aggiunga ad ogni dizionario una nuova chiave "importo_scontato" al quale associa il valore dell'importo scontato in base alla percentuale indicata alla chiave "sconto_fattura";
#2) Restituisca una lista di float dove il primo elemento è il totale degli importi e il secondo il totale degli importi scontati;
#3) Restituisca None se la lista delle fatture è vuota.

#La funzione ha la seguente signature:
#def calcola_importo(fatture:list[dict])->list[float]|None: ...... 

#Si provi la funzione in un programma dove le si dia in ingresso la seguente lista:
#fatture=[
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