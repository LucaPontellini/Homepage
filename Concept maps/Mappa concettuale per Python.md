# Python

## Esecuzione di file
- **Script Python**: Esegui un file Python come script.
- **Python interattivo**: Usa Python in una shell interattiva.

## Indentazione
- **Blocchi di codice**: I blocchi di codice sono denotati dall'indentazione.
- **Coerenza**: L'indentazione coerente è fondamentale in Python.

## I/O
- **print()**: Emette dati sulla console.
    - **strings**: Stampa dati di testo.
    - **numbers**: Stampa dati numerici.
    - **variables**: Stampa il valore delle variabili.
- **input()**: Legge i dati dalla console.
    - **strings**: Legge i dati di testo.
    - **conversione del tipo di dati**: Converte i dati di input nel tipo di dati richiesto.

## Variabili
- **assegnazione (=)**: Assegna un valore a una variabile.
- **nomi delle variabili**: Nomi dati alle variabili per l'identificazione.
- **variabili globali e locali**: Variabili definite nell'ambito globale e all'interno di una funzione rispettivamente.

## Commenti
- **commenti su una sola linea**: Commenti che coprono solo una linea.
- **commenti su più linee**: Commenti che coprono più linee.

## Tipi di dati
- **type()**: Ottieni il tipo di dati di una variabile.
- **Casting**:
    - **str()**: Converte una variabile in una stringa.
    - **int()**: Converte una variabile in un intero.
    - **float()**: Converte una variabile in un float.
- **str**:
    - **slicing**: Estrae parti di una stringa.
    - **len()**: Ottieni la lunghezza di una stringa.
    - **concatenazione**: Combina due stringhe.
    - **f-strings**: Formatta le stringhe in Python.
    - **caratteri di escape**: Caratteri speciali nelle stringhe.
- **bool**:
    - **True**: Valore booleano True.
    - **False**: Valore booleano False.
- **int**:
    - **operazioni aritmetiche**: Esegui calcoli con interi.
    - **confronto**: Confronta gli interi.
- **float**:
    - **operazioni aritmetiche**: Esegui calcoli con float.
    - **confronto**: Confronta i float.
- **list**:
    - **len()**: Ottieni il numero di elementi in una lista.
    - **append()**: Aggiungi un elemento alla fine di una lista.
    - **remove()**: Rimuovi un elemento da una lista.
    - **insert()**: Aggiungi un elemento in una posizione specifica in una lista.
    - **pop()**: Rimuovi un elemento da una posizione specifica in una lista.
    - **index()**: Trova l'indice di un elemento in una lista.
    - **count()**: Conta il numero di volte che un elemento appare in una lista.
    - **sort()**: Ordina gli elementi in una lista.
        - **reverse=True**: Ordina gli elementi in ordine decrescente.
        - **reverse=False**: Ordina gli elementi in ordine crescente (default).
        - **key**: Specifica una funzione di un argomento per estrarre una chiave di confronto da ciascun elemento della lista (es. `key=len` ordina una lista di stringhe per lunghezza).
    - **reverse()**: Inverti l'ordine degli elementi in una lista.
- **dict**:
    - **values()**: Ottieni tutti i valori in un dizionario.
    - **keys()**: Ottieni tutte le chiavi in un dizionario.
    - **items()**: Ottieni tutte le coppie chiave-valore in un dizionario.
    - **get()**: Ottieni il valore di una chiave specifica in un dizionario.
    - **update()**: Aggiorna il valore di una chiave specifica in un dizionario.
    - **pop()**: Rimuovi un elemento da un dizionario.
    - **clear()**: Rimuovi tutti gli elementi da un dizionario.

## Operatori
- **aritmetici**:
    - **addizione (+)**: Aggiungi due numeri.
    - **sottrazione (-)**: Sottrai un numero da un altro.
    - **moltiplicazione (*)**: Moltiplica due numeri.
    - **divisione (/)**: Divide un numero per un altro.
    - **modulo (%)**: Ottieni il resto di una divisione.
    - **esponente (**)**: Eleva un numero alla potenza di un altro.
- **di assegnazione**:
    - **assegnazione semplice (=)**: Assegna un valore a una variabile.
    - **assegnazione con operatore (+=, -=, *=, /=)**: Esegui un'operazione e assegna il risultato a una variabile.
- **di confronto**:
    - **uguale a (==)**: Controlla se due valori sono uguali.
    - **diverso da (!=)**: Controlla se due valori non sono uguali.
    - **minore di (<)**: Controlla se un valore è minore di un altro.
    - **maggiore di (>)**: Controlla se un valore è maggiore di un altro.
    - **minore o uguale a (<=)**: Controlla se un valore è minore o uguale a un altro.
    - **maggiore o uguale a (>=)**: Controlla se un valore è maggiore o uguale a un altro.
- **logici (and, or, not)**: Operatori logici.

## if...else
- **if**: Esegui un blocco di codice se una condizione è vera.
- **else**: Esegui un blocco di codice se la condizione nell'istruzione if è falsa.
- **elif**: Esegui un blocco di codice se le condizioni precedenti non erano vere.

## Cicli
- **for**: Esegui un blocco di codice per ogni elemento in una sequenza.
    - **for .. in []**: Scorri ogni elemento in una lista.
    - **for .. in {}**: Scorri ogni coppia chiave-valore in un dizionario.
    - **for .. in range()**: Scorri una sequenza di numeri.
