# CSS (Cascading Style Sheets)

## Introduzione a CSS
- **Definizione**: Linguaggio di stile utilizzato per definire l'aspetto e la presentazione delle pagine web.
- **Separazione dei Contenuti**: Separazione tra struttura HTML e stili CSS per migliorare la manutenibilità e la flessibilità.

## Selezione degli Elementi
- **Selezione per Tipo**: Stile applicato a tutti gli elementi di un determinato tipo (es. `p`, `h1`, `div`).
- **Selezione per Classe**: Stile applicato agli elementi con una determinata classe (es. `.classe`).
- **Selezione per ID**: Stile applicato a un elemento specifico con un ID univoco (es. `#id`).
- **Selezione Gerarchica**: Stile applicato a elementi figlio di un altro elemento (es. `div p`).

## Proprietà CSS Comuni
- **Colore e Sfondo**:
    - `color`: Colore del testo.
    - `background-color`: Colore di sfondo.
- **Dimensioni e Spaziatura**:
    - `width`, `height`: Dimensioni dell'elemento.
    - `margin`, `padding`: Spaziatura esterna e interna.
- **Testo**:
    - `font-family`: Famiglia di caratteri.
    - `font-size`: Dimensione del carattere.
    - `font-weight`: Spessore del carattere (grassetto).
    - `text-align`: Allineamento del testo.
- **Visualizzazione**:
    - `display`: Tipo di visualizzazione dell'elemento (blocco, inline, flex, etc.).
    - `visibility`: Visibilità dell'elemento.
    - `opacity`: Opacità dell'elemento.
- **Bordi e Cornici**:
    - `border`: Bordo dell'elemento.
    - `border-radius`: Angoli arrotondati.
- **Posizionamento**:
    - `position`: Tipo di posizionamento dell'elemento (static, relative, absolute, fixed).
    - `top`, `bottom`, `left`, `right`: Posizione rispetto ai bordi del contenitore.
- **Animazioni e Transizioni**:
    - `transition`: Definisce transizioni animate tra gli stati.
    - `animation`: Definisce animazioni personalizzate.

## Box Model
- **Content Box**: Contenuto dell'elemento (testo, immagini).
- **Padding**: Spazio tra il contenuto e il bordo.
- **Border**: Bordo dell'elemento.
- **Margin**: Spazio esterno attorno all'elemento.

## Selettore Universale e Pseudo-Classi
- `*`: Selettore universale per selezionare tutti gli elementi.
- `:hover`, `:focus`, `:active`: Pseudo-classi per lo stato dell'elemento.
- `:nth-child(n)`: Selettore per selezionare elementi in base alla loro posizione nell'albero DOM.

## Media Queries
- `@media`: Definisce stili specifici per diverse dimensioni di schermo (responsive design).

## Specificità dei Selettori
- **Specificità**: Regole per risolvere conflitti tra stili applicati a un elemento.
- **Inline Styles**: Stili definiti direttamente sugli elementi HTML.
- **Internal Styles**: Stili definiti all'interno del tag `<style>` nell'HTML.
- **External Styles**: Stili definiti in file CSS esterni.

## Layout CSS
- **Flexbox**: Layout flessibile basato su righe o colonne.
- **Grid**: Layout basato su griglie bidimensionali.
- **Floats**: Posizionamento di elementi rispetto al flusso di pagina.

## Frameworks CSS
- **Bootstrap**: Framework CSS per lo sviluppo di interfacce web responsive.
- **Tailwind CSS**: Utility-first framework CSS per progettare rapidamente.
- **Materialize**: Implementazione del design Material Design di Google.

## Strumenti e Risorse
- **Browser Developer Tools**: Strumenti integrati per l'ispezione e il debugging CSS.
- **Preprocessori CSS**: Sass, Less per estendere le funzionalità di CSS.
- **CSS Libraries**: Librerie e risorse per stili predefiniti (es. Font Awesome).

## Best Practices
- **Organizzazione del Codice**: Utilizzo di una struttura modulare per mantenere il CSS ordinato.
- **Ottimizzazione delle Immagini**: Compressione delle immagini per migliorare le prestazioni del sito.
- **Compatibilità del Browser**: Test su diversi browser per garantire la compatibilità.