# 📘 Funzioni principali di `re` in Python

## 🔍 `re.search()`
Cerca la **prima occorrenza** del pattern ovunque nella stringa.  
👉 Utile quando vuoi sapere se il pattern compare da qualche parte, non importa dove.

```python
import re

def esempio_search():
    m1 = re.search("gatto", "Il gatto dorme sul divano")
    if m1:
        print(m1.group())  # "gatto"
    else: print(None)

    m2 = re.search("divano", "Il gatto dorme sul divano")
    if m2:
        print(m2.group())  # "divano"
    else: print(None)

    m3 = re.search("cane", "Il gatto dorme sul divano")
    if m3:
        print(m3.group())
    else: print(None)  # None
```


## 🎯 `re.match()`
Controlla solo se il pattern è presente all’inizio della stringa.
👉 Utile per verificare se la stringa comincia con un certo testo.

```python
import re

def esempio_match():
    m1 = re.match("Il", "Il gatto dorme sul divano")
    if m1:
        print(m1.group())  # "Il"
    else: print(None)

    m2 = re.match("gatto", "Il gatto dorme sul divano")
    if m2:
        print(m2.group())
    else: print(None)  # None
```


## 📝 `re.fullmatch()`
Verifica se l’intera stringa corrisponde al pattern, dall’inizio alla fine.
👉 Utile quando vuoi essere sicuro che la stringa sia solo quel pattern.

```python
import re

def esempio_fullmatch():
    m1 = re.fullmatch(r"\d+", "12345")
    if m1:
        print(m1.group())  # "12345"
    else: print(None)

    m2 = re.fullmatch(r"\d+", "12345abc")
    if m2:
        print(m2.group())
    else: print(None)  # None
```


## 📋 `re.findall()`
Restituisce tutte le corrispondenze come lista.
👉 Utile per raccogliere tutte le occorrenze, non solo la prima.
Se ci sono gruppi di cattura (...), restituisce tuple con i valori dei gruppi.

```python
import re

def esempio_findall():
    # Senza gruppi
    risultato1 = re.findall(r"\d+", "Ci sono 12 gatti e 34 cani")
    if risultato1:
        print(risultato1)  # ["12", "34"]
    else: print(None)

    # Con gruppi
    risultato2 = re.findall(r"(\w+)=(\d+)", "set width=20 and height=10")
    if risultato2:
        print(risultato2)  # [("width", "20"), ("height", "10")]
    else: print(None)
```

### Testare tutto insieme su un file `.py`:
```python
import re

... # Vari def

# 🔽 Richiamo delle funzioni per vedere subito l'output
if __name__ == "__main__":
    esempio_search()
    esempio_match()
    esempio_fullmatch()
    esempio_findall()
```

### Struttura generica dei vari `re`:

```python
import re

# 🔍 re.search()
def esempio_search():
    # 1️⃣ Definisci il pattern che vuoi cercare
    pattern = "pattern"

    # 2️⃣ Definisci la stringa su cui cercare
    testo = "stringa"

    # 3️⃣ Applica re.search → cerca la prima occorrenza ovunque
    risultato = re.search(pattern, testo)

    # 4️⃣ Se trovato, stampa il contenuto con .group()
    print(risultato.group() if risultato else None)



# 🎯 re.match()
def esempio_match():
    # 1️⃣ Pattern da verificare
    pattern = "pattern"

    # 2️⃣ Stringa da analizzare
    testo = "stringa"

    # 3️⃣ Applica re.match → controlla solo all’inizio
    risultato = re.match(pattern, testo)

    # 4️⃣ Stampa il risultato se esiste
    print(risultato.group() if risultato else None)



# 📝 re.fullmatch()
def esempio_fullmatch():
    # 1️⃣ Pattern da verificare
    pattern = "pattern"

    # 2️⃣ Stringa da analizzare
    testo = "stringa"

    # 3️⃣ Applica re.fullmatch → deve combaciare tutta la stringa
    risultato = re.fullmatch(pattern, testo)

    # 4️⃣ Stampa il risultato se esiste
    print(risultato.group() if risultato else None)



# 📋 re.findall()
def esempio_findall():
    # 1️⃣ Pattern da cercare
    pattern = "pattern"

    # 2️⃣ Stringa da analizzare
    testo = "stringa"

    # 3️⃣ Applica re.findall → restituisce tutte le corrispondenze
    risultati = re.findall(pattern, testo)

    # 4️⃣ Stampa la lista dei risultati
    print(risultati)
```

### Legenda:
- pattern → è l’espressione regolare vera e propria, cioè la sequenza di simboli che definisce la regola di ricerca (ad esempio \d{2}/\d{2}/\d{4} per una data italiana).
- stringa → è l’esempio di testo che dovrebbe essere riconosciuto dal pattern (ad esempio 25/11/2025).

Quindi:
- il pattern è la “formula” che scrivi;
- la stringa è il “dato di prova” che deve combaciare con quella formula.