#Esercizio: Associazioni 1-1 tra Classi in Python

#Prerequisiti
#Conoscenza delle classi in Python.
#Comprensione delle associazioni tra classi, in particolare le associazioni uno a uno.
#Familiarità con i metodi getter e setter.

#Obiettivo
#Creare due classi in Python che rappresentano un'associazione uno a uno.
#Utilizzare l'associazione per collegare istanze delle due classi in modo che ogni istanza di una classe sia associata a una sola istanza dell'altra classe.

#Istruzioni
#Definisci una classe chiamata Auto con gli attributi di istanza marca e modello.
#Definisci una classe chiamata Motore con gli attributi di istanza numero_seriale e tipo.
#Implementa metodi di istanza in entrambe le classi per accedere e modificare i loro attributi.
#Aggiungi un attributo di istanza in ciascuna classe per mantenere il riferimento all'istanza associata dell'altra classe.
#Implementa un metodo in entrambe le classi per collegare le istanze tra loro, assicurando che l'associazione sia uno a uno.
#Crea istanze di entrambe le classi e associa ciascuna Auto a un unico Motore.
#Verifica che ogni Auto sia correttamente associata al proprio Motore e viceversa.
#Esempio di Utilizzo
# Creazione delle istanze
#car1 = Auto("Fiat", "500")
#engine1 = Motore("ENG123456", "Benzina")

# Associazione tra auto e motore
#car1.associa_motore(engine1)

# Verifica dell'associazione
#print(f"{car1.marca} {car1.modello} ha il motore: {car1.motore.numero_seriale}")
#print(f"Il motore {engine1.numero_seriale} appartiene a: {engine1.auto.marca} {engine1.auto.modello}")

#Output atteso
#Fiat 500 ha il motore: ENG123456
#Il motore ENG123456 appartiene a: Fiat 500

class Car:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if brand:
            self._brand = brand
        else:
            self._brand = "Unknown brand"
    
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if model:
            self._model = model
        else:
            self._model = "Unknown model"
    
    def associate_engine(self, engine) -> None:
        self.engine = engine.vehicle = self

class Engine:
    def __init__(self, serial_number: str, type: str):
        self.serial_number = serial_number
        self.type = type

    @property
    def serial_number(self):
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        if serial_number:
            self._serial_number = serial_number
        else:
            self._serial_number = "Unknown serial number"
    
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        if type:
            self._type = type
        else:
            self._type = "Unknown type"
    
    def associate_vehicle(self, vehicle) -> None:
        self.vehicle = vehicle.engine = self

car1 = Car("Fiat", "500")
engine1 = Engine("ENG123456", "Benzina")

car1.associate_engine(engine1)

print(f"{car1.brand} {car1.model} has the engine: {car1.engine.serial_number}")
print(f"Il motore {engine1.serial_number} belongs to: {engine1.car.brand} {engine1.car.model}")

#Fiat 500 ha il motore: ENG123456
#Il motore ENG123456 appartiene a: Fiat 500