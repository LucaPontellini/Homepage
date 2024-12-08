# Trasmissione via cavo

I cavi elettrici sono fondamentali per la trasmissione di segnali e dati. Comprendendo le loro caratteristiche e problemi associati, possiamo migliorare l'efficienza delle comunicazioni.

## Tipologie di cavi

Nel mondo delle reti di comunicazione, esistono diverse tipologie di cavi utilizzati per trasmettere segnali e dati:

- **Twisted Pair**: Utilizzato nelle reti Ethernet, consiste in coppie di fili intrecciati.
- **Coassiale (coax)**: Utilizzato per trasmettere segnali RF e dati ad alta velocità, come televisori via cavo e Internet.

## Caratteristiche dei cavi elettrici

I cavi elettrici presentano una serie di caratteristiche che influenzano la trasmissione dei segnali:

- **Resistenza (R)**: Il cavo ha una resistenza passiva che frena il moto di scorrimento del flusso di elettroni. La formula è: R = (k * l) / S.
  - \( R \): Resistenza (ohm) - Misura la difficoltà del cavo al passaggio della corrente.
  - \( k \): Resistività (ohm * metro) - Proprietà del materiale del cavo di opporsi alla corrente.
  - \( l \): Lunghezza (metri) - La distanza del cavo attraverso cui la corrente deve fluire.
  - \( S \): Sezione trasversale (metri quadrati) - L'area della sezione trasversale del cavo.
- **Capacità (C)**: Proprietà di un materiale dielettrico posto fra 2 conduttori di conservare la carica elettrica quando esiste una differenza di potenziale fra i 2 conduttori. La formula è: C = Q / |ΔV|.
  - \( C \): Capacità (farad) - Misura la capacità del cavo di immagazzinare carica elettrica.
  - \( Q \): Carica (coulomb) - La quantità di carica elettrica immagazzinata.
  - \( \Delta V \): Differenza di potenziale (volt) - La differenza di tensione tra i due conduttori.
- **Induttanza (L)**: Quando 2 conduttori sono percorsi da correnti uguali e contrarie, si viene a creare un campo magnetico (B) nello spazio fra i 2 conduttori. Il rapporto fra il flusso magnetico generato e la corrente che lo ha generato è l'induttanza. La formula è: L = Φ(I) / i.
  - \( L \): Induttanza (henry) - Misura la capacità del cavo di opporsi ai cambiamenti di corrente.
  - \( \Phi(I) \): Flusso magnetico (weber) - La quantità di flusso magnetico generato.
  - \( i \): Corrente (ampere) - La corrente che attraversa il cavo.
- **Impedenza caratteristica (Z)**: La risultante degli elementi passivi che si oppongono al flusso degli elettroni (R, C, L). Non ha un'unità di misura specifica, ma comunemente viene espressa in ohm.

## Problemi dei cavi

Durante la trasmissione, i cavi elettrici possono incontrare diversi problemi che influenzano la qualità del segnale trasmesso. Vediamo due problemi comuni:

- **Attenuazione**: È la riduzione dell'ampiezza del segnale in ingresso rispetto a quello in uscita. È proporzionale alla lunghezza del cavo (αl) e alla radice quadrata della frequenza (α√f).
  
- **Diafonia (cross-talk)**: È un'interferenza che si verifica fra due conduttori vicini. Durante la trasmissione, il segnale presente in un conduttore si trasferisce per induzione al conduttore vicino, creando un disturbo alla trasmissione.

## Classificazione della diafonia

Per comprendere appieno la diafonia e i suoi effetti sulla trasmissione, è utile classificarla in due categorie principali:

- **NEXT (Near End Cross Talk)**: Si riferisce alla diafonia che si verifica vicino alla sorgente del segnale, generalmente all'estremità di un cavo trasmittente. 
- **FEXT (Far End Cross Talk)**: Si riferisce alla diafonia che si verifica lontano dalla sorgente del segnale, generalmente all'estremità di un cavo ricevente.

## Doppino (Twisted Pair)

