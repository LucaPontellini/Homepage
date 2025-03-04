import threading

# Classe ContoBancarioCondiviso che rappresenta un conto bancario condiviso tra più thread
class ContoBancarioCondiviso:
    def __init__(self, saldo_iniziale=0):
        self.saldo = saldo_iniziale  # Imposta il saldo iniziale del conto
        self.lock = threading.Lock()  # Crea un oggetto Lock per garantire l'accesso esclusivo al saldo

    def deposita(self, amount):
        self.lock.acquire()  # Acquisisce il lock prima di modificare il saldo
        self.saldo += amount  # Aggiunge l'importo depositato al saldo
        print(f"Deposito di {amount}. Saldo attuale: {self.saldo}")  # Stampa il saldo attuale dopo il deposito
        self.lock.release()  # Rilascia il lock dopo aver terminato la modifica del saldo

    def preleva(self, amount):
        self.lock.acquire()  # Acquisisce il lock prima di modificare il saldo
        if self.saldo >= amount:
            self.saldo -= amount  # Sottrae l'importo prelevato dal saldo se sufficiente
            print(f"Prelievo di {amount}. Saldo attuale: {self.saldo}")  # Stampa il saldo attuale dopo il prelievo
        else:
            print(f"Prelievo di {amount} fallito. Saldo insufficiente: {self.saldo}")  # Stampa un messaggio di errore se il saldo è insufficiente
        self.lock.release()  # Rilascia il lock dopo aver terminato la modifica del saldo

# Funzione per eseguire operazioni bancarie su un conto condiviso
def operazioni_bancarie(conto, operazioni):
    for op in operazioni:  # Itera attraverso la lista delle operazioni
        if op[0] == 'deposita':
            conto.deposita(op[1])  # Esegue l'operazione di deposito
        elif op[0] == 'preleva':
            conto.preleva(op[1])  # Esegue l'operazione di prelievo

# Creazione del conto bancario condiviso con un saldo iniziale di 100
conto = ContoBancarioCondiviso(100)

# Elenco delle operazioni da eseguire nel primo thread
operazioni1 = [('deposita', 50), ('preleva', 30), ('preleva', 120)]

# Elenco delle operazioni da eseguire nel secondo thread
operazioni2 = [('preleva', 20), ('deposita', 100), ('preleva', 50)]

# Creazione dei thread per eseguire le operazioni bancarie con i nomi utente1 e utente2
utente1 = threading.Thread(target=operazioni_bancarie, args=(conto, operazioni1))
utente2 = threading.Thread(target=operazioni_bancarie, args=(conto, operazioni2))

# Avvio dei thread
utente1.start()
utente2.start()

# Attesa del completamento dei thread
utente1.join()
utente2.join()

# Stampa il saldo finale del conto dopo che entrambi i thread hanno completato le operazioni
print(f"Saldo finale del conto: {conto.saldo}")