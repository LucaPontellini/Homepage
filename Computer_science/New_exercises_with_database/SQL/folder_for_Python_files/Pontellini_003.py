# Esercizio: database studenti

# - Crea un database SQLite chiamato "scuola.db".
# - Crea due tabelle:
#   - Studenti: Matricola (INTEGER PRIMARY KEY), Nome (TEXT NOT NULL), Cognome (TEXT NOT NULL).
#   - Esami: Id (INTEGER PRIMARY KEY AUTOINCREMENT), Matricola (INTEGER NOT NULL), Corso (TEXT NOT NULL), Voto (INTEGER), con FOREIGN KEY su Studenti(Matricola).
# - Inserisci i seguenti dati (tutti gli studenti devono avere gli stessi record di esami):
#   - Studenti:
#     - Matricola 101, Nome Mario, Cognome Rossi
#     - Matricola 102, Nome Lucia, Cognome Bianchi
#   - Esami (da inserire per ogni studente: per Matricola 101 e per Matricola 102):
#     - Corso "Matematica", Voto 28
#     - Corso "Informatica", Voto 30
#     - Corso "Fisica", Voto 27
# - Esegui tre query semplici:
#   1. Elenco di tutti gli studenti (Matricola, Nome, Cognome).
#   2. Elenco dei corsi e voti sostenuti da uno studente specifico (usa la matricola 101 come esempio).
#   3. Numero di esami sostenuti per ciascuno studente (GROUP BY Matricola).

# Suggerimento: usa INSERT OR IGNORE per evitare errori su violazioni di vincoli (es. PRIMARY KEY)

import sqlite3

conn = sqlite3.connect('scuola.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Studenti (
    Matricola INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    Cognome TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Esami (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Matricola INTEGER NOT NULL,
    Corso TEXT NOT NULL,
    Voto INTEGER,
    FOREIGN KEY (Matricola) REFERENCES Studenti(Matricola)
);
''')

studenti = [
    (101, 'Mario', 'Rossi'),
    (102, 'Lucia', 'Bianchi')
]

esami = [
    (101, 'Matematica', 28),
    (101, 'Informatica', 30),
    (101, 'Fisica', 27),
    (102, 'Matematica', 28),
    (102, 'Informatica', 30),
    (102, 'Fisica', 27)
]

cursor.executemany('INSERT OR IGNORE INTO Studenti (Matricola, Nome, Cognome) VALUES (?, ?, ?);', studenti)
cursor.executemany('INSERT INTO Esami (Matricola, Corso, Voto) VALUES (?, ?, ?);', esami)

conn.commit()

print("Elenco di tutti gli studenti:")
cursor.execute('SELECT Matricola, Nome, Cognome FROM Studenti;')
for row in cursor.fetchall():
    print(row)

print("\nElenco dei corsi e voti sostenuti dallo studente con Matricola 101:")
cursor.execute('SELECT Corso, Voto FROM Esami WHERE Matricola = 101;')
for row in cursor.fetchall():
    print(row)

print("\nNumero di esami sostenuti per ciascuno studente:")
cursor.execute('SELECT Matricola, COUNT(*) as NumeroEsami FROM Esami GROUP BY Matricola;')
for row in cursor.fetchall():
    print(row)

conn.close()