Il doppino, o twisted pair, è un tipo comune di cavo elettrico utilizzato nelle reti di comunicazione. È formato da due fili conduttori, generalmente di rame, avvolti da una guaina isolante. Ciò che distingue il doppino è la sua caratteristica di attorcigliamento dei fili, nota come binatura. Questo processo di attorcigliamento riduce il rumore esterno e le interferenze, migliorando la qualità della trasmissione dei segnali.

### Cavi UTP (Unshielded Twisted Pair)

Il cavo UTP è una tipologia di cavo twisted pair non schermato e costituito da quattro doppini attorcigliati tra di loro. Questa configurazione offre diversi vantaggi:

- **Riduzione di interferenze e cross-talk**: L'intreccio dei doppini contribuisce a ridurre interferenze e disturbi durante la trasmissione.
- **Caratteristiche principali**:
  - Impedenza: 100 ohm
  - Lunghezza tipica: 100 metri
  - Facile installazione
  - Costo contenuto
  - Flessibilità
  - Dimensioni ridotte (circa 0,43 cm di diametro)
- **Alte prestazioni**: Le versioni più recenti dei cavi UTP possono supportare una banda passante fino a 10 Gbps.

Nei cavi UTP, i doppini sono organizzati in un preciso ordine e ciascun filo è identificato da un colore specifico. Ad esempio, l'ordine dei fili potrebbe essere il seguente:

#### RJ45 per cavi UTP:
1. Pin 1: Verde chiaro (trattato)
2. Pin 2: Verde
3. Pin 3: Arancione chiaro (trattato)
4. Pin 4: Blu (trattato) - Utilizzato per la connessione telefonica (sconsigliata)
5. Pin 5: Blu chiaro - Utilizzato per la connessione telefonica (sconsigliata)
6. Pin 6: Arancione
7. Pin 7: Marrone chiaro (trattato) - Inutilizzato
8. Pin 8: Marrone - Inutilizzato

Questo schema permette di distinguere facilmente i singoli doppini e assicura una corretta disposizione dei fili durante la creazione dei cavi UTP.

### Tipologie di Cavi RJ45

I cavi RJ45 più utilizzati sono di due tipi principali:

1. **Cavo Dritto (Straight-through)**
   - Utilizzato per collegare dispositivi diversi, come un computer a un router o a uno switch.
   - Nei cavi dritti, i pin sui due connettori RJ45 seguono lo stesso schema di cablaggio.

2. **Cavo Incrociato (Crossover)**
   - Utilizzato per collegare dispositivi simili, ad esempio un computer a un altro computer o un router a un router.
   - Nei cavi incrociati, i fili nei connettori RJ45 sono incrociati in modo che i pin utilizzati per la trasmissione da un dispositivo siano collegati ai pin utilizzati per la ricezione sull'altro dispositivo.

Queste due tipologie di cavi RJ45 sono fondamentali per garantire una corretta connessione tra dispositivi di rete e possono essere facilmente identificate in base al tipo di cablaggio utilizzato.

### Fibra Ottica

La fibra ottica è un mezzo di trasmissione che utilizza la luce per trasportare il segnale. Le fibre ottiche utilizzano la radiazione infrarossa, con lunghezze d'onda di 0,85µm, 1,35µm e 1,55µm (1 µm = 1 × 10^-6 m) . 

#### Principi dell'Ottica:

- **Propagazione rettilinea**: La luce si propaga in linea retta all'interno di un mezzo trasparente omogeneo e isotropo.
  - **Omogeneo**: Significa che le proprietà ottiche del mezzo sono uniformi in tutte le direzioni e in tutti i punti del materiale. In altre parole, la densità (ρ) e l'indice di rifrazione (n) della fibra ottica sono costanti lungo tutta la sua lunghezza e in tutte le direzioni.
  - **Isotropo**: Significa che il comportamento della luce nel mezzo è lo stesso in tutte le direzioni. In una fibra ottica isotropa, la propagazione della luce non è influenzata dalla direzione in cui la luce viaggia attraverso la fibra.
  
