#Esercizio 5: Ereditarietà

#Obiettivo
#Creare una gerarchia di classi che rappresenti diversi tipi di dipendenti in un'azienda.
#Utilizzare l'ereditarietà per definire una classe base Dipendente e classi derivate Manager e Sviluppatore che ereditano dalla classe base.

#Istruzioni
#Definisci una classe base chiamata Dipendente con attributi di istanza nome e stipendio.
#Implementa metodi di istanza nella classe Dipendente per accedere e modificare questi attributi.
#Definisci una classe derivata chiamata Manager che eredita dalla classe Dipendente.
#Aggiungi un attributo di istanza specifico per Manager, come numero_di_team.
#Definisci una classe derivata chiamata Sviluppatore che eredita dalla classe Dipendente.
#Aggiungi un attributo di istanza specifico per Sviluppatore, come linguaggio_di_programmazione.
#Implementa metodi di istanza nelle classi Manager e Sviluppatore per accedere e modificare i loro attributi specifici.

# Esempio di utilizzo
#manager = Manager("Alice", 50000, 3)
#print(manager.get_nome())  # Output: Alice
#print(manager.get_stipendio())  # Output: 50000
#print(manager.get_numero_di_team())  # Output: 3

#sviluppatore = Sviluppatore("Bob", 40000, "Python")
#print(sviluppatore.get_nome())  # Output: Bob
#print(sviluppatore.get_stipendio())  # Output: 40000
#print(sviluppatore.get_linguaggio_di_programmazione())  # Output: Python

class Employee:

    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary
    
    def get_name(self):
        return self.name
    
    def set_name(self, name: str):
        self.name = name
    
    def get_salary(self):
        return self.salary
    
    def set_salary(self, salary: int):
        self.salary = salary

class Manager(Employee):

    def __init__(self, name: str, salary: int, number_of_teams: int):
        super().__init__(name, salary)
        self.number_of_teams = number_of_teams
    
    def get_number_of_teams(self):
        return self.number_of_teams
    
    def set_number_of_teams(self, number_of_teams: int):
        self.number_of_teams = number_of_teams

class Developer(Employee):

    def __init__(self, name: str, salary: int, programming_language: str):
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def get_programming_language(self):
        return self.programming_language
    
    def set_programming_language(self, programming_language: str):
        self.programming_language = programming_language

manager = Manager("Alice", 50000, 3)
print(manager.get_name())  # Output: Alice
print(manager.get_salary())  # Output: 50000
print(manager.get_number_of_teams())  # Output: 3

developer = Developer("Bob", 40000, "Python")
print(developer.get_name())  # Output: Bob
print(developer.get_salary())  # Output: 40000
print(developer.get_programming_language())  # Output: Python