#Esercizio 9: Utilizzo di Getter e Setter

#Crea una classe che rappresenta un libro in una biblioteca.
#La classe deve avere i seguenti attributi privati:Libro

#_titolo: il titolo del libro
#_autore: l'autore del libro
#_pagine: il numero di pagine del libro
#Implementa i metodi getter e setter per ciascuno di questi attributi, assicurandoti che:

#il titolo e l'autore non possano essere stringhe vuote.
#il numero di pagine deve essere un numero positivo.

#Esempio di utilizzo della classe:

#libro = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 1200)
#print(libro.titolo)  # Chiama automaticamente il getter
#libro.titolo = "Lo Hobbit"  # Chiama automaticamente il setter
#print(libro.titolo)
#Prova a creare un'istanza della classe Libro e a utilizzare i metodi getter e setter per modificare e accedere agli attributi.

class Book:
    def __init__(self, title: str, author: str, pages: int):
        
        if title:
            self._title = title
        else:
            self._title = "Unknown Title"
        if author:
            self._author = author
        else:
            self._author = "Unknown Author"
        if pages > 0:
            self._pages = pages
        else:
            self._pages = 1
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if title:
            self._title = title
        else:
            self._title = "Unknown Title"

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if author:
            self._author = author
        else:
            self._author = "Unknown Author"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages):
        if pages > 0:
            self._pages = pages
        else:
            self._pages = 1

book = Book("", "", -5)
print(book.title)  # Output: Unknown Title
print(book.author)  # Output: Unknown Author
print(book.pages)  # Output: 1

book.title = "The Hobbit"
book.author = "J.R.R. Tolkien"
book.pages = 310

print(book.title)  # Output: The Hobbit
print(book.author)  # Output: J.R.R. Tolkien
print(book.pages)  # Output: 310