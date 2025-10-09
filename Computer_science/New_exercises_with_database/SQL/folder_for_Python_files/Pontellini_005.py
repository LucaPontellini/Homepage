import sqlite3

def create_tables():
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
        Anno INTEGER,
        Genere TEXT,
        FOREIGN KEY (Autore_id) REFERENCES Autori(Id)
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Prestiti (
        Id INTEGER PRIMARY KEY,
        Libro_id INTEGER NOT NULL,
        Utente TEXT NOT NULL,
        Data_prestito TEXT,
        Data_restituzione TEXT,
        FOREIGN KEY (Libro_id) REFERENCES Libri(Id)
    );
    ''')

    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()

    autori = [
        (1, 'Mario', 'Rossi'),
        (2, 'Lucia', 'Bianchi'),
        (3, 'Alessandro', 'Verdi')
    ]

    libri = [
        (1, 'Il mistero del castello', 1, 2020, 'Giallo'),
        (2, 'Viaggio nel tempo', 1, 2018, 'Fantascienza'),
        (3, 'La cucina italiana', 2, 2019, 'Cucina'),
        (4, 'Storia antica', 3, 2021, 'Storia'),
        (5, 'Romanzo moderno', 3, 2022, 'Narrativa'),
        (6, 'Il ritorno del castello', 1, 2023, 'Giallo')
    ]

    prestiti = [
        (1, 1, 'Mario Rossi', '2023-01-01', '2023-01-15'),
        (2, 2, 'Lucia Bianchi', '2023-02-01', None),
        (3, 3, 'Alessandro Verdi', '2023-03-01', '2023-03-10'),
        (4, 4, 'Mario Rossi', '2023-04-01', None)
    ]

    cursor.executemany('INSERT OR IGNORE INTO Autori VALUES (?, ?, ?)', autori)
    cursor.executemany('INSERT OR IGNORE INTO Libri VALUES (?, ?, ?, ?, ?)', libri)
    cursor.executemany('INSERT OR IGNORE INTO Prestiti VALUES (?, ?, ?, ?, ?)', prestiti)

    conn.commit()
    conn.close()

def query_libri_per_autore(autore_id):
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT Libri.Titolo, Libri.Anno, Libri.Genere
    FROM Libri
    JOIN Autori ON Libri.Autore_id = Autori.Id
    WHERE Autori.Id = ?
    ''', (autore_id,))

    results = cursor.fetchall()
    conn.close()
    return results

def query_prestiti_per_utente(utente):
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT Libri.Titolo, Prestiti.Data_prestito, Prestiti.Data_restituzione
    FROM Prestiti
    JOIN Libri ON Prestiti.Libro_id = Libri.Id
    WHERE Prestiti.Utente = ?
    ''', (utente,))

    results = cursor.fetchall()
    conn.close()
    return results

def query_libri_per_genere():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT Genere, COUNT(*) as NumeroLibri
    FROM Libri
    GROUP BY Genere
    HAVING COUNT(*) > 1
    ''')

    results = cursor.fetchall()
    conn.close()
    return results

def query_autori_con_piu_libri():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT Autori.Nome || ' ' || Autori.Cognome AS Autore, COUNT(Libri.Id) AS NumeroLibri
    FROM Autori
    JOIN Libri ON Autori.Id = Libri.Autore_id
    GROUP BY Autori.Id
    ORDER BY NumeroLibri DESC
    ''')

    results = cursor.fetchall()
    conn.close()
    return results

def query_prestiti_non_restituiti():
    conn = sqlite3.connect('libreria.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT Libri.Titolo, Prestiti.Utente, Prestiti.Data_prestito
    FROM Prestiti
    JOIN Libri ON Prestiti.Libro_id = Libri.Id
    WHERE Prestiti.Data_restituzione IS NULL
    ''')

    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == '__main__':
    create_tables()
    insert_data()

    print("Libri di Mario Rossi:")
    for libro in query_libri_per_autore(1):
        print(libro)

    print("\nPrestiti di Mario Rossi:")
    for prestito in query_prestiti_per_utente('Mario Rossi'):
        print(prestito)

    print("\nNumero di libri per genere (solo generi con più di 1 libro):")
    for genere in query_libri_per_genere():
        print(genere)

    print("\nAutori ordinati per numero di libri:")
    for autore in query_autori_con_piu_libri():
        print(autore)

    print("\nPrestiti non ancora restituiti:")
    for prestito in query_prestiti_non_restituiti():
        print(prestito)