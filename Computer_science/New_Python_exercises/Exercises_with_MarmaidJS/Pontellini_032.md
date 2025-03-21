### Piattaforma di Streaming Video

Immagina una piattaforma dove gli utenti possono guardare video, creare playlist e seguire i loro canali preferiti.

Ogni utente ha un suo profilo con nome, email e password, e può creare diverse playlist per organizzare i video che preferisce.
L'utente ha anche un abbonamento che gli permette di accedere a contenuti esclusivi.

I video sono il cuore della piattaforma: hanno un titolo, una descrizione, un URL per lo streaming e una durata.
Sotto ogni video, gli utenti possono lasciare commenti.

Le playlist sono raccolte di video create dagli utenti.
Ogni playlist ha un nome e un creatore, e contiene una lista di video.

Ogni abbonamento ha un tipo, un prezzo e una data di inizio e fine.

I commenti sono messaggi lasciati dagli utenti sotto i video dopo averlo guardato.
Ogni commento ha un autore, un testo, una data di pubblicazione ed è associato a uno specifico video.

In sintesi, la piattaforma gestisce utenti, video, playlist, abbonamenti e commenti, permettendo agli utenti di interagire tra loro e con i contenuti.

```mermaid
classDiagram

    class Platform {
        +name: str
        +type: str
        +manages_profile(Profile: profile): Profile
        +manages_video(Video: video): Video
        +manages_playlist(Playlist: playlist): Playlist
        +manages_subscription(Subscription: subscription): Subscription
        +manages_comment(Comment: comment): Comment
    }

    class Profile {
        +name: str
        +email: str
        +password: str
        +subscription: float
        +create_different_playlists(Playlist: list[str]): list[str]
        +leave_comments(Video: video): str
    }

    class Video {
        +title: str
        +description: str
        +url: str
        +duration: datetime
    }

    class Playlist {
        +name: str
        +creator: str
        +create_the_playlist()
        +delete_the_playlist()
    }

    class Subscription {
        +type: str
        +price: float
        +start_date: datetime
        +end_date: datetime
    }

    class Comment {
        +author: str
        +text: str
        +date_of_publication: datetime
        +lease: str
    }

    Platform --> "1..*" Profile : can handle
    Platform --> "1..*" Video : can handle
    Platform --> "1..*" Subscription : can handle
    Platform --> "1..*" Comment : can handle
    Profile --> "1..*" Playlist : can create
    Profile --> "1..*" Subscription : can have
    Profile --> "1..*" Comment : can leave
    Comment --> "1..*" Video : are under
    Profile --> "1..*" Video : can watch
    Playlist --> "1..*" Video : may contain
```