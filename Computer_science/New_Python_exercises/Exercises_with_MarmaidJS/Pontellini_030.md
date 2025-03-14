L'obiettivo di questo esercizio è sviluppare un sistema di gestione delle risorse di un laboratorio scolastico, dove gli studenti possono prenotare e annullare la prenotazione di risorse come computer, proiettori e altre attrezzature.
Il sistema dovrà essere in grado di gestire le disponibilità delle risorse, permettere agli studenti di effettuare prenotazioni e annullamenti, e visualizzare lo stato delle risorse in tempo reale.
In un laboratorio scolastico ci sono diverse risorse che gli studenti possono prenotare, come computer, proiettori e altre attrezzature.
Ogni risorsa può essere prenotata da uno studente, ma una volta prenotata non può essere prenotata da un altro studente fino a quando non viene annullata la prenotazione.  

Realizza il relativo diagramma UML

```mermaid
classDiagram
    class Student {
        +name: str
        +surname: str
        +class: str
        +year: int
        +reserved_resources: list[Resource]
        +canceled_resources: list[Resource]
        +reserve(resource: Resource): bool
        +cancel(resource: Resource): bool
    }

    class SchoolWorkshop {
        +name: str
        +lease: str
        +capacity: float
        +number_of_resources: list[Resource]
    }

    class Resource {
        +typology: str
        +quantity: int
        +availability: bool
        +manage_availability(resource: Resource): bool
        +view_status(resource: Resource): bool
    }

Resource "1..*" --> "1" Student : can be booked by
Resource "1..*" --> "1..*" SchoolWorkshop : is contained in the
Student "1..*" --> "1..*" SchoolWorkshop : can go to the
```