# Mappa Concettuale: Topologie delle Reti

## Introduzione
### Cos'è una Topologia di Rete?
La topologia di rete si riferisce alla disposizione fisica e logica dei nodi (dispositivi come computer, stampanti, server) e dei collegamenti (cavi, connessioni wireless) di una rete di computer. La scelta della topologia influisce sulla velocità, l'affidabilità, la scalabilità e il costo di una rete.

### Tipi di Topologie di Rete
Le topologie di rete si suddividono in due categorie principali:
- **Topologie Fisiche**: Rappresentano la disposizione fisica dei cavi e dei dispositivi nella rete.
- **Topologie Logiche**: Descrivono il flusso dei dati all'interno della rete, indipendentemente dalla disposizione fisica dei dispositivi.

## Topologie Fisiche

### 1. Topologia a Bus
- **Descrizione**: Tutti i nodi sono collegati a un singolo cavo centrale (bus). I dati trasmessi da un nodo possono essere ricevuti da tutti gli altri nodi sulla rete.
- **Vantaggi**:
  - Semplice da implementare.
  - Economica, richiede meno cavi.
  - Facile da estendere.
- **Svantaggi**:
  - Difficoltà di individuazione dei guasti.
  - Bassa scalabilità, difficoltà di gestione con l'aumento dei nodi.
  - Prestazioni degradano con l'aumento del traffico.
  - Se il cavo centrale si guasta, l'intera rete si arresta.
- **Utilizzo**: Questa topologia non è più utilizzata nelle reti moderne a causa dei suoi limiti.
- **Applicazioni Tipiche**: In passato, reti LAN piccole, reti di ufficio.
- **Caratteristiche**:
  - **Affidabilità**: Bassa
  - **Efficienza**: Moderata
  - **Flessibilità ed Espandibilità**: Bassa
  - **Costo**: Basso
