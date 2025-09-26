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