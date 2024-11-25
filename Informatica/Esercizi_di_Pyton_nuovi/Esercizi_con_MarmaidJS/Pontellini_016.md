```mermaid

classDiagram

    class 


    Author "1" --> "1" Biography
    Author "1" --> "n" Book
    Book "1" --> "1" Author
    Library "1" --> "n" Book
    Library "1" --> "n" Student
    Student "1" --> "n" Book
    Student "1" --> "1" Device
    Device <|-- Smartphone
    Device <|-- Tablet