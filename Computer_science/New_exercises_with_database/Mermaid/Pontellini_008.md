# Esercizio 8 — Negozio di Musica (testo)

Introduzione
------------
La catena di negozi di musica "Melodia" vende dischi, CD e vinili di artisti italiani e internazionali. L'azienda è organizzata con una sede centrale e molteplici negozi distribuiti in varie città. Ogni negozio gestisce l'inventario e le vendite al dettaglio.

Organizzazione e processi
------------------------
Ogni negozio è identificato da un codice numerico e dispone di un indirizzo e della città in cui si trova. Nei negozi lavorano più dipendenti: ogni dipendente è impiegato in un negozio specifico. Gli artisti producono album musicali, che sono identificati da un codice e hanno un titolo e un prezzo di vendita.

Le vendite vengono registrate giornalmente: per ogni vendita si conserva la data, il negozio che ha effettuato la vendita e l'importo totale. Per dettagliare i contenuti di una vendita si usano le righe di vendita che indicano, per ogni album venduto, la quantità e il prezzo unitario applicato.

Obiettivo del modello
--------------------
Progettare un modello ER che rappresenti la struttura sopra descritta e che permetta di rispondere a domande come:
- Quali album ha prodotto un determinato artista?
- Qual è il totale delle vendite di un negozio in un dato intervallo di date?
- Quali album sono stati venduti in una vendita specifica e in che quantità?

```mermaid
erDiagram

    RigheScontrino {
        INTEGER id PK
        INTEGER scontrino_id FK
        INTEGER album_id FK
        INTEGER quantita
    }

    Negozi {
        INTEGER codice PK
        TEXT indirizzo
        TEXT citta
    }

    Dipendenti {
        INTEGER id PK
        TEXT nome
        TEXT cognome
        INTEGER negozio_id FK
    }

    Artisti {
        INTEGER id PK
        TEXT nome
        TEXT cognome
    }

    AlbumVirtuale {
        INTEGER codice PK
        TEXT titolo
        REAL prezzo
        REAL prezzo_unitario
        INTEGER artista_id FK
    }

    Scontrino {
        INTEGER id PK
        DATE data
        INTEGER negozio_id FK
        REAL importo_totale
    }

    Negozi ||--o{ Dipendenti : "lavora"
    Negozi ||--o{ Scontrino : "effettua"
    Artisti ||--o{ AlbumVirtuale : "produce"
    Scontrino ||--o{ RigheScontrino : "dettaglia"
    RigheScontrino }o--|| AlbumVirtuale : "riguarda"
```