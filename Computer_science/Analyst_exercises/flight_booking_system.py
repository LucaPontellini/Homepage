#Esercizio: Scrivi un programma che gestisce un sistema di prenotazione di voli.
#Ogni volo ha una destinazione, una data e un numero di posti disponibili.
#Il programma deve permettere all'utente di aggiungere voli, visualizzare i voli disponibili,
#prenotare un volo, e visualizzare le prenotazioni correnti.

# Definizione di un tipo di dato per rappresentare un volo

Volo = dict[str, str | int]  # {'destinazione': ..., 'data': ..., 'posti_disponibili': ...}

def inserisci_dati_volo() -> Volo: # type: ignore
    
    """Chiede all'utente di inserire i dati di un volo.

    Returns:
        Volo: Un dizionario contenente i dati del volo"""
    
    pass

def aggiungi_volo(voli: list[Volo], volo: Volo) -> list[Volo]: # type: ignore
    
    """Aggiunge un volo alla lista dei voli disponibili.

    Args:
        voli (list[Volo]): La lista corrente dei voli.
        volo (Volo): Il nuovo volo da aggiungere.

    Returns:
        list[Volo]: La lista aggiornata dei voli"""
    
    pass

def visualizza_voli(voli: list[Volo]) -> None:
    
    """Visualizza tutti i voli disponibili.

    Args:
        voli (list[Volo]): La lista corrente dei voli"""
    
    pass

def prenota_volo(voli: list[Volo], volo: Volo) -> list[Volo]: # type: ignore
    
    """Prenota un posto su un volo specifico.

    Args:
        voli (list[Volo]): La lista corrente dei voli.
        volo (Volo): Il volo per cui si desidera prenotare un posto.

    Returns:
        list[Volo]: La lista aggiornata dei voli con la prenotazione effettuata"""
    
    pass

def visualizza_prenotazioni(prenotazioni: list[Volo]) -> None:
    
    """Visualizza le prenotazioni correnti.

    Args:
        prenotazioni (list[Volo]): La lista corrente delle prenotazioni"""
    
    pass

def main() -> None:
    
    """Funzione principale che gestisce il flusso del programma per la gestione delle prenotazioni di voli"""

    voli: list[Volo] = []

    nuovo_volo = inserisci_dati_volo()
    voli = aggiungi_volo(voli, nuovo_volo)

    visualizza_voli(voli)

    volo_da_prenotare = inserisci_dati_volo()
    voli = prenota_volo(voli, volo_da_prenotare)

    visualizza_prenotazioni(voli)

if __name__ == "__main__":
    main()