#Esercizio 7: Sistema di Gestione di Biblioteca

#Obiettivo
#Creare una gerarchia di classi che rappresenti diversi tipi di materiali in una biblioteca.
#Utilizzare l'ereditarietà per definire una classe base MaterialeBiblioteca e classi derivate Libro, Rivista e DVD che ereditano dalla classe base.
#Implementare metodi specifici per ogni tipo di materiale e aggiungere funzionalità avanzate come la gestione dei prestiti e la ricerca di materiali.

#Istruzioni
#Definisci una classe base chiamata MaterialeBiblioteca con attributi di istanza titolo, anno_pubblicazione e disponibile.
#Implementa metodi di istanza nella classe MaterialeBiblioteca per accedere e modificare questi attributi.
#Aggiungi un metodo prestito che imposta l'attributo disponibile a False e un metodo restituzione che lo imposta a True.
#Definisci una classe derivata chiamata Libro che eredita dalla classe MaterialeBiblioteca.
#Aggiungi attributi di istanza specifici per Libro, come autore e numero_pagine.
#Definisci una classe derivata chiamata Rivista che eredita dalla classe MaterialeBiblioteca.
#Aggiungi attributi di istanza specifici per Rivista, come numero_edizione e mese_pubblicazione.
#Definisci una classe derivata chiamata DVD che eredita dalla classe MaterialeBiblioteca.
#Aggiungi attributi di istanza specifici per DVD, come regista e durata.
#Implementa metodi di istanza nelle classi Libro, Rivista e DVD per accedere e modificare i loro attributi specifici.
#Aggiungi un metodo di ricerca nella classe MaterialeBiblioteca che permette di cercare materiali per titolo o anno di pubblicazione.

# Esempio di utilizzo
#libro = Libro("Il Signore degli Anelli", 1954, "J.R.R. Tolkien", 1178)
#print(libro.get_titolo())  # Output: Il Signore degli Anelli
#print(libro.get_autore())  # Output: J.R.R. Tolkien
#libro.prestito()
#print(libro.is_disponibile())  # Output: False
#libro.restituzione()
#print(libro.is_disponibile())  # Output: True

#rivista = Rivista("National Geographic", 2023, 5, "Maggio")
#print(rivista.get_titolo())  # Output: National Geographic
#print(rivista.get_numero_edizione())  # Output: 5

#dvd = DVD("Inception", 2010, "Christopher Nolan", 148)
#print(dvd.get_titolo())  # Output: Inception
#print(dvd.get_regista())  # Output: Christopher Nolan

#materiali = [libro, rivista, dvd]
#risultati = MaterialeBiblioteca.ricerca(materiali, titolo="Inception")
#for materiale in risultati:
#    print(materiale.get_titolo())  # Output: Inception

class Library_Material:

    def __init__(self, title: str, year_of_publication: int, available: bool = True):
        self.title = title
        self.year_of_publication = year_of_publication
        self.available = available

    def get_title(self):
        return self.title
    
    def set_title(self, title: str):
        self.title = title
    
    def get_year_of_publication(self):
        return self.year_of_publication
    
    def set_year_of_publication(self, year_of_publication: int):
        self.year_of_publication = year_of_publication
    
    def is_available(self):
        return self.available
    
    def set_available(self, available: bool):
        self.available = available
    
    def borrow(self):
        self.available = False
    
    def return_material(self):
        self.available = True

    @staticmethod
    def search(materials, title=None, year_of_publication=None):
        results = []
        for material in materials:
            if title and material.get_title() == title:
                results.append(material)
            elif year_of_publication and material.get_year_of_publication() == year_of_publication:
                results.append(material)
        return results

class Book(Library_Material):

    def __init__(self, title, year_of_publication, author, number_of_pages, available=True):
        super().__init__(title, year_of_publication, available)
        self.author = author
        self.number_of_pages = number_of_pages

    def get_author(self):
        return self.author

    def set_author(self, author):
        self.author = author

    def get_page_count(self):
        return self.number_of_pages

    def set_page_count(self, number_of_pages):
        self.number_of_pages = number_of_pages

class Magazine(Library_Material):

    def __init__(self, title, year_of_publication, edition_number, month_of_publication, available=True):
        super().__init__(title, year_of_publication, available)
        self.edition_number = edition_number
        self.month_of_publication = month_of_publication

    def get_issue_number(self):
        return self.edition_number

    def set_issue_number(self, edition_number):
        self.edition_number = edition_number

    def get_month_of_publication(self):
        return self.month_of_publication

    def set_month_of_publication(self, month_of_publication):
        self.month_of_publication = month_of_publication

class DVD(Library_Material):

    def __init__(self, title, year_of_publication, director, duration, available=True):
        super().__init__(title, year_of_publication, available)
        self.director = director
        self.duration = duration

    def get_director(self):
        return self.director

    def set_director(self, director):
        self.director = director

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

book = Book("The Lord of the Rings", 1954, "J.R.R. Tolkien", 1178)
print(book.get_title())  # Output: The Lord of the Rings
print(book.get_author())  # Output: J.R.R. Tolkien
book.borrow()  # Corretto qui
print(book.is_available())  # Output: False
book.return_material()
print(book.is_available())  # Output: True

magazine = Magazine("National Geographic", 2023, 5, "May")
print(magazine.get_title())  # Output: National Geographic
print(magazine.get_issue_number())  # Output: 5

dvd = DVD("Inception", 2010, "Christopher Nolan", 148)
print(dvd.get_title())  # Output: Inception
print(dvd.get_director())  # Output: Christopher Nolan

materials = [book, magazine, dvd]
results = Library_Material.search(materials, title="Inception")
for material in results:
    print(material.get_title())  # Output: Inception