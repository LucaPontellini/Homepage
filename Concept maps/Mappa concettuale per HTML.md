# Mappa Concettuale HTML

## Struttura di base di un documento HTML
- `<!DOCTYPE html>`: Definisce il tipo di documento e la versione di HTML.
- `<html>`: L'elemento radice di una pagina web.
  - `<head>`: Contiene metadati sulla pagina, come il titolo e i link ai fogli di stile CSS.
    - `<title>`: Definisce il titolo del documento, che viene visualizzato nella barra del titolo del browser.
    - `<link>`: Utilizzato per collegare i fogli di stile CSS esterni.
    - `<meta>`: Fornisce metadati sulla pagina HTML, come la codifica dei caratteri e le parole chiave per i motori di ricerca.
    - `<style>`: Utilizzato per includere informazioni di stile CSS all'interno di un documento HTML.
  - `</head>`
  - `<body>`: Contiene il contenuto principale del documento web.
    - Elementi del corpo
  - `</body>`
- `</html>`

## Elementi del corpo HTML
- Testo
  - `<h1>` - `<h6>`: Rappresentano i titoli. `<h1>` è il titolo di livello più alto e `<h6>` è il titolo di livello più basso.
  - `<p>`: Definisce un paragrafo.
  - `<br>`: Inserisce un salto di riga.
  - `<hr>`: Crea una linea orizzontale.
- Formattazione del testo
  - `<strong>`: Rende il testo in grassetto.
  - `<em>`: Rende il testo in corsivo.
  - `<small>`: Rende il testo più piccolo.
  - `<sub>`: Crea testo in pedice.
  - `<sup>`: Crea testo in apice.
- Link
  - `<a>`: Definisce un hyperlink.
- Immagini
  - `<img>`: Utilizzato per incorporare immagini.
- Liste
  - `<ul>`: Crea una lista non ordinata.
  - `<ol>`: Crea una lista ordinata.
  - `<li>`: Definisce un elemento della lista.
- Tabelle
  - `<table>`: Crea una tabella.
  - `<tr>`: Definisce una riga della tabella.
  - `<th>`: Definisce un'intestazione della tabella.
  - `<td>`: Definisce una cella della tabella.
- Form
  - `<form>`: Crea un modulo HTML per l'input dell'utente.
  - `<input>`: Crea campi di input interattivi per l'input dell'utente.
  - `<button>`: Rappresenta un pulsante cliccabile.
- Elementi semantici
  - `<header>`: Rappresenta un contenitore per contenuti introduttivi o un insieme di link di navigazione.
  - `<footer>`: Rappresenta un piede di pagina per il contenuto più vicino all'elemento padre.
  - `<article>`: Rappresenta un contenuto autonomo all'interno di un documento.
  - `<section>`: Rappresenta una sezione autonoma di un documento.
  - `<aside>`: Rappresenta una sezione di una pagina che consiste in contenuto che è tangenziale al contenuto attorno all'elemento aside, e che può essere considerato separato dal contenuto attorno ad esso.
  - `<nav>`: Rappresenta una sezione di una pagina che contiene link di navigazione.

# Colori
- *Rosso* : #FF0000 - Usato per indicare l'importanza o l'attenzione.
- *Verde* : #008000 - Spesso associato a successo o conferma.
- *Blu* : #0000FF - Usato per indicare fiducia e stabilità.
- *Giallo* : #FFFF00 - Può indicare cautela o attenzione.
- *Nero* : #000000 - Usato per il testo o per indicare l'eleganza.
- *Bianco* : #FFFFFF - Usato per lo sfondo o per indicare la purezza.
- *Arancione* : #FFA500 - Spesso usato per indicare creatività o gioia.
- *Viola* : #800080 - Può indicare lusso o ambizione.
- *Marrone* : #A52A2A - Spesso usato per indicare la terra o la natura.
- *Grigio* : #808080 - Usato per indicare la neutralità o il compromesso.
- *Rosa* : #FFC0CB - Spesso associato alla femminilità o alla dolcezza.
- *Ciano* : #00FFFF - Può indicare freschezza o leggerezza.
- *Magenta* : #FF00FF - Spesso usato per indicare l'originalità o l'audacia.
- *Lime* : #00FF00 - Può indicare energia o vivacità.
- *Teal* : #008080 - Usato per indicare la sofisticatezza o la stabilità.
- *Navy* : #000080 - Può indicare la professionalità o la serietà.
- *Maroon* : #800000 - Spesso associato alla forza o al coraggio.
- *Olive* : #808000 - Può indicare la pace o la tranquillità.
- *Aqua* : #00FFFF - Spesso usato per indicare la pulizia o la freschezza.
- *Fuchsia* : #FF00FF - Può indicare l'entusiasmo o la passione.
- *Silver* : #C0C0C0 - Usato per indicare la modernità o l'innovazione.
- *Purple* : #800080 - Può indicare il lusso o la regalità.

# Stili di testo

## Maiuscolo
- *Descrizione*: Il testo viene trasformato in maiuscolo.
- *Esempio HTML*: <p style="text-transform: uppercase;">Testo in maiuscolo</p>

## Minuscolo
- *Descrizione*: Il testo viene trasformato in minuscolo.
- *Esempio HTML*: <p style="text-transform: lowercase;">Testo in minuscolo</p>

## Corsivo
- *Descrizione*: Il testo viene trasformato in corsivo.
- *Esempio HTML*: <p style="font-style: italic;">Testo in corsivo</p>

## Testo evidenziato
- *Descrizione*: Il testo viene evidenziato.
- *Esempio HTML*: <mark>Testo evidenziato</mark>

## Testo barrato
- *Descrizione*: Il testo viene barrato.
- *Esempio HTML*: <del>Testo barrato</del>

## Grandezze del testo
- *Descrizione*: Il testo può essere impostato con diverse grandezze.
- *Esempio HTML*:
  - Piccolo: <small>Testo piccolo</small>
  - Normale: <p>Testo normale</p>
  - Grande: <h1>Testo grande</h1>

## Caratteri

### Serif
- *Descrizione*: I caratteri Serif hanno piccoli tratti o linee decorative alla fine delle lettere. Sono spesso usati per il testo del corpo perché sono facili da leggere.
- *Esempi HTML*: Times New Roman, Georgia.

### Sans-serif
- *Descrizione*: I caratteri Sans-serif non hanno i tratti decorativi alla fine delle lettere. Sono spesso usati per i titoli e gli intestazioni.
- *Esempi HTML*: Arial, Helvetica.

### Monospace
- *Descrizione*: I caratteri Monospace hanno la stessa larghezza per ogni carattere. Sono spesso usati per il codice o il testo preformattato.
- *Esempi HTML*: Courier New, Lucida Console.

### Cursive
- *Descrizione*: I caratteri Cursive imitano la scrittura a mano. Sono spesso usati per gli elementi decorativi.
- *Esempi HTML*: Brush Script MT, Lucida Handwriting.

### Fantasy
- *Descrizione*: I caratteri Fantasy sono caratteri decorativi con un aspetto unico. Sono spesso usati per i titoli e gli elementi decorativi.
- *Esempi HTML*: Impact, Western.