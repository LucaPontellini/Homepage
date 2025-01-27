Il programma ci permette di gestire una flotta aziendale di veicoli.
Ogni veicolo ha una marca, un modello e un tipo di carburante.
Esistono due tipologie di veicoli: *auto* e *camion*. Ogni veicolo può essere aggiunto alla flotta, e il programma deve consentire di visualizzare le informazioni sui veicoli.

Requisiti:
1. Creare una classe `Veicolo` con gli attributi di base: `marca`, `modello` e `carburante`.
2. Creare due sottoclassi: `Auto` e `Camion`. Ogni sottoclasse deve semplicemente ereditare gli attributi da `Veicolo`.
3. La classe `Flotta` deve gestire una lista di veicoli, permettere l’aggiunta di nuovi veicoli, e la visualizzazione delle informazioni di tutti i veicoli.

Crea relativo diagramma UML  e codice.

```mermaid

classDiagram
    class Vehicle {
        +brand: str
        +model: str
        +fuel: str
    }

    class Car {
        
    }

    class Truck {
        
    }

    class Fleet {
        +list[Vehicle]: vehicles
        +add_new_vehicles(Vehicle): none
        +view_vehicle_information(brand: str, model: str, fuel: str): str
    }

    Car --|> Vehicle
    Truck --|> Vehicle
    
    Vehicle "1..*" --> "0..*" Fleet : "can be in "
    Car "0..*" --> "0..*" Fleet : "can be in "
    Truck "0..*" --> "0..*" Fleet : "can be in"
```