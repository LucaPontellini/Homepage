```mermaid

classDiagram

    class Author {
        +String: name
        +String: surname
        +List<Book>: books
        +String: biography
    }
    class Biography {
        +String: text
        +String: publicationDate
    }
    class Library {
        +String: name
        +String: address
    }
    class Book {
        +String: title
        +Author: author
    }
    class Student {
        +String: name
        +String: surname
    }
    class Device {
        +String: brand
        +String: model
    }
    class Smartphone {
        +boolean: supports5G
    }
    class Tablet {
        +boolean: hasPen
    }

    Author "1" --> "1" Biography
    Author "1" --> "n" Book
    Book "1" --> "1" Author
    Library "1" --> "n" Book
    Library "1" --> "n" Student
    Student "1" --> "n" Book
    Student "1" --> "1" Device
    Device <|-- Smartphone
    Device <|-- Tablet