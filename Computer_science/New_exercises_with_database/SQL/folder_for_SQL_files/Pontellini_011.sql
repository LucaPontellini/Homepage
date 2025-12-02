-- database: :memory:
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

-- 1. Elenco degli apicoltori che producono miele DOP in una determinata regione
SELECT B.Nome AS Apicoltore, A.Regione, H.Denominazione AS Miele, T.Nome_tipologia AS Tipologia
FROM Beekeeper B
JOIN Apiary A ON B.Id_apicoltore = A.Id_apicoltore
JOIN Production P ON A.Codice_apiario = P.Codice_apiario
JOIN Honey H ON P.Id_miele = H.Id_miele
JOIN Typology T ON H.Id_tipologia = T.Id_tipologia
WHERE A.Regione = 'Toscana';

-- 2. Numero complessivo di apiari per ciascuna regione
SELECT Regione, COUNT(*) AS Numero_apiari
FROM Apiary
GROUP BY Regione;

-- 3. Quantità di miele prodotto in Italia lo scorso anno per ciascuna tipologia
SELECT T.Nome_tipologia, SUM(P.Quantita_annua) AS Totale_prodotto
FROM Production P
JOIN Honey H ON P.Id_miele = H.Id_miele
JOIN Typology T ON H.Id_tipologia = T.Id_tipologia
WHERE P.Anno = 2024
GROUP BY T.Nome_tipologia;