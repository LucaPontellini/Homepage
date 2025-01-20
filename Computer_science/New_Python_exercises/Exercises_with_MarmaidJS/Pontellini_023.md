
Descrizione dell'esercizio:
Un social network di fotografia (instagram).
Gli utenti possono registrarsi, creare un profilo, caricare foto, seguire altri utenti.
Ogni foto ha un titolo, una descrizione. Gli utenti possono creare album per organizzare le loro foto.

Classi Principali:

Utente: nome utente, email, password, profilo (immagine, biografia)
Foto: ID, titolo, descrizione, data caricamento, utente (chi l'ha caricata), album (a quale album appartiene)
Album: titolo, descrizione, utente (chi l'ha creato), foto (lista di foto)

Relazioni:

Un utente può caricare molte foto (relazione uno-a-molti).
Una foto può avere molti commenti (relazione uno-a-molti).
Un commento appartiene a un utente e a una foto (relazione molti-a-molti).
Una foto appartiene a un album (relazione uno-a-molti).
Un album appartiene a un utente (relazione uno-a-molti).

Crea relativo diagramma UML e codice.

```mermaid

    class User {
        +username: str
        +email: str
        +password: str
        +profile: str
    }

    class Photo {
        +ID: str
        +title: str
        +description: str
        +upload_date: date
        +user: str
        +album: str
    }

    class Album {
        +title: str
        +description: str
        +user: str
        +photo: str
    }

    class Album {
        +title: str
        +description: str
        +user: str
        +photo: list<photo>
    }

    class Comments {
    +author: User
    +lease: Photo
    }

    User "1..*" --> "0..*" Photo : "can upload"
    Photo "1..*" --> "0..*" Comments : "can have"
    Comments "0..*" --> "0..*" User : "belongs to"
    Comments "0..*" --> "0..*" Photo : "belongs to"
    Photo "1..*" --> "1..*" Album : "belongs to "
    Album "1..*" --> "1..*" User : "belongs to"
>>>>>>> abf90e8 (edit)
```