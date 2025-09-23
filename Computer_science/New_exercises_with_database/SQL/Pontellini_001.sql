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
-- Seleziona tutte le produzioni per l'apiario con codice = 'A001'.
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

CREATE TABLE Beekeeper (
    Id_apicoltore INT PRIMARY KEY,
    Nome VARCHAR(50)
    );

CREATE TABLE Tipology (
    Id_tipologia INT PRIMARY KEY,
    Nome_tipologia VARCHAR(50),
    Descrizione VARCHAR(255)
    );

CREATE TABLE Honey (
    Id_miele INT PRIMARY KEY,
    Denominazione VARCHAR(50),
    Id_tipologia INT FOREIGN KEY REFERENCES Tipology(Id_tipologia)
    );

CREATE TABLE Apiary (
    Codice_apiario VARCHAR(10) PRIMARY KEY,
    Numero_arnie INT,
    Localita VARCHAR(50),
    Comune VARCHAR(50),
    Provincia VARCHAR(50),
    Regione VARCHAR(50),
    Id_apicoltore INT FOREIGN KEY REFERENCES Beekeeper(Id_apicoltore)
    );

CREATE TABLE Production (
    Id_produzione INT PRIMARY KEY,
    Anno INT,
    Quantita_annua FLOAT,
    Codice_apiario VARCHAR(10) FOREIGN KEY REFERENCES Apiary(Codice_apiario),
    Id_miele INT FOREIGN KEY REFERENCES Honey(Id_miele)
    );
    
INSERT INTO Beekeeper (Nome, Id_apicoltore) VALUES ('Mario', 1);
INSERT INTO Tipology (Id_tipologia, Nome_tipologia, Descrizione) VALUES (1, 'Millefiori', 'Miele di vari fiori');
INSERT INTO Honey (Id_miele, Denominazione, Id_tipologia) VALUES (1, 'Miele di Primavera', 1);
INSERT INTO Apiary (Codice_apiario, Numero_arnie, Localita, Comune, Provincia, Regione, Id_apicoltore) VALUES ('A001', 10, 'Collina', 'Torino', 'TO', 'Piemonte', 1);
INSERT INTO Production (Id_produzione, Anno, Quantita_annua, Codice_apiario, Id_miele) VALUES (1, 2023, 150.5, 'A001', 1);