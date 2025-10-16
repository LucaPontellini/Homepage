L'Italia è uno dei maggiori produttori di vino al mondo; numerose denominazioni, vitigni autoctoni e tradizioni locali caratterizzano il territorio. Il progetto prevede la realizzazione di una banca dati per la raccolta, gestione e consultazione dei dati relativi alle aziende vinicole e alle produzioni dei loro vigneti.

Per consentire una modellazione coerente sono state individuate le seguenti informazioni e vincoli:

- Le aziende vinicole sono identificate da una partita IVA (o codice fiscale) e hanno: nome, via, numero civico, comune, provincia e regione.
- Ogni azienda può possedere più vigneti. Un vigneto è individuato da un codice univoco e annotato con: nome, superficie totale (ettari), località, comune, classe di esposizione (es: "nord", "sud", "est", "ovest") e numero di filari.
- Ogni vigneto è suddiviso in uno o più blocchi (parcelle), ciascuno con un codice identificativo, superficie (ettari), e classe di esposizione. Questa suddivisione permette di rappresentare variazioni locali all'interno dello stesso vigneto.
- I vitigni sono caratterizzati da nome scientifico, nome comune, colore della bacca ("rossa" o "bianca") e origine genetica.
- I vitigni sono piantati a livello di blocco: per ogni blocco si specifica quali vitigni vi sono coltivati e, per ciascuno, la percentuale della superficie del blocco occupata dal vitigno. Questa struttura permette composizioni diverse tra blocchi dello stesso vigneto.
- Le etichette di vino rappresentano l'unità di produzione commerciale: ogni etichetta ha nome, annata e tipologia (es: "DOC", "IGT", "Vino da Tavola"). Un'etichetta è prodotta da un'azienda, proviene da un vigneto principale e può essere associata a un vitigno prevalente.

Si richiede di modellare il dominio mediante un diagramma ER in cui siano chiaramente rappresentate entità, attributi (con chiavi primarie e chiavi esterne), relazioni e cardinalità.

```mermaid

erDiagram
    AZIENDA_VINICOLA {
      str partita_IVA PK
      str codice_fiscale PK
      str nome
      str via
      str numero_civico
      str comune
      str provincia
      str regione
    }

    VIGNETO {
      str codice_vigneto PK
      str nome
      float superficie_totale
      str localita
      str comune
      list classe_esposizione
      int numero_filari
    }

    PARCELLA {
      str codice_parcella PK
      float superficie
      list classe_esposizione
    }

    VITIGNI {
      str nome_scientifico
      str nome_comune
      tuple colore_bacca
      str origine_genetica
    }

    BLOCCO {
      str codice_blocco PK
      float percentuale_superficie
    }

    ETICHETTA_DEL_VINO {
      str nome
      int annata
      list tipologia
    }

    AZIENDA_VINICOLA ||--o{ VIGNETO : possiede
    VIGNETO ||--o{ PARCELLA : suddiviso_in
    PARCELLA ||--o{ BLOCCO : contiene
    BLOCCO }o--|| VITIGNI : coltivato_con
    AZIENDA_VINICOLA ||--o{ ETICHETTA_DEL_VINO : produce
    VIGNETO ||--o{ ETICHETTA_DEL_VINO : vigneto_principale
    VITIGNI ||--o{ ETICHETTA_DEL_VINO : vitigno_prevalente
```