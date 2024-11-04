#Esercizio 1: Creazione della Classe Persona

#Obiettivo
#Creare una classe chiamata Persona che rappresenti una persona.
#La classe deve avere tre attributi di istanza (nome, eta, citta) e due metodi di istanza (saluta, descrizione).

#Istruzioni
#Definisci una classe chiamata Persona.
#Aggiungi tre attributi di istanza nel metodo __init__: nome, eta, citta.
#Implementa un metodo di istanza saluta che restituisce una stringa di saluto contenente il nome della persona.
#Implementa un metodo di istanza descrizione che restituisce una stringa descrittiva contenente l'età e la citta della persona.

# Esempio di utilizzo
#persona = Persona("Mario", 30, "Roma")
#print(persona.saluta())  # Output: Ciao, mi chiamo Mario.
#print(persona.descrizione())  # Output: Ho 30 anni e vivo a Roma.

class Person:
    
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city
    
    def greets(self):
        print(f"Hello, my name is {self.name}.")
        return f"Hello, my name is {self.name}."

    def description(self):
        print(f"I'm {self.age} and i live in {self.city}.")
        return f"I'm {self.age} and i live in {self.city}."

person = Person("Mario", 30, "Rome")

person.greets()
person.description()