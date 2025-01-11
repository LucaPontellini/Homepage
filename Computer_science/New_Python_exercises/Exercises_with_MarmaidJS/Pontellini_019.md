## Esercizio UML

### Obiettivo

Si desidera modellare un sistema di gestione di un canile.

### Istruzioni

1. Creare un diagramma UML delle classi utilizzando la sintassi di MermaidJS. Consegnare un file markdown con il diagramma UML in un blocco mermaid.

## Requisiti Funzionali Sistema Gestione Canile

### 1. Gestione Animali

- Registrazione nuovo animale (codice microchip, nome, età, razza, data ingresso)
- Gestione stato di salute (vaccinazioni, visite veterinarie)
- Gestione caratteristiche comportamentali
- Tracking posizione nel canile (box/area)
- Upload e gestione foto dell'animale

### 2. Gestione Adozioni

- Registrazione potenziali adottanti
- Processo di matching animale-adottante
- Gestione pratiche di adozione
- Monitoraggio post-adozione
- Storico adozioni

### 3. Gestione Struttura

- Mappatura box/aree disponibili
- Gestione capacità e occupazione
- Manutenzione strutture
- Inventario risorse (cibo, medicinali)

### 4. Gestione Personale

- Turni dipendenti/volontari
- Assegnazione mansioni
- Tracciamento attività svolte

### 5. Gestione Sanitaria

- Calendario vaccinazioni
- Registro visite veterinarie
- Gestione terapie in corso
- Gestione emergenze

### 6. Report e Statistiche

- Report mensili presenze animali
- Statistiche adozioni
- Monitoraggio costi/risorse
- Dashboard indicatori principali

### Requisiti Non Funzionali

- Interfaccia user-friendly
- Backup giornaliero dati
- Conformità GDPR
- Multi-utente con livelli di accesso
- Log delle operazioni
- Tempi di risposta < 2 secondi
- Disponibilità sistema 99.9%

```mermaid

classDiagram
    class Animal {
        +String: microchip_code
        +String: name
        +Int: age
        +String: breed
        +Date: entry_date
        +String: health_status
        +String: behavioral_characteristics
        +String: location
        +String: photo
    }

    class Adoption {
        +String: adoption_id
        +String: animal_id
        +String: adopter_id
        +Date: adoption_date
        +String: adoption_status
        +String: post_adoption_monitoring
    }

    class Person {
        +String: person_id
        +String: name
        +String: contact
        +String: address
        +String: animal_preferences
    }

    class Box {
        +String: box_id
        +String: location
        +Int: capacity
        +String: status
    }

    class Staff {
        +String: staff_id
        +String: name
        +String: role
        +String: shift
        +String: tasks
        +String: activities_performed
    }

    class Resource {
        +String: resource_id
        +String: type
        +Int: quantity
        +Date: expiration_date
    }

    class VeterinaryVisit {
        +String: visit_id
        +String: animal_id
        +Date: visit_date
        +String: outcome
        +String: therapies
    }

    Animal "1" --> "1..*" VeterinaryVisit : "has"
    Animal "0..1" --> "1" Adoption : "is adopted in"
    Adoption "1" --> "1" Person : "is adopted by"
    Animal "1" --> "1" Box : "is located in"
    Staff "1" --> "1..*" Box : "manages"
    Staff "1" --> "1..*" Animal : "takes care of"
    Resource "0..*" --> "1" Box : "is available in"
```