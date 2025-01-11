#Esercizio: Scrivi un programma che gestisce un sistema di prenotazione per un cinema.
#Il cinema ha diverse sale, ognuna con un numero diverso di posti.
#Gli utenti possono prenotare posti per uno specifico film in una specifica sala.
#Il programma deve permettere all'utente di:

#Aggiungere una sala al cinema.
#Rimuovere una sala dal cinema.
#Visualizzare tutte le sale del cinema.
#Aggiungere un film a una sala.
#Rimuovere un film da una sala.
#Visualizzare tutti i film in una sala.
#Prenotare un posto per un film in una sala.
#Annullare una prenotazione per un film in una sala.

#In questo esercizio, il cinema è rappresentato come un dizionario di tipo,
#dove ogni chiave è il nome di una sala e il valore è un altro dizionario di tipo che contiene i dettagli della sala,
#come il numero di posti disponibili e l'elenco dei film in programmazione.
#Le funzioni modificano e interagiscono con questo dizionario per gestire il cinema.

# Definizione di un tipo di dato per rappresentare un film

Film = dict[str, list[str, int]]  # type: ignore # {'titolo': ..., 'posti_prenotati': ...}

# Definizione di un tipo di dato per rappresentare una sala

Sala = dict[str, list[str, int, list[Film]]]  # type: ignore # {'nome': ..., 'posti_totali': ..., 'film': ...}

# Definizione di un tipo di dato per rappresentare un cinema
# Ogni chiave è il nome di una sala 
# e il valore è un dizionario che rappresenta i dettagli della sala.

Cinema = dict[str, Sala]

def aggiungi_sala(cinema: Cinema, sala: str, posti: int) -> Cinema: # type: ignore
    
    """Aggiunge una nuova sala al cinema.

    Args:
        cinema (Cinema): Il dizionario che rappresenta il cinema.
        sala (str): Il nome della nuova sala da aggiungere.
        posti (int): Il numero totale di posti della nuova sala.

    Returns:
        Cinema: Il dizionario aggiornato del cinema con la nuova sala aggiunta"""
    
    pass

def rimuovi_sala(cinema: Cinema, sala: str) -> Cinema: # type: ignore
    
    """Rimuove una sala dal cinema.

    Args:
        cinema (Cinema): Il dizionario che rappresenta il cinema.
        sala (str): Il nome della sala da rimuovere.

    Returns:
        Cinema: Il dizionario aggiornato del cinema con la sala rimossa"""
    
    pass

def visualizza_sale(cinema: Cinema) -> None:
    
    """Visualizza tutte le sale presenti nel cinema.

    Args:
        cinema (Cinema): Il dizionario che rappresenta il cinema.

    Returns:
        None"""
    
    pass

def aggiungi_film(cinema: Cinema, sala: str, film: str) -> Cinema: # type: ignore
    
    """Aggiunge un film alla lista dei film proiettati in una sala.

    Args:
        cinema (Cinema): Il dizionario che rappresenta il cinema.
        sala (str): Il nome della sala a cui aggiungere il film.
        film (str): Il titolo del film da aggiungere.

    Returns:
        Cinema: Il dizionario aggiornato del cinema con il film aggiunto alla sala"""
    
    pass

def rimuovi_film(cinema: Cinema, sala: str, film: str) -> Cinema: # type: ignore
    
    """Rimuove un film dalla lista dei film proiettati in una sala.

    Args:
        cinema (Cinema): Il dizionario che rappresenta il cinema.
        sala (str): Il nome della sala da cui rimuovere il film.
        film (str): Il titolo del film da rimuovere.

    Returns:
        Cinema: Il dizionario aggiornato del cinema con il film rimosso dalla sala"""
    
    pass

def visualizza_film(cinema: Cinema, sala: str) -> None:
    
    """Visualizza tutti i film proiettati in una sala specifica.

    Args:
        cinema (Cinema): Il dizionario che rappresenta il cinema.
        sala (str): Il nome della sala di cui visualizzare i film.

    Returns:
        None"""
    
    pass

def prenota_posto(cinema: Cinema, sala: str, film: str) -> Cinema: # type: ignore
    
    """Prenota un posto per un film specifico in una sala specifica.

    Args:
        cinema (Cinema): Il dizionario che rappresenta il cinema.
        sala (str): Il nome della sala in cui prenotare il posto.
        film (str): Il titolo del film per cui prenotare il posto.

    Returns:
        Cinema: Il dizionario aggiornato del cinema con il posto prenotato"""
    
    pass

def annulla_prenotazione(cinema: Cinema, sala: str, film: str) -> Cinema: # type: ignore
    
    """Annulla una prenotazione per un film specifico in una sala specifica.

    Args:
        cinema (Cinema): Il dizionario che rappresenta il cinema.
        sala (str): Il nome della sala in cui annullare la prenotazione.
        film (str): Il titolo del film per cui annullare la prenotazione.

    Returns:
        Cinema: Il dizionario aggiornato del cinema con la prenotazione annullata"""
    
    pass

def main():
    
    """Funzione principale che esegue un esempio di gestione di un cinema.

    Esegue le seguenti operazioni:
    1. Aggiunge due sale al cinema.
    2. Aggiunge diversi film alle sale.
    3. Visualizza le sale e i film presenti nel cinema.
    4. Prenota posti per vari film.
    5. Annulla una prenotazione.
    6. Visualizza i film nelle sale aggiornati con le prenotazioni.

    Returns:
        None"""
    
    cinema = {}
    cinema = aggiungi_sala(cinema, 'Sala 1', 100)
    cinema = aggiungi_sala(cinema, 'Sala 2', 50)
    cinema = aggiungi_film(cinema, 'Sala 1', 'Il Signore degli Anelli')
    cinema = aggiungi_film(cinema, 'Sala 1', 'Harry Potter')
    cinema = aggiungi_film(cinema, 'Sala 2', 'Star Wars')
    print(visualizza_sale(cinema))
    print(visualizza_film(cinema, 'Sala 1'))
    print(visualizza_film(cinema, 'Sala 2'))
    cinema = prenota_posto(cinema, 'Sala 1', 'Il Signore degli Anelli')
    cinema = prenota_posto(cinema, 'Sala 1', 'Il Signore degli Anelli')
    cinema = prenota_posto(cinema, 'Sala 1', 'Harry Potter')
    cinema = prenota_posto(cinema, 'Sala 2', 'Star Wars')
    cinema = annulla_prenotazione(cinema, 'Sala 1', 'Il Signore degli Anelli')
    print(visualizza_film(cinema, 'Sala 1'))
    print(visualizza_film(cinema, 'Sala 2'))