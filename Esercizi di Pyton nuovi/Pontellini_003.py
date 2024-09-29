#Esercizio 3: Attributi e Metodi di Classe
#Obiettivo
#Creare una classe chiamata Veicolo che utilizzi attributi e metodi di classe per tenere traccia del numero totale di veicoli creati. La classe deve avere un attributo di classe numero_veicoli e metodi di classe per accedere e modificare questo attributo.

#Istruzioni
#Definisci una classe chiamata Veicolo.
#Aggiungi un attributo di classe numero_veicoli inizializzato a 0.
#Nel metodo __init__, incrementa numero_veicoli ogni volta che viene creata una nuova istanza della classe.
#Implementa un metodo di classe get_numero_veicoli per restituire il valore dell'attributo di classe numero_veicoli.
#Esempio di Utilizzo
## Esempio di utilizzo
#print(Veicolo.get_numero_veicoli())  # Output: 0
#auto1 = Veicolo("Auto", "Toyota")
#auto2 = Veicolo("Moto", "Honda")
#print(Veicolo.get_numero_veicoli())  # Output: 2

class Vehicle:
    number_of_vehicles = 0

    def __init__(self, type_: str, brand: str):
        self.type_ = type_
        self.brand = brand
        Vehicle.number_of_vehicles += 1
    
    @classmethod
    def get_number_of_vehicles(cls):
        return cls.number_of_vehicles
        
print(Vehicle.get_number_of_vehicles())  # Output: 0
car1 = Vehicle("Car", "Toyota")
car2 = Vehicle("Motion", "Honda")
print(Vehicle.get_number_of_vehicles())  # Output: 2