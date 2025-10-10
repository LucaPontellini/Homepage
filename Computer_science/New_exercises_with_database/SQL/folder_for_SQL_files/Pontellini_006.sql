CREATE TABLE IF NOT EXISTS Autori (
    Id INTEGER PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL,
    Cognome VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Libri (
    Id INTEGER PRIMARY KEY,
    Titolo VARCHAR(50) NOT NULL,
    Autore_id INTEGER,
    Anno INTEGER,
    Genere VARCHAR(50),
    FOREIGN KEY (Autore_id) REFERENCES Autori(Id)
);

CREATE TABLE IF NOT EXISTS Prestiti (
    Id INTEGER PRIMARY KEY,
    Libro_id INTEGER NOT NULL,
    Utente VARCHAR(50) NOT NULL,
    Data_prestito VARCHAR(50),
    Data_restituzione VARCHAR(50),
    FOREIGN KEY (Libro_id) REFERENCES Libri(Id)
);

INSERT OR IGNORE INTO Autori (Id, Nome, Cognome) VALUES
(1, 'Mario', 'Rossi'),
(2, 'Lucia', 'Bianchi'),
(3, 'Alessandro', 'Verdi');

INSERT OR IGNORE INTO Libri (Id, Titolo, Autore_id, Anno, Genere) VALUES
(1, 'Il mistero del castello', 1, 2020, 'Giallo'),
(2, 'Viaggio nel tempo', 1, 2018, 'Fantascienza'),
(3, 'La cucina italiana', 2, 2019, 'Cucina'),
(4, 'Storia antica', 3, 2021, 'Storia'),
(5, 'Romanzo moderno', 3, 2022, 'Narrativa'),
(6, 'Il ritorno del castello', 1, 2023, 'Giallo');

INSERT OR IGNORE INTO Prestiti (Id, Libro_id, Utente, Data_prestito, Data_restituzione) VALUES
(1, 1, 'Mario Rossi', '2023-01-01', '2023-01-15'),
(2, 2, 'Lucia Bianchi', '2023-02-01', NULL),
(3, 3, 'Alessandro Verdi', '2023-03-01', '2023-03-10'),
(4, 4, 'Mario Rossi', '2023-04-01', NULL);

SELECT Libri.Titolo, Libri.Anno, Libri.Genere
FROM Libri
JOIN Autori ON Libri.Autore_id = Autori.Id
WHERE Autori.Nome = 'Mario' AND Autori.Cognome = 'Rossi';

SELECT Libri.Titolo, Prestiti.Data_prestito, Prestiti.Data_restituzione
FROM Prestiti
JOIN Libri ON Prestiti.Libro_id = Libri.Id
WHERE Prestiti.Utente = 'Lucia Bianchi';

SELECT Genere, COUNT(*) AS NumeroLibri
FROM Libri
GROUP BY Genere
HAVING COUNT(*) > 1;

SELECT Autori.Nome || ' ' || Autori.Cognome AS Autore, COUNT(Libri.Id) AS NumeroLibri
FROM Autori
JOIN Libri ON Autori.Id = Libri.Autore_id
GROUP BY Autori.Id
ORDER BY NumeroLibri DESC;

SELECT Libri.Titolo, Prestiti.Utente, Prestiti.Data_prestito
FROM Prestiti
JOIN Libri ON Prestiti.Libro_id = Libri.Id
WHERE Prestiti.Data_restituzione IS NULL;