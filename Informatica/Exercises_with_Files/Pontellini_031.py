#Esercizio 1:
#Scrivi in un file.
#Crea un nuovo file denominato exercise1.txt e scrivi le seguenti righe:
#"Ciao, Mondo!"
#"Benvenuto nella gestione dei file in Python."

f = open ("exercise_1.txt", "w")
f.write ("Hello, world!\n")
f.write ("Welcome to file handing in Python")
f.close ()

#Esercizio 2:
#Leggi da un file. Leggi il contenuto del file exercise_1.txt e stamparlo nella console.

f = open ("exercise_1.txt", "r")
print (f.read ())
f.close ()

#Esercizio 3: Aggiungi a un file la seguente riga al file exercise_1.txt: 
#"Questa riga è stata aggiunta".

f = open ("exercise_1.txt", "a")
f.write ("\nThis line has been added")
f.close ()
print ()

#Esercizio 4: Leggi le righe dal file exercise1.txt riga per riga e stampare ogni riga nella console.

f = open ("exercise_1.txt", "r")

for file_line in f:
    print (file_line.rstrip ())

f.close ()

#Esercizio 5: Copia di un file. Crea una copia del file exercise_1.txt e denominala exercise_1_copy.txt.

import shutil

src = "exercise_1.txt"
dst = "exercise_1_copy.txt"

shutil.copy (src, dst)

f = open ("exercise_1.txt", "r")