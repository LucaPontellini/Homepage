# CRUD: Create, Read, Update, Delete

## Introduzione
CRUD è un acronimo che rappresenta le quattro operazioni fondamentali per la gestione dei dati in un sistema informatico:
- **Create** (Creazione): Inserimento di nuovi dati.
- **Read** (Lettura): Recupero di dati esistenti.
- **Update** (Aggiornamento): Modifica di dati esistenti.
- **Delete** (Eliminazione): Rimozione di dati.

## Origine del termine
Il termine CRUD è stato probabilmente reso popolare nel 1983 da James Martin nel suo libro *Managing the Data-base Environment*.

## Varianti del CRUD
Esistono diverse varianti del modello CRUD, ognuna con un focus leggermente diverso:
- **CRUDL** (Create, Read, Update, Delete, List) → Aggiunge l'operazione di **listing**, utile per visualizzare più elementi contemporaneamente.
- **BREAD** (Browse, Read, Edit, Add, Delete) → Simile a CRUD, ma enfatizza la navigazione dei dati.
- **DAVE** (Delete, Add, View, Edit) → Un'altra variante con un ordine leggermente diverso delle operazioni.
- **CRAP** (Create, Replicate, Append, Process) → Più orientato alla gestione dei dati in sistemi distribuiti.
- **FEDI** (Find, Edit, Delete, Insert) → Si concentra sulla ricerca e modifica dei dati.

## Modalità di Lettura (Read)
La lettura dei dati può avvenire in diversi modi, a seconda del contesto e delle esigenze dell'applicazione:
- **Lettura singola** → Recupero di un singolo elemento specifico.
- **Lettura multipla** → Recupero di più elementi contemporaneamente.
- **Lettura filtrata** → Recupero di elementi basati su criteri specifici.
- **Lettura paginata** → Recupero di dati suddivisi in pagine per migliorare le prestazioni.
- **Lettura in streaming** → Recupero continuo di dati, utile per applicazioni in tempo reale.
- **Lettura cache** → Recupero di dati memorizzati temporaneamente per ridurre il carico sul sistema.

## Modalità di Creazione (Create)
La creazione di dati può avvenire in diversi modi:
- **Create singolo** → Aggiunta di un solo elemento alla volta.
- **Create multiplo** → Inserimento di più elementi contemporaneamente.
- **Create condizionato** → Creazione di un elemento solo se non esiste già (ad esempio, evitare duplicati).
- **Create con validazione** → Controllo dei dati prima di inserirli per garantire che siano corretti.

## Modalità di Aggiornamento (Update)
L'aggiornamento dei dati può avvenire con diverse strategie:
- **Update singolo** → Modifica di un solo elemento.
- **Update multiplo** → Aggiornamento di più elementi contemporaneamente.
- **Update parziale** → Modifica solo di alcuni campi di un elemento senza sovrascrivere tutto.
- **Update con storico** → Creazione di una versione precedente dell'elemento prima di aggiornarlo, utile per il versioning.

## Modalità di Eliminazione (Delete)
L'eliminazione dei dati può avvenire in diversi modi:
- **Delete singolo** → Rimozione di un solo elemento.
- **Delete multiplo** → Eliminazione di più elementi contemporaneamente.
- **Delete logico** → L'elemento non viene realmente cancellato, ma solo "disattivato" (ad esempio, impostando un flag).
- **Delete fisico** → L'elemento viene completamente rimosso dal sistema senza possibilità di recupero.

## Esempio di utilizzo del CRUD:
```python
# Lista per gestire i dati
dati = []

# Creazione (Create): aggiungere un nuovo elemento
def create(elemento):
    dati.append(elemento)
    print(f"Creato: {elemento}")

# Lettura (Read): ottenere un elemento specifico
def read(elemento):
    if elemento in dati:
        print(f"Letto: {elemento}")
    else:
        print("Elemento non trovato.")

# Aggiornamento (Update): modificare un elemento
def update(vecchio_elemento, nuovo_elemento):
    if vecchio_elemento in dati:
        dati[dati.index(vecchio_elemento)] = nuovo_elemento
        print(f"Aggiornato: {vecchio_elemento} → {nuovo_elemento}")
    else:
        print("Elemento non trovato.")

# Eliminazione (Delete): rimuovere un elemento
def delete(elemento):
    if elemento in dati:
        dati.remove(elemento)
        print(f"Eliminato: {elemento}")
    else:
        print("Elemento non trovato.")

# Esempio di utilizzo delle funzioni CRUD
create("Luca")
read("Luca")
update("Luca", "Marco")
delete("Marco")
```

## Utilizzo del CRUD nelle Applicazioni

CRUD è un concetto chiave nello sviluppo software e viene applicato in diversi contesti per la gestione dei dati.

## Sviluppo Web
Tutti i **CMS** (Content Management System) e i database web utilizzano CRUD per gestire contenuti. Le operazioni CRUD sono essenziali per la gestione dei dati nei siti web e nelle applicazioni online.

## Database Management
Sistemi di database come **MySQL, PostgreSQL e MongoDB** si basano su operazioni CRUD per la manipolazione dei dati. Ogni interazione con un database, da una semplice query a operazioni più complesse, si basa su CRUD.

## Gestione dei File
La logica CRUD si applica anche alla gestione di **file di testo, documenti e altri tipi di archiviazione**. Creare un file, leggerne il contenuto, modificarlo e cancellarlo segue esattamente il modello CRUD.

## Applicazioni Mobile
Le **app per dispositivi mobili** utilizzano CRUD per gestire informazioni degli utenti, preferenze, database interni e comunicazione con server esterni.

## API REST e Microservizi
Le **API RESTful** implementano le operazioni CRUD attraverso i metodi HTTP:
- `POST` → Creazione di dati
- `GET` → Lettura di dati
- `PUT/PATCH` → Aggiornamento di dati
- `DELETE` → Eliminazione di dati

## Sistemi di Gestione delle Identità
CRUD viene utilizzato per la gestione di **utenti e permessi** nei sistemi di autenticazione, facilitando la creazione di account, la modifica dei profili e la cancellazione di utenti.

## Applicazioni di Data Science
Nella gestione di **dataset**, CRUD permette di **manipolare i dati** prima di analizzarli, facilitando operazioni come la pulizia, trasformazione e archiviazione dei dati.