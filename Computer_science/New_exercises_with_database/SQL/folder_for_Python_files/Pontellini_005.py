import sqlite3

conn = sqlite3.connect('libreria.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Autori (
    Id INTEGER PRIMARY KEY,
    Nome TEXT NOT NULL,
    Cognome TEXT NOT NULL
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Libri (
    Id INTEGER PRIMARY KEY,
    Titolo TEXT NOT NULL,
    Autore_id INTEGER,
    FOREIGN KEY (Autore_id) REFERENCES Autori(id)
    Anno INTEGER,
    Genere TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Prestiti (
    Id INTEGER PRIMARY KEY,
    Libro_id INTEGER NOT NULL,
    FOREIGN KEY (Libro_id) REFERENCES Libri(Id),
    Utente TEXT NOT NULL,
    Data_prestito TEXT,
    Data_restituzione TEXT
);
''')