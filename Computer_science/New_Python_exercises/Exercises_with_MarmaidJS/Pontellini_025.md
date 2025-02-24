Gestire le prenotazioni in un ristorante.

Ogni prenotazione ha un nome del cliente, una data e ora, un numero di persone e uno stato (confermata, in attesa, cancellata).
Il sistema deve permettere di:

- aggiungere nuove prenotazioni
- cercare prenotazioni per nome del cliente o data
- visualizzare tutte le prenotazioni
- cancellare una prenotazione

Il sistema deve includere due classi principali:
- rappresenta una singola prenotazione nel ristorante
- gestisce le prenotazioni e le operazioni associate

```mermaid

classDiagram
    class Reservation {
        +customer_name: str
        +date: date
        +number_of_people: int
        +status: str
    }

    class ReservationManager {
        +list[Reservation]: reservations
        +add_reservation(self, customer_name: str, date: date, number_of_people: int, status: str)
        +search_reservation_by_name(self, customer_name: str): list[Reservation]
        +search_reservation_by_date(self, date: date): list[Reservation]
        +view_all_reservations(self): list[Reservation]
        +cancel_reservation(self, customer_name: str, date: date)
    }

    ReservationManager "1" --> "0..*" Reservation : "contains"
```