- **Rifrazione e Legge di Snell**: Quando la luce passa attraverso il confine tra due mezzi trasparenti con diversi indici di rifrazione, la sua direzione di propagazione cambia. Questo fenomeno è chiamato rifrazione, e la sua legge è definita dalla Legge di Snell, che stabilisce che il rapporto dei seni degli angoli di incidenza (θi) e rifrazione (θt) è uguale al rapporto degli indici di rifrazione dei due mezzi: n1 * sin(θi) = n2 * sin(θt).

  Nella legge di Snell:
  - ( θi ): Angolo di incidenza
  - ( θt ): Angolo di rifrazione
  - ( n_1 ) e ( n_2 ): Indici di rifrazione dei due mezzi. L'indice di rifrazione è il rapporto tra la velocità della luce nel vuoto ( c ) e la velocità della luce in un mezzo specifico ( v ) , quindi n = c / v dove ( n >= 1 ).


  Possiamo anche esprimere la Legge di Snell come:

  (sin θi / sin θt) = (n2 / n1)

  Questa relazione è utile perché consente di calcolare l'angolo di rifrazione ( θt ) conoscendo l'angolo di incidenza ( θi ) e gli indici di rifrazione ( n1 ) e ( n2 ) dei due mezzi coinvolti.

Questi principi sono fondamentali per comprendere il funzionamento della fibra ottica e le sue applicazioni nelle reti di comunicazione.

- **Casi Specifici di Rifrazione**:
  - **Caso 1: n1 < n2**
    - Descrizione: La luce passa da un materiale meno denso a uno più denso.
    - Caratteristiche:
      - L'angolo di deviazione della luce rispetto alla normale è minore rispetto all'angolo di incidenza.
      - Esempi includono quando la luce passa dall'aria alla superficie di separazione dell'acqua o del vetro.
  - **Caso 2: n2 > n1**
    - Descrizione: La luce passa da un materiale più denso a uno meno denso.
    - Caratteristiche:
      - L'angolo di deviazione della luce rispetto alla normale è maggiore rispetto all'angolo di incidenza.
      - Esempi includono quando la luce passa dalla superficie di separazione dell'acqua o del vetro all'aria.

- **Riflessione Totale**:
  - Descrizione: La riflessione totale interna si verifica quando la luce passa da un mezzo con un alto indice di rifrazione a uno con un basso indice di rifrazione e l'angolo di incidenza supera un certo valore critico. In questo caso, la luce viene riflessa completamente all'interno del mezzo più denso senza essere rifratta nell'altro mezzo.
  - Esempi includono quando la luce passa attraverso la fibra ottica e viene riflessa all'interno del nucleo della fibra.

Queste descrizioni illustrano come la luce cambia direzione quando passa attraverso materiali con diversi indici di rifrazione, in relazione alla normale e alla superficie di separazione.

### Struttura della Fibra Ottica

La fibra ottica è costituita da diverse parti che lavorano insieme per consentire la trasmissione ottimale della luce. Ecco una descrizione della struttura tipica di una fibra ottica:

- **Nucleo**: Questa è la parte centrale della fibra ottica attraverso cui passa la luce. È composto da vetro altamente trasparente con un alto indice di rifrazione. Il nucleo svolge il ruolo principale nella guida della luce lungo la fibra.

- **Strato di Cladding**: Il nucleo è circondato da uno strato esterno chiamato cladding. Il cladding è realizzato con un materiale otticamente meno denso rispetto al nucleo e ha un indice di rifrazione più basso. Questa differenza di densità tra il nucleo e il cladding consente alla luce di essere confinata nel nucleo attraverso il fenomeno della riflessione totale interna.

- **Rivestimento**: All'esterno del cladding c'è un rivestimento protettivo che offre una barriera meccanica e di isolamento per la fibra ottica. Questo rivestimento può essere realizzato in materiali diversi, come polimeri o materiali compositi, e ha lo scopo di proteggere la fibra dagli agenti esterni e dai danni meccanici.

La combinazione di questi elementi consente alla fibra ottica di trasmettere la luce lunghe distanze con minima attenuazione e dispersione del segnale, rendendola una scelta efficace per le reti di comunicazione ad alta velocità e ad alta capacità.