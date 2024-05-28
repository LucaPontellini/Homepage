# Mappa Concettuale sui Sistemi Operativi

## Fasi per Accendere il Computer:

### 1. Creazione del programma di Bootstrap
- **Scritto da**: Produttore dell'hardware
- **Memorizzato in**: Memoria ROM (Read Only Memory)
  - **Definizione**: Memoria "a sola lettura"
  - **Caratteristiche**:
    - L'utilizzatore può solo leggerla
    - Il contenuto non può essere modificato

### 2. Alimentazione del computer
- L'alimentazione viene fornita al computer
- Componente hardware riceve corrente

### 3. Indirizzo di Caricamento del S.O.
- **Indirizzo Specifico**: 0xFFFFFFF0

### 4. Autodiagnostica POST (Power On Self Test)
- **Descrizione**:
  - Ogni componente hardware esegue un programma di autodiagnostica
  - Serie di test per verificare il corretto funzionamento del dispositivo

    ### Cosa fa il POST:

    - **Autodiagnostica della Scheda Madre**: Verifica il funzionamento dei componenti critici della scheda madre. Se tutti i test danno esito favorevole, viene emesso un segnale acustico (beep) e si procede con il test della scheda video.

    - **Autodiagnostica della Scheda Video**: Verifica il corretto funzionamento della scheda video.

    - **Conteggio della Memoria Dinamica**: Verifica il funzionamento della memoria dinamica (RAM).

    - **Controlli su Tastiera, Mouse e Periferiche di Input**: Verifica il corretto funzionamento delle periferiche di input come tastiera e mouse.

    - **Controlli sulle Periferiche Collegate**: Verifica il corretto funzionamento delle periferiche collegate al computer, incluso il disco fisso.

### 5. Caricamento del Programma di Boot
- **Procedura**:
  - L'hardware è predisposto per caricare il programma di boot
  - Il caricamento inizia da un indirizzo specifico

### 6. Avvio del Sistema Operativo
- Una volta completati tutti i controlli e superata l'autodiagnostica, una parte del sistema operativo, chiamata kernel, viene caricata in memoria.
- Il kernel è il nucleo del sistema operativo e permette al computer di iniziare a operare.

# Sistema Operativo (S.O.)

- **Definizione**: Il sistema operativo è un gruppo di programmi che gestisce il funzionamento del computer, agendo come intermediario tra l'utente e il calcolatore.
- **Ruolo**: Fa parte del software di base, che è composto da programmi essenziali per il funzionamento del computer.
- **Funzioni**:
  - Gestione delle risorse hardware e software
  - Gestione dei file e delle periferiche
  - Fornisce un'interfaccia per l'utente

## Software di Base

- **Definizione**: Insieme dei programmi che consentono a un utente di eseguire operazioni base, come costruire e mandare in esecuzione un programma applicativo.
- **Composizione**:
  - **Sistema Operativo (S.O.)**: Gestisce tutte le attività e le risorse del computer, fornendo un'interfaccia per l'utente e gestendo l'accesso alle periferiche.
  
  - **Editor**: Permette la creazione, la modifica e il salvataggio di documenti di testo, utili per scrivere codice o prendere appunti.
  
  - **Traduttori**: Convertire il codice scritto in un linguaggio di programmazione in istruzioni che il computer può capire e eseguire. Questo processo è chiamato compilazione o interpretazione.
  
  - **Linker**: Assembla diverse parti di codice e librerie per creare un programma eseguibile.
  
  - **Loader**: Carica il programma eseguibile in memoria quando lo si avvia, consentendo al computer di eseguirlo.
  
  - **Debugger**: Aiuta a individuare e risolvere errori nel programma, mostrando dove si sono verificati gli errori e aiutando a capire cosa è andato storto.

## Software Applicativo

- **Definizione**: Programmi progettati per svolgere specifiche attività o funzioni per l'utente.
- **Ruolo**: Serve all'utente per svolgere compiti specifici o lavorare con dati e informazioni.

## Possibilità di più Sistemi Operativi

- **Definizione**: Un singolo computer può ospitare più di un sistema operativo contemporaneamente.
- **Esempio**: È possibile avere sia Windows che Linux installati sullo stesso computer, permettendo all'utente di scegliere quale sistema operativo avviare all'avvio del computer.

### Metodi per Installare più Sistemi Operativi

1. **Dual Boot**:
   - **Descrizione**: Si installano due o più sistemi operativi sullo stesso disco rigido e, all'avvio del computer, si sceglie quale avviare.
   - **Esempio**: Installazione di Windows e Linux sullo stesso disco rigido.

2. **Virtualizzazione**:
   - **Descrizione**: Si utilizza un software di virtualizzazione per eseguire più sistemi operativi contemporaneamente su un'unica macchina.
   - **Esempio**: Utilizzo di VMware o VirtualBox per eseguire diverse istanze di Windows, Linux o altri sistemi operativi all'interno di una finestra del sistema operativo principale.

3. **Boot da Dispositivi Esterni**:
   - **Descrizione**: Si avvia il computer da dispositivi esterni come unità USB o CD/DVD che contengono sistemi operativi diversi.
   - **Esempio**: Avvio di un sistema operativo Linux da un'unità USB senza doverlo installare sul disco rigido.