- **Immagine**:
![Topologia a Bus](https://upload.wikimedia.org/wikipedia/commons/2/2b/NetworkTopology-Bus.svg)

### 2. Topologia ad Anello
- **Descrizione**: Ogni nodo è collegato al nodo successivo e l'ultimo nodo è collegato al primo, formando un anello chiuso. I dati viaggiano in una direzione (unidirezionale) o in entrambe le direzioni (bidirezionale).
- **Vantaggi**:
  - Prestazioni uniformi, nessuna collisione di dati.
  - Adatta per reti a lunga distanza.
- **Svantaggi**:
  - Il guasto di un singolo nodo o cavo interrompe l'intera rete.
  - Difficile da configurare e gestire.
- **Applicazioni Tipiche**: Reti MAN, reti WAN.
- **Caratteristiche**:
  - **Affidabilità**: Moderata
  - **Efficienza**: Alta
  - **Flessibilità ed Espandibilità**: Bassa
  - **Costo**: Moderato
- **Immagine**:
![Topologia ad Anello](https://upload.wikimedia.org/wikipedia/commons/a/a2/NetworkTopology-Ring.svg)

### 3. Topologia a Stella
- **Descrizione**: Tutti i nodi sono collegati a un nodo centrale (hub o switch), attraverso cui passano tutte le comunicazioni.
- **Vantaggi**:
  - Facile da gestire e individuare guasti.
  - Alta scalabilità, facile aggiungere nuovi nodi.
  - Il guasto di un singolo cavo non influisce sugli altri nodi.
- **Svantaggi**:
  - Il nodo centrale è un punto di vulnerabilità: se si guasta, l'intera rete si arresta.
  - Maggior utilizzo di cavi, aumento dei costi.
- **Applicazioni Tipiche**: Reti LAN di medie e grandi dimensioni.
- **Caratteristiche**:
  - **Affidabilità**: Moderata
  - **Efficienza**: Moderata
  - **Flessibilità ed Espandibilità**: Alta
  - **Costo**: Moderato
- **Immagine**:
![Topologia a Stella](https://upload.wikimedia.org/wikipedia/commons/7/79/Star_Topology.svg)

### 4. Topologia a Stella Estesa
- **Descrizione**: Una variazione della topologia a stella, in cui più nodi centrali (hub o switch) sono collegati tra loro per formare una rete di stelle.
- **Vantaggi**:
  - Maggiore tolleranza ai guasti rispetto a una semplice topologia a stella.
  - Scalabilità migliorata.
- **Svantaggi**:
  - Più complessa da configurare e gestire.
  - Maggiori costi di implementazione.
- **Applicazioni Tipiche**: Grandi reti aziendali.
- **Caratteristiche**:
  - **Affidabilità**: Alta
  - **Efficienza**: Moderata
  - **Flessibilità ed Espandibilità**: Alta
  - **Costo**: Alto
- **Immagine**:
![Topologia a Stella Estesa](https://upload.wikimedia.org/wikipedia/commons/5/55/Extended_star_topology.png)

### 5. Topologia a Maglia Completa
- **Descrizione**: Ogni nodo è collegato a tutti gli altri nodi nella rete, creando una rete di connessioni ridondanti.
- **Vantaggi**:
  - Alta affidabilità, fault tolerance: molteplici percorsi per i dati.
  - Elevata sicurezza: difficile intercettare i dati.
  - Prestazioni elevate: molteplici vie di comunicazione.
- **Svantaggi**:
  - Costosa da implementare a causa della grande quantità di cavi e porte di rete.
  - Complessa gestione e configurazione.
- **Applicazioni Tipiche**: Reti WAN, reti di data center.
- **Caratteristiche**:
  - **Affidabilità**: Molto alta
  - **Efficienza**: Alta
  - **Flessibilità ed Espandibilità**: Alta
  - **Costo**: Molto alto
- **Immagine**:
![Topologia a Maglia Completa](https://upload.wikimedia.org/wikipedia/commons/7/74/NetworkTopology-Mesh.svg)

### 6. Topologia a Maglia Incompleta
- **Descrizione**: Ogni nodo è collegato a uno o più nodi, ma non a tutti, creando una rete di connessioni parzialmente ridondanti.
- **Vantaggi**:
  - Alta affidabilità rispetto alle topologie non ridondanti.
  - Migliore utilizzo delle risorse rispetto a una maglia completa.
  - Maggior sicurezza rispetto alle topologie non ridondanti.
- **Svantaggi**:
  - Ancora costosa rispetto ad altre topologie come la stella o il bus.
  - Complessa gestione e configurazione, anche se meno della maglia completa.
- **Applicazioni Tipiche**: Reti WAN, reti aziendali che richiedono alta affidabilità ma con budget limitato rispetto alla maglia completa.
- **Caratteristiche**:
  - **Affidabilità**: Alta
  - **Efficienza**: Moderata
  - **Flessibilità ed Espandibilità**: Moderata
  - **Costo**: Alto
- **Immagine**:
![Topologia a Maglia Incompleta](https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/NetworkTopology-Mesh.svg/300px-NetworkTopology-Mesh.svg.png)

## Topologie Logiche

### 1. Topologia a Broadcast
- **Descrizione**: In questa topologia, tutti i nodi ricevono i dati inviati da qualsiasi altro nodo. Non c'è un percorso prefissato per il flusso dei dati, ma i pacchetti sono diffusi a tutti i nodi sulla rete.
- **Vantaggi**:
  - Semplice da implementare.
  - Adatta per la trasmissione di informazioni a più destinazioni contemporaneamente.
- **Svantaggi**:
  - Maggiore congestione di rete dovuta alla trasmissione broadcast.
  - Possibilità di collisioni di pacchetti.
- **Applicazioni Tipiche**: Reti LAN con necessità di trasmettere dati a tutti i nodi, come trasmissioni in tempo reale.
- **Caratteristiche**:
  - **Affidabilità**: Moderata
  - **Efficienza**: Moderata
  - **Flessibilità ed Espandibilità**: Bassa
  - **Costo**: Basso

### 2. Topologia a Token Passing
- **Descrizione**: In questa topologia, un "token" viene passato da nodo a nodo nella rete. Solo il nodo che detiene il token ha il permesso di trasmettere dati. Questo metodo regola l'accesso alla rete e previene le collisioni di dati.
- **Vantaggi**:
  - Controllo dell'accesso alla rete, evita collisioni.
  - Prestazioni più efficienti rispetto a topologie condivise come il bus.
- **Svantaggi**:
  - Maggiore complessità nell'implementazione rispetto al broadcast.
  - Se il token si guasta, l'intera rete può subire rallentamenti.
- **Applicazioni Tipiche**: Reti LAN con necessità di gestione del traffico e prevenzione delle collisioni.
- **Caratteristiche**:
  - **Affidabilità**: Moderata
  - **Efficienza**: Alta
  - **Flessibilità ed Espandibilità**: Moderata
  - **Costo**: Moderato

## Considerazioni sulla Scelta della Topologia
La scelta della topologia di rete dipende da diversi fattori:
- **Dimensione della Rete**: Piccole reti possono utilizzare una topologia a bus o stella, mentre le grandi reti possono necessitare di una topologia a stella estesa o a maglia.
- **Budget**: Le topologie più semplici come il bus e la stella sono generalmente più economiche.
- **Affidabilità**: La topologia a maglia offre alta affidabilità, ma a un costo maggiore.
- **Facilità di Manutenzione**: Le topologie come la stella sono più facili da mantenere e gestire.

## Conclusione
Comprendere i pro e i contro di ciascuna topologia di rete è essenziale per progettare reti efficienti e affidabili. La scelta appropriata dipenderà dalle
esigenze specifiche dell'organizzazione, inclusi costi, scalabilità, gestione e tolleranza ai guasti.