# Mappa Concettuale: Gestione del Processore

## Programma
- **Definizione**: Insieme delle istruzioni memorizzate su memoria di massa.
- **Caratteristiche**:
  - Entità statica

## Processo
- **Definizione**: Istanza di un programma in evoluzione eseguito dal processore.
- **Caratteristiche**:
  - Deve essere residente in memoria RAM.
  - Entità logica in evoluzione
  - Entità dinamica

## Sinonimi
- **Task**
  - Sinonimo di processo
- **Job**
  - Sinonimo di processo
  - Utilizzato in contesti diversi:
    - **Sistemi Batch**: si parla di job.
    - **Sistemi di Time Sharing**: si parla di processo o task.

### Struttura di un Processo
- **Codice**:
  - Insieme di istruzioni eseguibili.
- **Dati del Programma**:
  - Contenuti del programma, suddivisi in:
    - **Variabili Globali**: Accessibili da tutto il programma.
    - **Variabili Locali**: Accessibili solo all'interno di una specifica funzione o blocco di codice.
    - **Variabili Non Locali**: Accessibili da funzioni annidate.
    - **Variabili Temporanee Introdotte dal Compilatore**: Incluse tra cui il program counter.
    - **Variabili Allocate Dinamicamente**: Spazio di memoria allocato durante l'esecuzione del programma.
- **Contesto del Processo**:
  - Insieme di tutti i dati di un processo, compresi codice e dati del programma.

### Processi Indipendenti, Cooperativi e Competitivi

#### Processi Indipendenti
- **Definizione**:
  - Processi che operano in modo isolato, senza dipendenze o interazioni significative con altri processi.
- **Caratteristiche**:
  - Eseguono il proprio compito senza influenze esterne.
  - Non richiedono coordinazione con altri processi.
  - Le attività possono essere eseguite in parallelo senza richiedere sincronizzazione.

#### Processi Cooperativi
- **Definizione**:
  - Processi che collaborano e comunicano tra loro per raggiungere un obiettivo comune.
- **Caratteristiche**:
  - Condividono risorse e informazioni per completare un compito.
  - Richiedono coordinazione e comunicazione per garantire che le attività siano eseguite correttamente.
  - Possono avere dipendenze tra loro, in cui l'avanzamento di un processo dipende dall'esito o dallo stato di un altro processo.

#### Processi Competitivi
- **Definizione**:
  - Processi che competono per l'accesso alle risorse o per il completamento di un'attività.
- **Caratteristiche**:
  - Mirano a ottenere vantaggio su altri processi nell'allocazione di risorse o nell'assegnazione di compiti.
  - Possono utilizzare strategie di pianificazione e di accesso alle risorse per ottimizzare la propria esecuzione.
  - Le attività possono essere prioritarie, in modo che alcuni processi ricevano trattamenti preferenziali rispetto ad altri.

#### Interazioni e Relazioni
- **Interazioni**:
  - I processi indipendenti operano in modo isolato.
  - I processi cooperativi lavorano insieme per raggiungere un obiettivo comune.
  - I processi competitivi competono per risorse o priorità.
- **Relazioni**:
  - Possono coesistere all'interno di un sistema complesso, dove alcuni processi possono essere indipendenti, mentre altri sono cooperativi o competitivi.

### Stati di un Processo

#### Stati Principali
- **Nuovo (New)**:
  - Il processo è stato creato ma non è ancora stato ammesso al sistema operativo per l'esecuzione.
  - Le risorse necessarie al processo devono essere allocate prima che possa passare allo stato "Pronto".
- **Esecuzione (Running)**:
  - Il processo sta eseguendo le sue istruzioni sulla CPU.
  - Solo un processo può essere in stato di esecuzione su una CPU in un dato momento.
- **In Attesa o Sospeso (Waiting)**:
  - Il processo è temporaneamente sospeso, spesso in attesa di un evento esterno come un'operazione di I/O o un segnale.
  - Non può continuare l'esecuzione fino a quando non avviene l'evento desiderato.
