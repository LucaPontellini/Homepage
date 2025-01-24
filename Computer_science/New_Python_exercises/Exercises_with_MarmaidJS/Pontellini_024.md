Gestione di una libreria di film.

Ogni film ha un titolo, un regista, un anno di uscita, un genere (azione, commedia, drammatico, horror, documentario) e una valutazione (da 1 a 10).

Il sistema deve permettere di:
- aggiungere nuovi film alla libreria
- cercare film per titolo o regista
- visualizzare tutti i film presenti nella libreria
- calcolare la valutazione media dei film

Il sistema deve includere due classi principali:
- rappresenta un singolo film nella libreria
- gestisce i film e le operazioni associate

Creare il Mermaid e il codice

```mermaid

classDiagram
    class Film {
        +title: str
        +director: str
        +year_of_release: date
        +genre: str
        +rating: float
        +__init__()
        +__str__()
    }

    class MovieLibrary {
        +__init__()
        +add_new_movies()
        +search_films_by_title()
        +view_all_movies()
        +calculate_average()
    }

Film "0..*" --> "1..*" MovieLibrary : "can be in"