-- database: /path/to/database.db
-- 1. Creare le tabelle del modello ER
-- 2. Inserire dati nelle tabelle con le istruzioni di INSERT (2-3 righe per tabella)
-- 3. Fare le seguenti query:
-- Seleziona tutti gli apicoltori.
-- Seleziona il nome dell'apicoltore con id = 1.
-- Seleziona tutti gli apiari nella regione 'Lombardia'.
-- Seleziona codice e numero_arnie degli apiari con più di 10 arnie.
-- Seleziona codice e località degli apiari posseduti dall'apicoltore con id = 2.
-- Seleziona tutti i mieli appartenenti alla tipologia con id = 3.
-- Seleziona la denominazione del miele con id = 5.
-- Seleziona tutte le produzioni dell'anno 2024.
-- Seleziona tutte le produzioni per l'apiario con codice = '102'.
-- Seleziona le produzioni per il miele con id = 3 nell'anno 2023.

-- erDiagram
--     BEEKEEPER {
--         int id PK "id_apicoltore"
--         string name "nome"
--     }
 
--     TYPOLOGY {
--         int id PK
--         string name "nome_tipologia"
--         string description
--     }

--     HONEY {
--         int id PK
--         string denomination "denominazione"
--         int typology_id FK
--     }

--     APIARY {
--         string code PK "codice_apiario"
--         int num_hives "numero_arnie"
--         string locality "località"
--         string comune
--         string province
--         string region
--         int beekeeper_id FK
--     }

--     PRODUCTION {
--         int id PK
--         int year "anno"
--         float quantity "quantita_annua"
--         int apiary_code FK
--         int honey_id FK
--     }

--     %% Relationships
--     BEEKEEPER ||--o{ APIARY : "possiede"
--     TYPOLOGY ||--o{ HONEY : "classifica"
--     HONEY ||--o{ PRODUCTION : "è_prodotto_in"
--     APIARY ||--o{ PRODUCTION : "registra"

-- -- Typology
-- INSERT INTO Typology (id, typology_name, typology_description) VALUES
-- (1, 'Monofloral', 'Miele prodotto prevalentemente da un unico fiore'),
-- (2, 'Polyfloral', 'Miele di millefiori, raccolto da più specie floreali'),
-- (3, 'Honeydew', 'Miele prodotto a partire dal melato (secrezioni di insetti)');

-- -- Beekeeper
-- INSERT INTO Beekeeper (id, beekeeper_name) VALUES
-- (1, 'Marco Rossi'),
-- (2, 'Lucia Bianchi'),
-- (3, 'Alessandro Verdi');

-- -- Honey
-- INSERT INTO Honey (id, denomination, typology_id) VALUES
-- (1, 'Acacia', 1),
-- (2, 'Castagno', 1),
-- (3, 'Millefiori', 2),
-- (4, 'Eucalipto', 2),
-- (5, 'Melata di Bosco', 3);

-- -- Apiary
-- INSERT INTO Apiary (code, num_hives, locality, comune, province, region, beekeeper_id) VALUES
-- (100, 12, 'Fattoria Le Rose', 'San Pietro', 'Pisa', 'Toscana', 1),
-- (101, 8, 'Colle Verde', 'Montevarchi', 'Arezzo', 'Toscana', 2),
-- (102, 20, 'Bosco Alto', 'Vercelli', 'Vercelli', 'Piemonte', 3),
-- (103, 5, 'Terrazza Sud', 'Verona', 'Verona', 'Veneto', 1);

-- -- Production
-- INSERT INTO Production (id, year, quantity, apiary_code, honey_id) VALUES
-- (1, 2022, 120.5, 100, 1),
-- (2, 2022, 95.2, 101, 3),
-- (3, 2023, 210.0, 102, 5),
-- (4, 2023, 34.7, 103, 2),
-- (5, 2024, 150.0, 100, 3),
-- (6, 2024, 78.3, 101, 4);

-- CREATE TABLE Typology (
--     id INT PRIMARY KEY,
--     typology_name VARCHAR(50) NOT NULL,
--     typology_description VARCHAR(300),
-- );

-- CREATE TABLE Honey (
--     id INT PRIMARY KEY,
--     denomination VARCHAR(50) NOT NULL,
--     typology_id INT,
--     FOREIGN KEY (typology_id) REFERENCES Typology(id)
-- );

-- CREATE TABLE Beekeeper (
--     id INT PRIMARY KEY,
--     beekeeper_name VARCHAR(50) NOT NULL,
-- );

-- CREATE TABLE Apiary (
--     code INT PRIMARY KEY,
--     num_hives INT NOT NULL,
--     locality VARCHAR(300) NOT NULL,
--     comune VARCHAR(300) NOT NULL,
--     province VARCHAR(300) NOT NULL,
--     region VARCHAR(300) NOT NULL,
--     beekeeper_id INT,
--     FOREIGN KEY (beekeeper_id) REFERENCES Beekeeper(id)
-- );

-- CREATE TABLE Production (
--     id INT PRIMARY KEY,
--     year INT,
--     quantity FLOAT,
--     apiary_code INT,
--     honey_id INT,
--     FOREIGN KEY (apiary_code) REFERENCES Apiary(code),
--     FOREIGN KEY (honey_id) REFERENCES Honey(id)
-- );

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

SELECT * FROM Beekeeper;
SELECT Nome FROM Beekeeper WHERE Id_apicoltore = 1;
SELECT * FROM Apiary WHERE Regione = 'Lombardia';
SELECT Codice_apiario, Numero_arnie FROM Apiary WHERE Numero_arnie > 10;
SELECT Codice_apiario, Localita FROM Apiary WHERE Id_apicoltore = 2;
SELECT * FROM Honey WHERE Id_tipologia = 3;
SELECT Denominazione FROM Honey WHERE Id_miele = 5;
SELECT * FROM Production WHERE Anno = 2024;
SELECT * FROM Production WHERE Codice_apiario = '102';
SELECT * FROM Production WHERE Id_miele = 3 AND Anno = 2023;