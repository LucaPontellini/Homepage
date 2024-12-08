# HTML (HyperText Markup Language)

## Introduzione a HTML
- **Definizione**: Linguaggio di markup utilizzato per la creazione e la strutturazione delle pagine web.
- **Elemento HTML**: Componente fondamentale di una pagina web, definito da tag.

## Struttura di Base di un Documento HTML
- **`<!DOCTYPE html>`**: Dichiarazione del tipo di documento HTML.
- **`<html>`**: Elemento radice che racchiude tutto il documento HTML.
    - **`<head>`**: Contiene metadati, collegamenti a fogli di stile e script.
        - **`<title>`**: Definisce il titolo della pagina visualizzato nella barra del browser.
        - **`<meta>`**: Fornisce metadati sulla pagina (es. descrizione, parole chiave).
        - **`<link>`**: Collega il documento a fogli di stile esterni.
        - **`<style>`**: Contiene stili CSS per la formattazione della pagina.
        - **`<script>`**: Collega script JavaScript o definisce script inline.
    - **`<body>`**: Contiene il contenuto visibile della pagina.
        - **Elementi HTML**: Tutti gli elementi che costituiscono la struttura della pagina.

## Elementi HTML di Base
- **`<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>`, `<h6>`**: Intestazioni di diversi livelli.
- **`<p>`**: Paragrafo di testo.
- **`<a>`**: Collegamento ipertestuale (link).
    - **Attributo `href`**: URL di destinazione del link.
- **`<img>`**: Immagine.
    - **Attributo `src`**: URL dell'immagine.
    - **Attributo `alt`**: Testo alternativo per l'immagine.
- **`<ul>`, `<ol>`, `<li>`**: Liste non ordinate (puntate) e ordinate (numeriche/item).
- **`<table>`, `<tr>`, `<td>`**: Tabelle, righe e celle.
- **`<div>`**: Contenitore generico per organizzare il layout.
- **`<span>`**: Elemento per applicare stili o manipolare parti di testo.
- **`<form>`**: Formulario per la raccolta di input utente.
    - **Elementi di input**: `<input>`, `<select>`, `<textarea>`, `<button>`, etc.

## Attributi HTML Comuni
- **`id`**: Identificatore univoco per un elemento.
- **`class`**: Classe CSS per applicare stili agli elementi.
- **`style`**: Stili CSS inline per un elemento specifico.
- **`src`**: Percorso dell'immagine o risorsa esterna.
- **`href`**: URL di destinazione per i collegamenti.
- **`alt`**: Testo alternativo per immagini.

## Formattazione e Struttura
- **Tag di Blocco**: Definiscono blocchi di contenuto (es. `<div>`, `<p>`, `<h1>`).
- **Tag Inline**: Incorporati nel testo senza interromperne il flusso (es. `<a>`, `<strong>`, `<em>`).
- **Commenti HTML**: `<!-- Commento -->` per annotazioni nel codice.

## Altri Concetti Avanzati
- **HTML Semantico**: Utilizzo di tag specifici per descrivere correttamente la struttura del contenuto (es. `<header>`, `<nav>`, `<section>`, `<article>`, `<footer>`).
- **Multimedia**: Incorporazione di audio (`<audio>`) e video (`<video>`) nelle pagine web.
- **Formulare e Input**: Utilizzo di elementi di input per la raccolta di dati dagli utenti.
- **Stili CSS**: Collegamento a fogli di stile esterni o definizione di stili inline.
- **Script JavaScript**: Utilizzo di script per aggiungere interattività e dinamicità alle pagine web.
- **Responsive Design**: Creazione di pagine web che si adattano a diversi dispositivi e dimensioni dello schermo.

## Best Practices e Strumenti
- **Validazione HTML**: Utilizzo di strumenti online per verificare la correttezza del codice HTML.
- **Debugger e Console**: Utilizzo degli strumenti di sviluppo del browser per il debugging.
- **Linters e Editor di Codice**: Utilizzo di linters HTML e editor di codice per garantire la correttezza e la coerenza del codice.

## Moduli Avanzati e Frameworks
- **Bootstrap**: Framework CSS per lo sviluppo di interfacce web responsive.
- **jQuery**: Libreria JavaScript per semplificare la manipolazione del DOM e le interazioni utente.
- **Vue.js**, **React**, **Angular**: Frameworks JavaScript per lo sviluppo di interfacce utente dinamiche e reattive.