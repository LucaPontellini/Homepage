#Esercizio: Write a function that receives as input a list of dictionaries containing the invoices of n users formed as follows:
#{"id":"id_utente",
#"amount":128.54,
#"sconto_fattura":15}
#performs the following functions:
#1) Add a new "importo_scontato" key to each dictionary to which it associates the value of the discounted amount based on the percentage indicated in the "sconto_fattura" key;
#2) Return a list of floats where the first element is the total amount and the second the total amount discounted;
#3) Return None if the list of invoices is empty.

#The function has the following signature:
#def calcola_importo(invoices:list[dict])->list[float]|None: ...... 

#Test the function in a program where you input the following list:

#bills = [
#{"id":"Monticelli",
#"amount":245.78,
#"invoice discount":10
#},
#{"id":"Kola",
#"amount":325.71,
#"invoice discount":12
#},
#{"id":"Romagna",
#"amount":245.78,
#"invoice discount":8
#},
#{"id":"Bilancioni",
#"amount":245.78,
#"invoice discount":15
#},
#{"id":"Sanchi",
#"amount":245.78,
#"invoice discount":5
#},
#{"id":"Pontellini",
#"amount":245.78,
#"invoice discount":18
#},
#{"id":"Clementi",
#"amount":245.78,
#"invoice discount":20
#},
#{"id":"Arlotti",
#"amount":245.78,
#"invoice discount":19
#},
#{"id":"Nedria",
#"amount":245.78,
#"invoice discount":7
#},
#{"id":"Santini",
#"amount":245.78,
#"invoice discount":22
#},
#]

user = {"id": None,
     "amount": None,
     "invoice discount": None
    }

bills = [user]

number = int (input ("How many invoices do you want to create? '"))

for x in range (number):
    
    id = int (input ("Enter your id: '"))
    amount = float (input ("Enter the discount on your invoice: '"))
    invoice_discount = int (input ("Enter the discount on your invoice: '"))

    user.update ({"id": id, "amount": amount, "invoice discount": invoice_discount})

    print (f"{user}")

    #discounted_amount

def add_a_new_key ():

    for user in bills:

        new_key = input ("")
#1) Aggiunga ad ogni dizionario una nuova chiave "importo_scontato" al quale associa il valore dell'importo scontato in base alla percentuale indicata alla chiave "sconto_fattura";
#2) Restituisca una lista di float dove il primo elemento è il totale degli importi e il secondo il totale degli importi scontati;
#3) Restituisca None se la lista delle fatture è vuota.