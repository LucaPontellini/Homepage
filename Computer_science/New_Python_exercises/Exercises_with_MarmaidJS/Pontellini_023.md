
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

classDiagram
    class User {
        +username: str
        +email: str
        +password: str
        +profile: str
        +register()
        +create_profile()
        +upload_photo()
        +follow_user()
        +create_album()
    }

    class Photo {
        +ID: str
        +title: str
        +description: str
        +upload_date: date
        +user: User
        +album: Album
    }

    class Album {
        +title: str
        +description: str
        +user: User
        +photos: List~Photo~
    }

    class Comment {
        +author: User
        +photo: Photo
        +content: str
        +date: date
    }

    User "1" --> "0..*" Photo : "uploads"
    Photo "1" --> "0..*" Comment : "has"
    Comment "1" --> "1" User : "is written by"
    Comment "1" --> "1" Photo : "is about"
    Photo "1" --> "1" Album : "belongs to"
    Album "1" --> "0..*" Photo : "contains"
    Album "1" --> "1" User : "is created by"
```