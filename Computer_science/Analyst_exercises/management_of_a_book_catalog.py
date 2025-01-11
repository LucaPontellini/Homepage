#Esercizio: Scrivi un programma che gestisce un catalogo di libri.
#Ogni libro ha un titolo, un autore e un anno di pubblicazione.
#Il programma deve permettere all'utente di aggiungere libri al catalogo,
#visualizzare il catalogo corrente, cercare libri per titolo o autore, e rimuovere libri dal catalogo.

# Definizione di un tipo di dato per rappresentare un libro

Libro = dict[str, str]  # {'titolo': ..., 'autore': ..., 'anno': ...}

def inserisci_dati_libro() -> Libro: # type: ignore
    
    """Chiede all'utente di inserire i dati di un libro.

    Returns:
        Libro: Un dizionario contenente i dati del libro"""
    
    pass

def aggiungi_libro(catalogo: list[Libro], libro: Libro) -> list[Libro]: # type: ignore
    
    """Aggiunge un libro al catalogo dei libri.

    Args:
        catalogo (list[Libro]): Il catalogo corrente dei libri.
        libro (Libro): Il nuovo libro da aggiungere.

    Returns:
        list[Libro]: Il catalogo aggiornato dei libri"""
    
    pass

def visualizza_catalogo(catalogo: list[Libro]) -> None:
    
    """Visualizza tutti i libri nel catalogo.

    Args:
        catalogo (list[Libro]): Il catalogo corrente dei libri"""
    
    pass

def cerca_libro(catalogo: list[Libro], chiave: str) -> list[Libro]: # type: ignore
    
    """Cerca i libri nel catalogo per titolo o autore.

    Args:
        catalogo (list[Libro]): Il catalogo corrente dei libri.
        chiave (str): La chiave di ricerca (titolo o autore).

    Returns:
        list[Libro]: Una lista di libri che corrispondono alla chiave di ricerca"""
    
    pass

def rimuovi_libro(catalogo: list[Libro], libro: Libro) -> list[Libro]: # type: ignore
    
    """Rimuove un libro dal catalogo.

    Args:
        catalogo (list[Libro]): Il catalogo corrente dei libri.
        libro (Libro): Il libro da rimuovere.

    Returns:
        list[Libro]: Il catalogo aggiornato dei libri"""
    
    pass

def main() -> None:
    
    """Funzione principale che gestisce il flusso del programma per la gestione del catalogo di libri"""

    catalogo: list[Libro] = []

    nuovo_libro = inserisci_dati_libro()
    catalogo = aggiungi_libro(catalogo, nuovo_libro)

    visualizza_catalogo(catalogo)

    chiave_di_ricerca = input("Inserisci il titolo o l'autore del libro da cercare: ")
    libri_trovati = cerca_libro(catalogo, chiave_di_ricerca)
    print("Libri trovati:")
    for libro in libri_trovati:
        print(libro)

    libro_da_rimuovere = inserisci_dati_libro()
    catalogo = rimuovi_libro(catalogo, libro_da_rimuovere)

    visualizza_catalogo(catalogo)

if __name__ == "__main__":
    main()