# Assembly

## Operazioni di base
### ADD 
- Aggiunge due numeri.

### SUB 
- Sottrae un numero da un altro.

### MUL 
- Moltiplica due numeri.

### DIV 
- Divide un numero per un altro.

### CMP 
- Confronta due operandi sottraendo uno dall'altro. 
- Non modifica gli operandi, ma aggiorna il registro dei flag per le decisioni condizionali.

## Registri
### AX 
- Usato nelle operazioni aritmetiche. 
- Può essere suddiviso in:
    - AH: La parte alta (8 bit superiori) del registro `AX`.
    - AL: La parte bassa (8 bit inferiori) del registro `AX`.

### BX 
- Usato come puntatore ai dati. 
- Può essere suddiviso in:
    - BH: La parte alta (8 bit superiori) del registro `BX`.
    - BL: La parte bassa (8 bit inferiori) del registro `BX`.

### CX 
- Usato nei cicli e negli spostamenti. 
- Può essere suddiviso in:
    - CH: La parte alta (8 bit superiori) del registro `CX`.
    - CL: La parte bassa (8 bit inferiori) del registro `CX`.

### DX 
- Usato nelle operazioni aritmetiche e di input/output. 
- Può essere suddiviso in:
    - DH: La parte alta (8 bit superiori) del registro `DX`.
    - DL: La parte bassa (8 bit inferiori) del registro `DX`.

### SI/DI 
- Registri indice di origine/destinazione. 
- Usati come puntatori all'origine/destinazione nei trasferimenti di array. 
- L'offset di `SI` è relativo al segmento dei dati, mentre l'offset di `DI` è relativo al segmento extra. 
- Quando usati con parentesi (come [SI] o [DI]), fanno riferimento al valore all'indirizzo di memoria puntato dal registro. 
- Senza parentesi, fanno riferimento al valore del registro stesso.

## Salti
### JMP 
- Salto incondizionato. 
- Indipendentemente dallo stato del programma, l'esecuzione salta all'istruzione specificata.

### JNE 
- Salto se non uguale. 
- L'esecuzione salta all'istruzione specificata solo se l'ultima operazione di confronto ha determinato che i due valori non erano uguali.

### JL 
- Salto se inferiore. 
- L'esecuzione salta all'istruzione specificata solo se l'ultima operazione di confronto ha determinato che il primo valore era inferiore al secondo.

### JG 
- Salto se maggiore. 
- L'esecuzione salta all'istruzione specificata solo se l'ultima operazione di confronto ha determinato che il primo valore era maggiore al secondo.

### JE 
- Salto se uguale. 
- L'esecuzione salta all'istruzione specificata solo se l'ultima operazione di confronto ha determinato che i due valori erano uguali.

## Cicli
### Cicli in Assembly 
- Implementati utilizzando istruzioni di salto e CX.

## Vettori e stringhe
### Vettori 
- Implementati come blocchi di memoria contigui. 
- Ogni elemento del vettore occupa un certo numero di byte in memoria, e gli elementi sono disposti uno dopo l'altro senza spazi tra di loro. 
- La lunghezza fisica di un vettore si riferisce al numero totale di elementi che il vettore può contenere. 
- La lunghezza logica di un vettore si riferisce al numero di elementi attualmente presenti nel vettore.

### Stringhe 
- Implementati come vettori di caratteri.