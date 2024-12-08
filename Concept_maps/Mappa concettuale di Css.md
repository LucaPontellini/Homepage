# CSS (Cascading Style Sheets)

## Introduzione a CSS
- **Definizione**: Linguaggio di stile utilizzato per definire l'aspetto e la presentazione delle pagine web.
- **Separazione dei Contenuti**: Separazione tra struttura HTML e stili CSS per migliorare la manutenibilità e la flessibilità.

## Selezione degli Elementi e Selettori
### Selezione degli Elementi
- **Selezione per Tipo**: Stile applicato a tutti gli elementi di un determinato tipo (es. `p`, `h1`, `div`).
- **Selezione per Classe**: Stile applicato agli elementi con una determinata classe (es. `.classe`).
- **Selezione per ID**: Stile applicato a un elemento specifico con un ID univoco (es. `#id`).
- **Selezione Gerarchica**: Stile applicato a elementi figlio di un altro elemento (es. `div p`).

### Selettori
- **Selettore di tipo**: Seleziona elementi in base al tipo di nodo.
- **Selettore di classe**: Seleziona elementi in base alla classe.
- **Selettore di ID**: Seleziona un elemento in base al suo ID.
- **Selettore universale**: Seleziona tutti gli elementi.
- **Selettore discendente**: Seleziona elementi che sono discendenti di un altro elemento.
- **Selettore figlio**: Seleziona elementi che sono figli diretti di un altro elemento.
- **Selettore di attributo**: Seleziona elementi in base a un attributo e al suo valore.
- **Pseudo-classi e pseudo-elementi**: Seleziona elementi in base a uno stato o a una parte specifica.

## Proprietà CSS Comuni e Proprietà
### Proprietà CSS Comuni
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

### Proprietà
- **Proprietà del testo**: `color`, `font-family`, `font-size`, `text-align`, ecc.
- **Proprietà del box model**: `margin`, `border`, `padding`, `width`, `height`, ecc.
- **Proprietà di posizionamento**: `position`, `top`, `right`, `bottom`, `left`, `z-index`, ecc.
- **Proprietà di visualizzazione**: `display`, `visibility`, `opacity`, ecc.
- **Proprietà di sfondo**: `background-color`, `background-image`, `background-repeat`, ecc.
- **Proprietà di lista**: `list-style-type`, `list-style-position`, ecc.
- **Proprietà di tabella**: `border-collapse`, `border-spacing`, ecc.

## Box Model e CSS Box Model
### Box Model
- **Content Box**: Contenuto dell'elemento (testo, immagini).
- **Padding**: Spazio tra il contenuto e il bordo.
- **Border**: Bordo dell'elemento.
- **Margin**: Spazio esterno attorno all'elemento.

### CSS Box Model
- **Contenuto**: L'area dove viene visualizzato il testo o le immagini.
- **Padding**: L'area attorno al contenuto.
- **Border**: L'area attorno al padding (e al contenuto).
- **Margin**: L'area attorno al bordo.

## Specificità dei Selettori e Specificità
### Specificità dei Selettori
- **Specificità**: Regole per risolvere conflitti tra stili applicati a un elemento.
- **Inline Styles**: Stili definiti direttamente sugli elementi HTML.
- **Internal Styles**: Stili definiti all'interno del tag `<style>` nell'HTML.
- **External Styles**: Stili definiti in file CSS esterni.

### Specificità
- **Calcolo della specificità dei selettori**.
- **Regole di cascata**: l'ultima regola definita prevale.
- **`!important`**: sovrascrive qualsiasi specificità.

## Regole
- **Sintassi di una regola CSS**: selettore, parentesi graffe, dichiarazioni.
- **Dichiarazione**: proprietà e valore separati da due punti.
- **Gruppo di selettori**: più selettori separati da virgole, condividono le stesse dichiarazioni.

## Posizionamento
### Posizionamento
- **Statico**: Il posizionamento predefinito.
- **Relativo**: Posizionato rispetto alla sua posizione normale.
- **Assoluto**: Posizionato rispetto al suo contenitore più vicino (non statico).
- **Fisso**: Posizionato rispetto alla finestra del browser.

## Valori
- **Valori numerici**: `0`, `14px`, `1.5em`, ecc.
- **Valori di colore**: `red`, `#ff0000`, `rgb(255, 0, 0)`, ecc.
- **Valori di stringa**: `"Times New Roman"`, `url(image.jpg)`, ecc.
- **Valori speciali**: `auto`, `inherit`, `none`, ecc.

## Unità
- **Assolute**: `px`, `pt`, `cm`, ecc.
- **Relative**: `em`, `%`, `vh`, `vw`, ecc.

## CSS3
### CSS3
- **Nuovi selettori**: `nth