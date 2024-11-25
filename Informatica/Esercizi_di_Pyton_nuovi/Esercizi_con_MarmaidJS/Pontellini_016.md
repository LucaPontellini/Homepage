```mermaid

classDiagram

    class Doctor {
        +String: name
        +String: surname
        +String: specialization
    }
    class Drugs {
        +String: name
        +Float: dose
    }
    class Hospital {
        +String: name
        +String: address
        +List <department>: departments
    }