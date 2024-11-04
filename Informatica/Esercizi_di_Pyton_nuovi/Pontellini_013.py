#Esercizio: Associazioni 1-N tra Classi in Python

#Prerequisiti
#Conoscenza delle classi in Python.
#Comprensione delle associazioni tra classi, in particolare le associazioni uno a molti.
#Familiarità con i metodi getter e setter.

#Obiettivo
#Creare due classi in Python che rappresentano un'associazione uno a molti.
#Utilizzare l'associazione per collegare un'istanza di una classe (uno) a più istanze dell'altra classe (molti).

#Istruzioni
#Definisci una classe chiamata house con gli attributi di istanza indirizzo e proprietario.
#Definisci una classe chiamata Stanza con gli attributi di istanza nome e superficie.
#Implementa metodi di istanza in entrambe le classi per accedere e modificare i loro attributi.
#Aggiungi un attributo di istanza nella classe house per mantenere una lista di istanze di Stanza associate.
#Implementa un metodo nella classe house per aggiungere una Stanza alla sua collezione.
#Crea un'istanza di house e aggiungi diverse istanze di Stanza alla sua collezione.
#Verifica che la house contenga correttamente tutte le Stanza aggiunte.
#Esempio di Utilizzo
# Creazione dell'istanza di house
#house = house("Via delle Rose 15", "Maria Rossi")

# Creazione delle istanze di Stanza
#soggiorno = Stanza("Soggiorno", 30)
#Kitchen = Stanza("Kitchen", 15)
#Bedroom = Stanza("Bedroom da Letto", 20)

# Aggiunta delle stanze alla house
#house.aggiungi_stanza(soggiorno)
#house.aggiungi_stanza(Kitchen)
#house.aggiungi_stanza(Bedroom)

# Verifica dell'associazione
#print(f"house di {house.proprietario} situata in {house.indirizzo} contiene le seguenti stanze:")
#for stanza in house.stanze:
#    print(f"- {stanza.nome} ({stanza.superficie} mq)")

#Output atteso
#house di Maria Rossi situata in Via delle Rose 15 contiene le seguenti stanze:
#- Soggiorno (30 mq)
#- Kitchen (15 mq)
#- Bedroom da Letto (20 mq)

class House:
    def __init__(self, address: str, owner: str):
        self.address = address
        self.owner = owner
        self.rooms = []
    
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if address:
            self._address = address
        else:
            self._address = "Unknown address"
    
    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if owner:
            self._owner = owner
        else:
            self._owner = "Unknown owner"

    def add_room(self, room) -> None:
        self.rooms.append(room)

    def get_rooms(self) -> list:
        return self.rooms

class Room:
    def __init__(self, name: str, surface: int):
        self.name = name
        self.surface = surface

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name:
            self._name = name
        else:
            self._name = "Unknown name"
    
    @property
    def surface(self):
        return self._surface

    @surface.setter
    def surface(self, surface):
        if surface > 0: 
            self._surface = surface 
        else: self._surface = 0

house = House("Via delle Rose 15", "Maria Rossi")

living_room = Room("Living room", 30)
kitchen = Room("Kitchen", 15)
bedroom = Room("Bedroom", 20)

house.add_room(living_room)
house.add_room(kitchen)
house.add_room(bedroom)

print(f"House of {house.owner} located in {house.address} contains the following rooms:")
for room in house.get_rooms():
    print(f"- {room.name} ({room.surface} mq)")

#Casa di Maria Rossi situata in Via delle Rose 15 contiene le seguenti stanze:
#- Soggiorno (30 mq)
#- Cucina (15 mq)
#- Camera da Letto (20 mq)