- **while**: Esegui un blocco di codice mentre una condizione è vera.
    - **while con condizione**: Esegui un blocco di codice mentre una condizione è vera.
    - **break**: Esci prematuramente dal ciclo.
    - **continue**: Salta l'iterazione corrente e continua con la successiva.

## Funzioni
- **def**: Definisce una nuova funzione.
    - **Nome della funzione**: Identifica univocamente la funzione.
    - **Parametri**: Specifica gli input per la funzione.
    - **Corpo della funzione**: Il codice che viene eseguito quando la funzione viene chiamata.
    - **Return**: Restituisce un valore dalla funzione. Se non specificato, la funzione restituirà `None`.
    - **Docstring**: Fornisce una descrizione della funzione.

## Importazione di moduli
- **import**: Importa un modulo intero.
- **from ... import ...**: Importa specifiche funzioni o variabili da un modulo.
- **import ... as ...**: Importa un modulo con un alias.
- **from ... import ... as ...**: Importa specifiche funzioni o variabili da un modulo con un alias.

# File in Python
## File di testo
- Apertura: `open('file.txt', 'r')`
- Lettura: `f.read()`, `f.readline()`, `f.readlines()`
- Scrittura: `f.write(str)`, `f.writelines(list)`
- Chiusura: `f.close()`

## File binari
- Apertura: `open('file.bin', 'rb')` o `open('file.bin', 'wb')`
- Lettura: `f.read()`
- Scrittura: `f.write(bytes)`
- Chiusura: `f.close()`

## File CSV
- Apertura: `open('file.csv', 'r')`
- Lettura: `csv.reader(f)`
- Scrittura: `csv.writer(f).writerow(list)` o `csv.writer(f).writerows(list_of_lists)`
- Chiusura: `f.close()`

## File JSON
- Apertura: `open('file.json', 'r')`
- Lettura: `json.load(f)`
- Scrittura: `json.dump(dict, f)`
- Chiusura: `f.close()`

## File XML
- Apertura: `xml.etree.ElementTree.parse('file.xml')`
- Lettura: `tree.getroot()`
- Scrittura: `tree.write('file.xml')`

## File HTML
- Apertura: `open('file.html', 'r')`
- Lettura: `f.read()`
- Scrittura: `f.write(str)`
- Chiusura: `f.close()`

## File YAML
- Apertura: `open('file.yaml', 'r')`
- Lettura: `yaml.safe_load(f)`
- Scrittura: `yaml.safe_dump(dict, f)`
- Chiusura: `f.close()`

## File PDF
- Per lavorare con i file PDF, avrai bisogno della libreria specifica `PyPDF2`.
Questa libreria fornisce funzioni specifiche per leggere, scrivere e manipolare i file PDF.

## File DOCX
- Per i file DOCX, la libreria `python-docx` è necessaria. 
Questa libreria offre funzioni per leggere, scrivere e manipolare i file DOCX.

## File XLSX
- Per lavorare con i file XLSX, dovrai utilizzare la libreria `openpyxl`. 
Questa libreria fornisce funzioni specifiche per leggere, scrivere e manipolare i file XLSX.

## File PPTX
- Per i file PPTX, avrai bisogno della libreria `python-pptx`. 
Questa libreria offre funzioni per leggere, scrivere e manipolare i file PPTX

# Classi e Oggetti in Python

- **Classe**: Un modello per creare oggetti. Definisce attributi e metodi.
- **Oggetto**: Un'istanza di una classe.
- **Metodo**: Una funzione definita all'interno di una classe.
- **Attributo**: Una variabile definita all'interno di una classe.
- **Incapsulamento**: Raggruppa dati e metodi che lavorano sui dati all'interno di un'unica unità.
- **Ereditarietà**: Consente di creare una classe derivata che eredita gli attributi e i metodi da una classe base.
- **Polimorfismo**: Consente di trattare oggetti di diverse classi derivate come oggetti della classe base.
- **Metodi Magici**: Metodi speciali con funzionalità predefinite.
  - **`__init__`**: Inizializzatore degli oggetti (costruttore). Viene chiamato quando un'istanza della classe viene creata. Spesso usato per inizializzare gli attributi.
  - **`__str__`**: Definisce la rappresentazione stringa di un oggetto. Viene chiamato quando l'oggetto è passato a `print()` o `str()`.
  - **`__repr__`**: Definisce una rappresentazione ufficiale dell'oggetto. Viene chiamato da `repr()` e dagli ambienti interattivi come la shell di Python. Dovrebbe restituire una stringa che possa essere usata per ricreare l'oggetto.
  - **`__len__`**: Definisce il comportamento della funzione `len()` applicata all'oggetto.
  - **`__getitem__`**: Definisce il comportamento dell'indicizzazione (`[]`) sugli oggetti.
  - **`__setitem__`**: Definisce il comportamento dell'assegnazione tramite indicizzazione.
  - **`__delitem__`**: Definisce il comportamento della cancellazione di un elemento tramite indicizzazione.
  - **`__iter__`**: Definisce il comportamento dell'iterazione sugli oggetti (ad esempio, con un ciclo `for`).
  - **`__next__`**: Definisce il comportamento del passaggio all'elemento successivo in un'iterazione.

- **Getter e Setter**: Metodi per accedere e modificare gli attributi privati.
  - **Getter**: Metodo che restituisce il valore di un attributo privato.
  - **Setter**: Metodo che permette di modificare il valore di un attributo privato.

- **Decoratore `@property`**: Permette di definire metodi che si comportano come attributi.