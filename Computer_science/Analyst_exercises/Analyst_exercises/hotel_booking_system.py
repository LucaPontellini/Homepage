#Esercizio: Scrivi un programma che gestisce un sistema di prenotazione di hotel.
#Ogni hotel ha un nome, una località, un numero di stanze disponibili e un prezzo per notte.
#Il programma deve permettere all'utente di aggiungere hotel, visualizzare gli hotel disponibili,
#prenotare una stanza, e visualizzare le prenotazioni correnti.
#Inoltre, il programma deve gestire le prenotazioni in modo che non sia possibile prenotare una stanza se l'hotel è al completo.

# Definizione di un tipo di dato per rappresentare un hotel

Hotel = dict[str, str | int | float]  # {'nome': ..., 'località': ..., 'stanze_disponibili': ..., 'prezzo_per_notte': ...}

def inserisci_dati_hotel() -> Hotel: # type: ignore
    
    """Chiede all'utente di inserire i dati di un hotel.

    Returns:
        Hotel: Un dizionario contenente i dati dell'hotel"""
    
    pass

def aggiungi_hotel(hotel_list: list[Hotel], hotel: Hotel) -> list[Hotel]: # type: ignore
    
    """Aggiunge un hotel alla lista degli hotel.

    Args:
        hotel_list (list[Hotel]): La lista corrente degli hotel.
        hotel (Hotel): Il nuovo hotel da aggiungere.

    Returns:
        list[Hotel]: La lista aggiornata degli hotel"""
    
    pass

def visualizza_hotel(hotel_list: list[Hotel]) -> None:
    
    """Visualizza tutti gli hotel disponibili.

    Args:
        hotel_list (list[Hotel]): La lista corrente degli hotel"""
    
    pass

def prenota_stanza(hotel_list: list[Hotel], hotel: Hotel) -> list[Hotel]: # type: ignore
    
    """Prenota una stanza in un hotel specifico.

    Args:
        hotel_list (list[Hotel]): La lista corrente degli hotel.
        hotel (Hotel): L'hotel in cui si desidera prenotare una stanza.

    Returns:
        list[Hotel]: La lista aggiornata degli hotel"""
    
    pass

def visualizza_prenotazioni(prenotazioni: list[Hotel]) -> None:
    
    """Visualizza le prenotazioni correnti.

    Args:
        prenotazioni (list[Hotel]): La lista corrente delle prenotazioni"""
    
    pass

def main() -> None:
    
    """Funzione principale che gestisce il flusso del programma per la gestione delle prenotazioni di hotel"""

    hotel_list: list[Hotel] = []

    nuovo_hotel = inserisci_dati_hotel()
    hotel_list = aggiungi_hotel(hotel_list, nuovo_hotel)

    visualizza_hotel(hotel_list)

    hotel_da_prenotare = inserisci_dati_hotel()
    hotel_list = prenota_stanza(hotel_list, hotel_da_prenotare)

    visualizza_prenotazioni(hotel_list)

if __name__ == "__main__":
    main()