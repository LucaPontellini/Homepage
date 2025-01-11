#Esercizio 6: Polimorfismo

#Obiettivo
#Creare una gerarchia di classi che rappresenti diversi tipi di pagamento in un sistema di e-commerce.
#Utilizzare il polimorfismo per definire una classe base Pagamento e classi derivate CartaDiCredito e PayPal che implementano un metodo comune processa_pagamento.

#Istruzioni
#Definisci una classe base chiamata Pagamento con un metodo processa_pagamento
#Definisci una classe derivata chiamata CartaDiCredito che eredita dalla classe Pagamento.
#Implementa il metodo processa_pagamento per gestire i pagamenti con carta di credito.
#Definisci una classe derivata chiamata PayPal che eredita dalla classe Pagamento.
#Implementa il metodo processa_pagamento per gestire i pagamenti con PayPal.
#Crea una funzione Pagamento che accetti un oggetto di tipo processa_pagamento e chiami il metodo su di esso, dimostrando il polimorfismo.

#Esempio di utilizzo
#def effettua_pagamento(metodo_di_pagamento: Pagamento):
#    metodo_di_pagamento.processa_pagamento()

#pagamento_carta = CartaDiCredito("Mario Rossi", "1234 5678 9012 3456", "12/23", "123")
#pagamento_paypal = PayPal("mario.rossi@example.com", "password123")

#effettua_pagamento(pagamento_carta)  # Output: Elaborazione pagamento con Carta di Credito per Mario Rossi
#effettua_pagamento(pagamento_paypal)  # Output: Elaborazione pagamento con PayPal per mario.rossi@example.com

class Payment:

    def process_payment(self):
        pass

class CreditCard(Payment):

    def __init__(self, name_of_the_holder, card_number, expiration, cvv):
        self.name_of_the_holder = name_of_the_holder
        self.card_number = card_number
        self.expiration = expiration
        self.cvv = cvv

    def process_payment(self):
        print(f"Credit Card payment processing for {self.name_of_the_holder}")

class PayPal(Payment):
    
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def process_payment(self):
        print(f"Payment processing with PayPal for {self.email}")

def make_payment(payment_method: Payment):
    payment_method.process_payment()

# Example usage
payment_by_card = CreditCard("Mario Rossi", "1234 5678 9012 3456", "12/23", "123")
payment_by_paypal = PayPal("mario.rossi@example.com", "password123")

make_payment(payment_by_card)  # Output: Credit Card payment processing for Mario Rossi
make_payment(payment_by_paypal)  # Output: Payment processing with PayPal for mario.rossi@example.com