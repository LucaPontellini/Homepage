// Oggetto principale della biblioteca
let biblioteca = { libri: [] };

// Caricamento di un file JSON
document.getElementById("fileJSON").addEventListener("change", e => {

    const file = e.target.files[0];
    const reader = new FileReader();

    reader.onload = () => {
        biblioteca = JSON.parse(reader.result); // Converte il JSON in oggetto JS
        aggiornaTabella(); // Aggiorna la tabella
    };

    reader.readAsText(file);
});

// Aggiunta del libro dalla FORM
document.getElementById("formLibro").addEventListener("submit", e => {
    e.preventDefault(); // Evita il refresh

    // Crea l’oggetto libro
    const libro = {
        categoria: categoria.value,
        numero: numero.value,
        titolo: titolo.value,
        autore: autore.value,
        edizione: edizione.value
    };

    // Aggiunge il libro alla collezione
    biblioteca.libri.push(libro);

    // Aggiorna la tabella
    aggiornaTabella();

    // Reset del form
    e.target.reset();
});

// Aggiorna la tabella HTML
function aggiornaTabella() {
    const tbody = document.querySelector("#tabellaLibri tbody");

    tbody.innerHTML = biblioteca.libri.map(l => `
        <tr>
            <td>${l.categoria}</td>
            <td>${l.numero}</td>
            <td>${l.titolo}</td>
            <td>${l.autore}</td>
            <td>${l.edizione}</td>
        </tr>
    `).join("");
}

// Scaricamento del JSON
document.getElementById("scaricaJSON").addEventListener("click", () => {

    const dati = JSON.stringify(biblioteca, null, 2);
    const blob = new Blob([dati], { type: "application/json" });
    const url = URL.createObjectURL(blob);

    const link = document.createElement("a");
    link.href = url;
    link.download = "biblioteca.json";
    link.click();

    URL.revokeObjectURL(url);
});

// Seleziona tutti gli input della form (compreso il file)
const elementiForm = document.querySelectorAll("#formLibro input");

// Bordo rosso chiaro al click
elementiForm.forEach(el => {
    el.addEventListener("click", () => {
        el.style.borderColor = "#ff9999"; // rosso chiaro
    });

    // Bordo rosso scuro quando ha il focus
    el.addEventListener("focus", () => {
        el.style.borderColor = "#cc0000"; // rosso scuro
    });

    // Ripristino quando perde il focus
    el.addEventListener("blur", () => {
        el.style.borderColor = "";
    });
});