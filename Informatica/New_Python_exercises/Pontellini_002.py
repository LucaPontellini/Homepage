#Esercizio 2: Classe ContoBancario con Attributo Privato

#Obiettivo
#Creare una classe chiamata ContoBancario che rappresenti un conto bancario.
#La classe deve avere tre attributi di istanza (numero_conto, intestatario) e un attributo privato (_saldo).
#Deve inoltre avere metodi pubblici per accedere e modificare il saldo.

#Istruzioni
#Definisci una classe chiamata ContoBancario.
#Aggiungi tre attributi di istanza nel metodo __init__: numero_conto, intestatario, _saldo.
#Implementa un metodo pubblico get_saldo per restituire il valore dell'attributo privato _saldo.
#Aggiungi un metodo deposita per incrementare il saldo e un metodo preleva per decrementare il saldo, assicurandoti che il saldo non diventi negativo.

# Esempio di utilizzo
#conto = ContoBancario("123456789", "Mario Rossi", 1000.0)
#print(conto.get_saldo())  # Output: 1000.0
#conto.deposita(500.0)
#print(conto.get_saldo())  # Output: 1500.0
#conto.preleva(200.0)
#print(conto.get_saldo())  # Output: 1300.0

class BankAccount:
    def __init__(self, account_number: str, account_holder: str, initial_balance: float):
        self.account_number = account_number
        self.account_holder = account_holder
        self._balance = initial_balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
        else:
            print("The deposit amount must be positive.")

    def withdraw(self, amount: float):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print("Invalid amount or insufficient balance.")

account = BankAccount("123456789", "Mario Rossi", 1000.0)
print(account.get_balance())
account.deposit(500.0)
print(account.get_balance())
account.withdraw(200.0)
print(account.get_balance())