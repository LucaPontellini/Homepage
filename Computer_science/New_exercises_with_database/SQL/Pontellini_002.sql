-- database: db.sqlite
-- Query con GROUP BY e funzioni aggregate:

-- Seleziona la quantità totale prodotta per anno.
-- Seleziona la produzione media per apiario.
-- Seleziona il numero di produzioni e la produzione totale per miele.
-- Seleziona la produzione totale per miele nell'anno 2024.
-- Seleziona il valore massimo e minimo di produzione per anno.
-- Seleziona gli apiari la cui produzione totale supera 200.
-- Seleziona la produzione totale per tipologia di miele (typology_id).
-- Seleziona il numero di mieli per ciascuna tipologia.
-- Seleziona la produzione totale per apicoltore (beekeeper_id).
-- Seleziona la produzione media per arnia (produzione totale divisa per num_hives) per apiario.
-- Seleziona per ogni anno il conteggio delle produzioni con quantità maggiore di 100.
-- Seleziona per ogni miele e anno la somma delle quantità.

CREATE TABLE Beekeeper (
    Id_apicoltore INT PRIMARY KEY,
    Nome VARCHAR(50)
);

CREATE TABLE Typology (
    Id_tipologia INT PRIMARY KEY,
    Nome_tipologia VARCHAR(50),
    Descrizione VARCHAR(255)
);

CREATE TABLE Honey (
    Id_miele INT PRIMARY KEY,
    Denominazione VARCHAR(50),
    Id_tipologia INT REFERENCES Typology(Id_tipologia)
);

CREATE TABLE Apiary (
    Codice_apiario VARCHAR(10) PRIMARY KEY,
    Numero_arnie INT,
    Localita VARCHAR(50),
    Comune VARCHAR(50),
    Provincia VARCHAR(50),
    Regione VARCHAR(50),
    Id_apicoltore INT REFERENCES Beekeeper(Id_apicoltore)
);

CREATE TABLE Production (
    Id_produzione INT PRIMARY KEY,
    Anno INT,
    Quantita_annua FLOAT,
    Codice_apiario VARCHAR(10) REFERENCES Apiary(Codice_apiario),
    Id_miele INT REFERENCES Honey(Id_miele)
);
    
-- Typology
INSERT INTO Typology (Id_tipologia, Nome_tipologia, Descrizione) VALUES
(1, 'Monofloral', 'Miele prodotto prevalentemente da un unico fiore'),
(2, 'Polyfloral', 'Miele di millefiori, raccolto da più specie floreali'),
(3, 'Honeydew', 'Miele prodotto a partire dal melato (secrezioni di insetti)');

-- Beekeeper
INSERT INTO Beekeeper (Id_apicoltore, Nome) VALUES
(1, 'Marco Rossi'),
(2, 'Lucia Bianchi'),
(3, 'Alessandro Verdi');

-- Honey
INSERT INTO Honey (Id_miele, Denominazione, Id_tipologia) VALUES
(1, 'Acacia', 1),
(2, 'Castagno', 1),
(3, 'Millefiori', 2),
(4, 'Eucalipto', 2),
(5, 'Melata di Bosco', 3);

-- Apiary
INSERT INTO Apiary (Codice_apiario, Numero_arnie, Localita, Comune, Provincia, Regione, Id_apicoltore) VALUES
('100', 12, 'Fattoria Le Rose', 'San Pietro', 'Pisa', 'Toscana', 1),
('101', 8, 'Colle Verde', 'Montevarchi', 'Arezzo', 'Toscana', 2),
('102', 20, 'Bosco Alto', 'Vercelli', 'Vercelli', 'Piemonte', 3),
('103', 5, 'Terrazza Sud', 'Verona', 'Verona', 'Veneto', 1);

-- Production
INSERT INTO Production (Id_produzione, Anno, Quantita_annua, Codice_apiario, Id_miele) VALUES
(1, 2022, 120.5, '100', 1),
(2, 2022, 95.2, '101', 3),
(3, 2023, 210.0, '102', 5),
(4, 2023, 34.7, '103', 2),
(5, 2024, 150.0, '100', 3),
(6, 2024, 78.3, '101', 4);

SELECT Anno, SUM(Quantita_annua) AS Quantita_totale
FROM Production
GROUP BY Anno;

SELECT Codice_apiario, AVG(Quantita_annua) AS Media_apiario
FROM Production
GROUP BY Codice_apiario;

SELECT Id_miele, COUNT(*) AS Numero_produzioni, SUM(Quantita_annua) AS Quantita_totale
FROM Production
GROUP BY Id_miele;

SELECT Id_miele, SUM(Quantita_annua) AS Quantita_totale_2024
FROM Production
WHERE Anno = 2024
GROUP BY Id_miele;

SELECT Anno, MAX(Quantita_annua) AS Max_produzione, MIN(Quantita_annua) AS Min_produzione
FROM Production
GROUP BY Anno;

SELECT Codice_apiario, SUM(Quantita_annua) AS Totale_apiario
FROM Production
GROUP BY Codice_apiario
HAVING SUM(Quantita_annua) > 200;

SELECT Id_tipologia, SUM(Quantita_annua) AS Totale_per_tipologia
FROM Production
JOIN Honey ON Production.Id_miele = Honey.Id_miele
GROUP BY Id_tipologia;

SELECT Id_tipologia, COUNT(*) AS Numero_mieli
FROM Honey
GROUP BY Id_tipologia;

SELECT Id_apicoltore, SUM(Quantita_annua) AS Totale_per_apicoltore
FROM Production
JOIN Apiary ON Production.Codice_apiario = Apiary.Codice_apiario
GROUP BY Id_apicoltore;

SELECT Apiary.Codice_apiario, SUM(Quantita_annua) / Numero_arnie AS Media_per_arnia
FROM Production
JOIN Apiary ON Production.Codice_apiario = Apiary.Codice_apiario
GROUP BY Apiary.Codice_apiario;

SELECT Anno, COUNT(*) AS Produzioni_sopra_100
FROM Production
WHERE Quantita_annua > 100
GROUP BY Anno;

SELECT Id_miele, Anno, SUM(Quantita_annua) AS Quantita_totale
FROM Production
GROUP BY Id_miele, Anno;