- **Pronto (Ready-to-Run)**:
  - Il processo è pronto per l'esecuzione ma deve attendere il suo turno per l'assegnazione della CPU.
  - Viene mantenuto in una coda dei processi pronti, in attesa di essere selezionato dallo scheduler della CPU.
- **Terminato o Finito (Terminated)**:
  - Il processo ha completato la sua esecuzione o è stato terminato dall'utente o dal sistema operativo.
  - Rilascia tutte le risorse allocate e può essere eliminato dal sistema.

## Vita di un Processo

### Assegnazione di un Identificatore e Inserimento nella Ready List
- Il nuovo processo viene assegnato un identificatore unico (PID, Process IDentifier).
- Viene inserito nell'elenco dei processi pronti (RL, Ready List), in attesa che arrivi il suo turno per l'utilizzo della CPU.

### Stato di Esecuzione
- Quando al processo viene assegnata la CPU, passa nello stato di esecuzione.
- Può uscire da questo stato per tre motivi:
  - Termina la sua esecuzione.
  - Termina il suo tempo di esecuzione.
  - Manca la disponibilità di una risorsa necessaria.

### Dallo Stato di Sospeso allo Stato di Pronto
- Da uno stato di sospeso (attesa), il processo non può passare direttamente a quello di esecuzione.
- Quando la risorsa che il processo sta "aspettando" diventa disponibile, il processo viene rimosso dalla WL (Waiting List) e inserito nella RL (Ready List), pronti ad accedere alla CPU.

## Descrittore del Processo (PCB)

Il descrittore del processo (PCB) contiene i principali dati che rappresentano lo stato del processo:

- **Identificatore Unico (PID)**:
  - Identificatore numerico univoco assegnato al processo.
- **Stato Corrente**:
  - Indica lo stato attuale del processo (es. Nuovo, Pronto, Esecuzione, Sospeso, Terminato).
- **Program Counter**:
  - Indica l'indirizzo di memoria dell'istruzione successiva da eseguire all'interno del processo.
- **Registri**:
  - Contiene i valori correnti dei registri della CPU associati al processo.
- **Priorità**:
  - Indica la priorità del processo rispetto ad altri processi nella coda dei processi pronti.
- **Puntatori alla Memoria del Processo**:
  - Indica l'area di memoria assegnata al processo.
- **Puntatori alle Risorse Allocate al Processo**:
  - Indica le risorse di sistema allocate al processo, come file aperti, dispositivi I/O in uso, ecc.

## Scheduling
- **Obiettivo**: Migliorare le prestazioni del sistema.
- **Tipi di Scheduling**:
  - **Scheduling dei Job**:
    - Gestione dell'ordine e delle priorità dei job in attesa.
  - **Scheduling della CPU**:
    - Assegnazione della CPU ai processi in esecuzione.

## Tipologie del Parallelismo

### Multitasking
- **Definizione**: Esecuzione di più task (processi) in modo apparentemente simultaneo su una singola CPU.
- **Caratteristiche**:
  - Basato sulla condivisione di tempo della CPU.
  - Implementato tramite lo scheduling della CPU.

### Multiprocessing
- **Definizione**: Utilizzo di più CPU (o core) per eseguire processi simultaneamente.
- **Caratteristiche**:
  - Può eseguire più processi contemporaneamente in modo reale.
  - Aumenta la capacità di elaborazione parallela.

## Criteri di Scheduling

### Obiettivi Primari delle Politiche di Scheduling

Gli obiettivi primari delle politiche di scheduling sono:

- **Massimizzare la Percentuale di Utilizzo della CPU**:
  - Assicurarsi che la CPU sia sempre occupata con un processo attivo per massimizzare l'efficienza del sistema.
- **Massimizzare il Throughput del Sistema**:
  - Aumentare la quantità di lavoro completato nell'unità di tempo per ottimizzare le risorse del sistema.
- **Ridurre al Minimo i Tempi di Risposta**:
  - Garantire una risposta rapida ai processi interattivi o in tempo reale per migliorare l'esperienza utente.
- **Minimizzare i Tempi di Attesa**:
  - Ridurre il tempo in cui i processi rimangono inattivi o in stato di sospensione per massimizzare l'utilizzo delle risorse.
