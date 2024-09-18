# Classi e Oggetti in Python

## Concetti Principali

- *Classe*
  - Definizione: Una classe è un modello o schema per creare oggetti. Definisce un insieme di attributi e metodi che gli oggetti creati da essa avranno.
  - Sintassi: class NomeClasse:

  ## Esempio:
    ```python
    class Auto:  # Definizione della classe
    def __init__(self, marca, modello):  # Metodo costruttore
        self.marca = marca  # Attributo della classe
        self.modello = modello  # Attributo della classe            
- *Oggetto*
  - Definizione: Un oggetto è un'istanza di una classe. È una rappresentazione concreta e specifica della classe, con valori propri per gli attributi definiti nella classe.
  - Creazione: nome_oggetto = NomeClasse(parametri)
  ## Esempio:
    ```python
    mia_auto = Auto("Toyota", "Corolla")  # Creazione di un oggetto della classe Auto
## Attributi e Metodi

- *Attributi*
  - Definizione: Gli attributi sono variabili che appartengono a un oggetto. Rappresentano le proprietà o caratteristiche dell'oggetto.
  ## Esempio:
    ```python
    class Auto:  # Definizione della classe
    def __init__(self, marca, modello):  # Metodo costruttore
        self.marca = marca  # Attributo della classe
        self.modello = modello  # Attributo della classe

- *Metodi*
  - Definizione: I metodi sono funzioni definite all'interno di una classe che descrivono i comportamenti che un oggetto può eseguire. I metodi possono manipolare gli attributi dell'oggetto.
  ## Esempio:
    ```python
    class Auto:  # Definizione della classe
    def __init__(self, marca, modello):  # Metodo costruttore
        self.marca = marca  # Attributo della classe
        self.modello = modello  # Attributo della classe

    def mostra_info(self):  # Metodo della classe
        print(f"Marca: {self.marca}, Modello: {self.modello}")  # Stampa le informazioni dell'oggetto
## Incapsulamento

- *Definizione*
  - L'incapsulamento è il principio di nascondere i dettagli interni di un oggetto e mostrare solo ciò che è necessario. Questo protegge i dati e previene l'accesso non autorizzato.
  ## Esempio:
    ```python
    class Auto:  # Definizione della classe
    def __init__(self, marca, modello):  # Metodo costruttore
        self.__marca = marca  # Attributo privato della classe
        self.__modello = modello  # Attributo privato della classe

    def mostra_info(self):  # Metodo della classe
        print(f"Marca: {self.__marca}, Modello: {self.__modello}")  # Stampa le informazioni dell'oggetto
## Ereditarietà

- *Definizione*
  - L'ereditarietà permette a una classe (classe derivata o sottoclasse) di ereditare attributi e metodi da un'altra classe (classe base o superclasse). Questo favorisce il riutilizzo del codice e la creazione di gerarchie di classi.
  ## Esempio:
    ```python
    class Veicolo:  # Definizione della classe base
        def __init__(self, tipo):  # Metodo costruttore
            self.tipo = tipo  # Attributo della classe base

    class Auto(Veicolo):  # Definizione della classe derivata
        def __init__(self, marca, modello):  # Metodo costruttore
            super().__init__("Auto")  # Chiamata al costruttore della classe base
            self.marca = marca  # Attributo della classe derivata
            self.modello = modello  # Attributo della classe derivata
## Polimorfismo

- *Definizione*
  - Il polimorfismo permette a metodi di avere comportamenti diversi in classi derivate. Questo consente di utilizzare un'interfaccia comune per oggetti di classi diverse.
  ## Esempio:
    ```python
    class Veicolo:  # Definizione della classe base
        def mostra_info(self):  # Metodo della classe base
        print("Questo è un veicolo")

    class Auto(Veicolo):  # Definizione della classe derivata
        def mostra_info(self):  # Metodo sovrascritto nella classe derivata
            print(f"Marca: {self.marca}, Modello: {self.modello}")
## Metodi Statici

- *Definizione*
  - I metodi statici sono metodi che possono essere chiamati senza creare un'istanza della classe. Sono definiti usando il decoratore @staticmethod e non possono accedere agli attributi o metodi dell'istanza.
  ## Esempio:
    ```python
    class Utilita:  # Definizione della classe
        @staticmethod
        def saluta():  # Metodo statico
            print("Ciao!")
## Esempio Completo

```python
class Auto:  # Definizione della classe
    def __init__(self, marca, modello):  # Metodo costruttore
        self.marca = marca  # Attributo della classe
        self.modello = modello  # Attributo della classe

    def mostra_info(self):  # Metodo della classe
        print(f"Marca: {self.marca}, Modello: {self.modello}")  # Stampa le informazioni dell'oggetto

mia_auto = Auto("Toyota", "Corolla")  # Creazione di un oggetto della classe Auto
mia_auto.mostra_info()  # Chiamata al metodo mostra_info dell'oggetto