### Marche di Sistemi Operativi

1. **Windows**:
   - **Descrizione**: Windows è un sistema operativo sviluppato da Microsoft ed è ampiamente utilizzato nei computer desktop, laptop e tablet. Offre una vasta gamma di funzionalità e supporto per il software di terze parti.

2. **Linux**:
   - **Descrizione**: Linux è un sistema operativo open source che è disponibile in molte distribuzioni diverse. È noto per la sua flessibilità, sicurezza e affidabilità ed è ampiamente utilizzato in server, computer desktop e dispositivi embedded.

3. **Android**:
   - **Descrizione**: Android è un sistema operativo open source sviluppato da Google ed è utilizzato principalmente nei dispositivi mobili come smartphone e tablet. Offre un'ampia selezione di app disponibili attraverso il Google Play Store.

4. **iOS**:
   - **Descrizione**: iOS è un sistema operativo sviluppato da Apple ed è utilizzato esclusivamente sui dispositivi mobili Apple come iPhone e iPad. È noto per la sua stabilità, sicurezza e integrazione con altri prodotti Apple.

5. **macOS**:
   - **Descrizione**: macOS è un sistema operativo sviluppato da Apple per i computer Mac. Offre una combinazione di prestazioni elevate, design elegante e integrazione con altri prodotti Apple.

## Ruoli Principali del Sistema Operativo

- **Gestione delle Risorse Hardware**:
  - Il sistema operativo gestisce le risorse hardware del computer, come la CPU, la memoria e le periferiche di input/output.
  - Assegna in modo efficiente le risorse ai programmi per consentire loro di eseguire le proprie operazioni.
  
- **Interfaccia Utente**:
  - Fornisce un'interfaccia tramite cui gli utenti possono comunicare con il computer.
  - Può essere sotto forma di riga di comando testuale o di un'interfaccia grafica utente (GUI).
  - Consente agli utenti di avviare programmi, gestire file e configurare le impostazioni di sistema.

## Funzioni Aggiuntive del Sistema Operativo

- **Gestione dei Processi**:
  - Il sistema operativo gestisce l'esecuzione dei processi, assegnando la CPU e la memoria ai vari programmi in esecuzione.
  - Monitora lo stato dei processi e li gestisce in base alle priorità e alle risorse disponibili.

- **Gestione della Memoria**:
  - Il sistema operativo gestisce l'allocazione della memoria del computer tra i diversi processi in esecuzione.
  - Assegna e dealloca la memoria in modo da ottimizzare l'utilizzo delle risorse disponibili.

- **Gestione dei File e dei Dispositivi di Archiviazione**:
  - Gestisce l'accesso ai file e ai dispositivi di archiviazione, consentendo agli utenti di creare, modificare e eliminare file.
  - Fornisce un'organizzazione logica dei file e delle directory nel sistema di archiviazione.

- **Gestione delle Periferiche di Input/Output**:
  - Il sistema operativo gestisce l'interazione con le periferiche di input/output, come tastiere, mouse e stampanti.
  - Fornisce driver e protocolli per consentire la comunicazione tra il computer e le periferiche collegate.

- **Gestione della Rete**:
  - Gestisce le connessioni di rete e facilita la comunicazione tra il computer e altri dispositivi sulla rete.
  - Fornisce protocolli di rete e servizi per l'invio e la ricezione di dati attraverso la rete.

## Struttura a "Buccia di Cipolla" del Sistema Operativo

1. **Nucleo (Kernel)**
   - Si trova al livello più basso della struttura.
   - Responsabile della gestione delle risorse hardware e delle operazioni fondamentali del sistema.

2. **Gestore della Memoria Centrale**
   - Livello che gestisce l'allocazione e la gestione della memoria centrale del computer.
   - Ottimizza l'uso della memoria per garantire prestazioni efficienti del sistema.

3. **Gestore delle Periferiche**
   - Si occupa della gestione e del controllo delle periferiche hardware, come tastiere, mouse e stampanti.
   - Fornisce un'interfaccia per l'accesso e il controllo delle periferiche da parte del sistema e dei programmi applicativi.

4. **File System**
   - Gestisce l'organizzazione, l'accesso e la memorizzazione dei file sul disco.
   - Fornisce un'interfaccia unificata per la gestione dei file da parte del sistema e degli utenti.

5. **Interfaccia con l'Utente (UI)**
   - **Interfaccia Utente a Caratteri (CUI - Character User Interface)**
     - Fornisce un'interfaccia testuale che permette agli utenti di interagire con il sistema attraverso l'inserimento di comandi testuali.
   - **Interfaccia Utente Grafica (GUI - Graphical User Interface)**
     - Offre un'interfaccia grafica interattiva basata su finestre, icone e menu, semplificando l'interazione con il sistema per gli utenti.

6. **Programmi Applicativi**
   - Livello più alto della struttura, composto dai programmi che gli utenti eseguono per svolgere specifiche attività o compiti.
   - Utilizzano le funzionalità fornite dai livelli inferiori del sistema operativo per accedere alle risorse hardware e gestire i dati.