- **Ottimizzare il Burst di CPU e di I/O**:
  - Ottimizzare il tempo trascorso da un processo in esecuzione sulla CPU e il tempo necessario per completare le operazioni di I/O.

### Tipi di Criteri di Scheduling

#### First-Come, First-Served (FCFS)
- I processi vengono eseguiti nell'ordine in cui arrivano.
- È un approccio non preemptive, il che significa che un processo in esecuzione non può essere interrotto finché non termina o passa allo stato di sospeso.

#### Shortest Job Next (SJN)
- Viene dato la priorità al processo con il tempo di esecuzione più breve.
- È un approccio non preemptive, poiché la CPU viene assegnata al processo più corto finché non termina o passa allo stato di sospeso.

#### Priority Scheduling
- I processi vengono eseguiti in base alla loro priorità.
- Un processo con priorità più alta riceve la CPU prima rispetto a quelli con priorità più bassa.
- Può essere preemptive o non preemptive.

#### Round Robin (RR)
- I processi vengono eseguiti in round-robin, assegnando a ciascuno un intervallo di tempo fisso (quantum).
- Dopo l'intervallo di tempo, il processo viene sospeso e inserito nella coda dei processi pronti.
- È un approccio preemptive, in quanto un processo può essere interrotto per assegnare la CPU a un altro processo.

#### Multilevel Queue Scheduling
- I processi vengono assegnati a diverse code a seconda della loro priorità o del tipo di lavoro.
- Le code vengono gestite separatamente, ognuna con il proprio algoritmo di scheduling.
- Le code possono essere organizzate gerarchicamente o in base a criteri specifici.

### Scelta del Criterio di Scheduling
La scelta del criterio di scheduling dipende dalle esigenze del sistema e dagli obiettivi di prestazione. Ad esempio, in un sistema in tempo reale, dove la risposta rapida è critica, potrebbe essere preferibile un approccio preemptive come Round Robin. Al contrario, in un sistema in cui si desidera massimizzare l'utilizzo della CPU, l'approccio FCFS potrebbe essere più appropriato.

## Obiettivi dei Sistemi Operativi

### Obiettivi Generali

I sistemi operativi si propongono di raggiungere una serie di obiettivi generali per garantire un funzionamento efficace e efficiente del sistema nel suo complesso:

- **Equità**:
  - Garantire un trattamento equo e giusto di tutti i processi e gli utenti del sistema, evitando situazioni di favoritismo o discriminazione.

- **Bilanciamento**:
  - Distribuire equamente le risorse del sistema, come la CPU, la memoria e i dispositivi di I/O, per massimizzare l'utilizzo e prevenire sovrautilizzo o sottoutilizzo.

- **Attuare Politiche di Controllo e Uso della CPU**:
  - Implementare politiche di scheduling efficaci per controllare l'allocazione della CPU e massimizzare l'efficienza del sistema.

### Obiettivi Specifici

Oltre agli obiettivi generali, i sistemi operativi possono adattare le proprie funzionalità per soddisfare esigenze specifiche in base al tipo di sistema o alle priorità degli utenti:

#### Sistemi Batch
- **Massimizzare il Throughput**:
  - L'obiettivo principale è completare il maggior numero possibile di lavori nell'unità di tempo, ottimizzando il tempo di esecuzione complessivo.

#### Sistemi Interattivi
- **Minimizzare i Tempi di Risposta**:
  - Priorità alla risposta rapida alle richieste degli utenti per migliorare l'esperienza interattiva.

#### Sistemi Real-Time
- **Rispettare le Deadline**:
  - Garantire che i processi critici abbiano accesso alla CPU e alle risorse necessarie entro i limiti temporali specificati, per evitare fallimenti o perdite di dati.

### Adattabilità degli Obiettivi
Va notato che gli obiettivi possono sovrapporsi e variare in base al contesto operativo e alle esigenze specifiche del sistema. I sistemi operativi devono essere flessibili e adattabili per soddisfare una vasta gamma di requisiti e scenari di utilizzo.
