# Classi e Oggetti in Python

## Concetti Principali

- **Classe**
  - Definizione: Una classe è un modello o schema per creare oggetti. Definisce un insieme di attributi e metodi che gli oggetti creati da essa avranno.
  - Sintassi: `class NomeClasse:`

  ## Esempio:
    ```python
    class Auto:  # Definizione della classe
        def __init__(self, marca, modello):  # Metodo costruttore
            self.marca = marca  # Attributo della classe
            self.modello = modello  # Attributo della classe
    ```

- **Oggetto**
  - Definizione: Un oggetto è un'istanza di una classe. È una rappresentazione concreta e specifica della classe, con valori propri per gli attributi definiti nella classe.
  - Creazione: `nome_oggetto = NomeClasse(parametri)`

  ## Esempio:
    ```python
    mia_auto = Auto("Toyota", "Corolla")  # Creazione di un oggetto della classe Auto
    ```

## Attributi e Metodi

- **Attributi**
  - Definizione: Gli attributi sono variabili che appartengono a un oggetto. Rappresentano le proprietà o caratteristiche dell'oggetto.

  ## Esempio:
    ```python
    class Auto:  # Definizione della classe
        def __init__(self, marca, modello):  # Metodo costruttore
            self.marca = marca  # Attributo della classe
            self.modello = modello  # Attributo della classe
    ```

- **Metodi**
  - Definizione: I metodi sono funzioni definite all'interno di una classe che descrivono i comportamenti che un oggetto può eseguire. I metodi possono manipolare gli attributi dell'oggetto.

  ## Esempio:
    ```python
    class Auto:  # Definizione della classe
        def __init__(self, marca, modello):  # Metodo costruttore
            self.marca = marca  # Attributo della classe
            self.modello = modello  # Attributo della classe

        def mostra_info(self):  # Metodo della classe
            print(f"Marca: {self.marca}, Modello: {self.modello}")  # Stampa le informazioni dell'oggetto
    ```

## Incapsulamento

- **Definizione**
  - L'incapsulamento è il principio di nascondere i dettagli interni di un oggetto e mostrare solo ciò che è necessario. Questo protegge i dati e previene l'accesso non autorizzato.

  ## Esempio:
    ```python
    class Auto:  # Definizione della classe
        def __init__(self, marca, modello):  # Metodo costruttore
            self.__marca = marca  # Attributo privato della classe
            self.__modello = modello  # Attributo privato della classe

        def mostra_info(self):  # Metodo della classe
            print(f"Marca: {self.__marca}, Modello: {self.__modello}")  # Stampa le informazioni dell'oggetto
    ```

## Ereditarietà

- **Definizione**
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
    ```

## Polimorfismo

- **Definizione**
  - Il polimorfismo permette a metodi di avere comportamenti diversi in classi derivate. Questo consente di utilizzare un'interfaccia comune per oggetti di classi diverse.

  ## Esempio:
    ```python
    class Veicolo:  # Definizione della classe base
        def mostra_info(self):  # Metodo della classe base
            print("Questo è un veicolo")

    class Auto(Veicolo):  # Definizione della classe derivata
        def mostra_info(self):  # Metodo sovrascritto nella classe derivata
            print(f"Marca: {self.marca}, Modello: {self.modello}")
    ```

## Metodi Statici

- **Definizione**
  - I metodi statici sono metodi che possono essere chiamati senza creare un'istanza della classe. Sono definiti usando il decoratore @staticmethod e non possono accedere agli attributi o metodi dell'istanza.

  ## Esempio:
    ```python
    class Utilita:  # Definizione della classe
        @staticmethod
        def saluta():  # Metodo statico
            print("Ciao!")
    ```

## Getter e Setter

### Getter

- **Definizione**: Un getter è un metodo che restituisce il valore di un attributo. Di solito viene utilizzato quando un attributo è dichiarato privato (con un nome che inizia con un `_` o `__`) per evitare un accesso diretto.

## Esempio di un getter:
  ```python
  class Studente:
      def __init__(self, nome, eta):  # Inizializza nome ed età
          self._nome = nome  # Attributo privato nome
          self._eta = eta  # Attributo privato età

      def get_eta(self):  # Getter per l'attributo 'eta'
          return self._eta  # Restituisce il valore di 'eta'
  
  # Utilizzo
  studente = Studente("Alice", 20)  # Creazione di un oggetto Studente
  print(studente.get_eta())  # Output: 20  # Stampa il valore di 'eta' tramite il getter
  ```
### Setter

- **Definizione**: Un setter è un metodo che permette di modificare il valore di un attributo privato. Come per i getter, è utile per controllare e limitare le modifiche che possono essere fatte agli attributi.

## Esempio di un setter:
  ```python
  class Studente:
      def __init__(self, nome, eta):  # Inizializza nome ed età
          self._nome = nome  # Attributo privato nome
          self._eta = eta  # Attributo privato età

      def get_eta(self):  # Getter per l'attributo 'eta'
          return self._eta  # Restituisce il valore di 'eta'

      def set_eta(self, nuova_eta):  # Setter per l'attributo 'eta'
          if nuova_eta > 0:  # Controllo sull'età positiva
              self._eta = nuova_eta  # Imposta il nuovo valore di 'eta'
          else:
              raise ValueError("L'età deve essere positiva")  # Solleva un'eccezione se l'età non è valida

  # Utilizzo del setter
  studente = Studente("Alice", 20)  # Creazione di un oggetto Studente
  studente.set_eta(25)  # Modifica il valore di 'eta' tramite il setter
  print(studente.get_eta())  # Output: 25  # Stampa il nuovo valore di 'eta' tramite il getter
  ```

## Decoratore `@property`

- **Definizione**: `property` è un tipo speciale di decoratore in Python che consente di definire metodi che si comportano come attributi. Permette di incapsulare l'accesso agli attributi e di eseguire ulteriori operazioni quando un attributo viene letto o scritto.
- **Sintassi**:
  ```python
  class NomeClasse:
      def __init__(self, attributo):
          self._attributo = attributo  # Attributo privato

      @property
      def attributo(self):  # Getter per l'attributo
          return self._attributo

      @attributo.setter
      def attributo(self, valore):  # Setter per l'attributo
          self._attributo = valore
  ```

## Esempio:
```python
class Auto:
    def __init__(self, marca, modello):
        self._marca = marca  # Attributo privato
        self._modello = modello  # Attributo privato

    @property
    def marca(self):  # Getter per l'attributo 'marca'
        return self._marca

    @marca.setter
    def marca(self, valore):  # Setter per l'attributo 'marca'
        self._marca = valore

    @property
    def modello(self):  # Getter per l'attributo 'modello'
        return self._modello

    @modello.setter
    def modello(self, valore):  # Setter per l'attributo 'modello'
        self._modello = valore

