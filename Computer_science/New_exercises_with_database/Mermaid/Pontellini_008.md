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
    NEGOZIO {
      int codice PK
      str indirizzo
      str citta
    }

    DIPENDENTE {
      str id_dipendente PK
      str nome
      str cognome
      str ruolo
      str codice_negozio FK
    }

    ARTISTA {
      str id_artista PK
      str nome
      str nazionalita
    }

    ALBUM_MUSICALE {
      str codice PK
      str titolo
      float prezzo_vendita
      str id_artista FK
    }

    VENDITA {
      str id_vendita PK
      date data
      str codice_negozio FK
      float importo_totale
    }

    RIGA_VENDITA {
      str id_riga_vendita PK
      str id_vendita FK
      str codice_album FK
      int quantita
      float prezzo_unitario
    }

    NEGOZIO ||--o{ DIPENDENTE : "impiega"
    ARTISTA ||--o{ ALBUM_MUSICALE : "produce"
    NEGOZIO ||--o{ VENDITA : "effettua"
    VENDITA ||--o{ RIGA_VENDITA : "contiene"
    ALBUM_MUSICALE ||--o{ RIGA_VENDITA : "è venduto in"
```