# Utilizzo
mia_auto = Auto("Toyota", "Corolla")
print(mia_auto.marca)  # Output: Toyota
mia_auto.marca = "Honda"
print(mia_auto.marca)  # Output: Honda
```

## Metodi Magici

I metodi magici, anche chiamati metodi speciali o dunder methods (per via dei doppi underscore che li circondano), sono metodi predefiniti di Python che iniziano e finiscono con due trattini bassi (`__`). Questi metodi consentono di definire comportamenti speciali per le classi e di interagire con le funzionalità interne del linguaggio. Ecco i principali:

- **`__init__`** (Costruttore): Inizializzatore degli oggetti. Viene chiamato quando un'istanza della classe viene creata. Spesso usato per inizializzare gli attributi.
  ```python
  class Classe:
      def __init__(self, attributo1, attributo2):  # Inizializza gli attributi dell'oggetto
          self.attributo1 = attributo1  # Imposta il valore dell'attributo1
          self.attributo2 = attributo2  # Imposta il valore dell'attributo2
  ```

- **`__str__`**: Definisce la rappresentazione stringa di un oggetto. Viene chiamato quando l'oggetto è passato a print() o str().
  ```python

  class Classe:
    def __str__(self):  # Ritorna una rappresentazione stringa leggibile dell'oggetto
        return f"Classe({self.attributo1}, {self.attributo2})"  # Rappresentazione della stringa
  ```

- **`__repr__`**: Definisce una rappresentazione ufficiale dell'oggetto. Viene chiamato da repr() e dagli ambienti interattivi come la shell di Python. Dovrebbe restituire una stringa che possa essere usata per ricreare l'oggetto.
  ```python

  class Classe:
    def __repr__(self):  # Ritorna una rappresentazione ufficiale e dettagliata dell'oggetto
        return f"Classe({self.attributo1}, {self.attributo2})"  # Rappresentazione dettagliata
  ```

- **`__len__`**: Definisce il comportamento della funzione len() applicata all'oggetto.
  ```python

  class Classe:
    def __len__(self):  # Ritorna la lunghezza dell'oggetto
        return 42  # Esempio di lunghezza
  ```

- **`__getitem__`**: Definisce il comportamento dell'indicizzazione ([]) sugli oggetti.
  ```python

  class Classe:
    def __getitem__(self, key):  # Ritorna il valore associato alla chiave 'key'
        return self.attributi[key]  # Accesso all'attributo tramite chiave
  ```

- **`__setitem__`**: Definisce il comportamento dell'assegnazione tramite indicizzazione.
  ```python

  class Classe:
    def __setitem__(self, key, value):  # Imposta il valore per la chiave 'key'
        self.attributi[key] = value  # Assegnazione dell'attributo tramite chiave
  ```

- **`__delitem__`**: Definisce il comportamento della cancellazione di un elemento tramite indicizzazione.
  ```python

  class Classe:
    def __delitem__(self, key):  # Elimina l'attributo associato alla chiave 'key'
        del self.attributi[key]  # Cancellazione dell'attributo tramite chiave
  ```

- **`__iter__`**: Definisce il comportamento dell'iterazione sugli oggetti (ad esempio, con un ciclo for).
  ```python

  class Classe:
    def __iter__(self):  # Ritorna un iteratore per l'oggetto
        return iter(self.attributi)  # Iteratore degli attributi
  ```

- **`__next__`**: Definisce il comportamento del passaggio all'elemento successivo in un'iterazione.
  ```python

  class Classe:
    def __next__(self):  # Ritorna l'elemento successivo nell'iterazione
        return next(self.attributi)  # Passa all'elemento successivo
  ```