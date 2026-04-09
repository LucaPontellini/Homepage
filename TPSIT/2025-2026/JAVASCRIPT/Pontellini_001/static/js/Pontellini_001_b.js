// Variabile che conterrà la biblioteca caricata
let biblioteca = null;

// Caricamento del file JSON
document.getElementById("fileJSON").addEventListener("change", e => {

    const file = e.target.files[0];
    const reader = new FileReader();

    reader.onload = () => {
        biblioteca = JSON.parse(reader.result);
        aggiornaTabella();
    };

    reader.readAsText(file);
});

// Aggiorna la tabella HTML
function aggiornaTabella() {
    const tbody = document.querySelector("#tabellaLibri tbody");
    tbody.innerHTML = "";

    // Se non ci sono libri → messaggio
    if (!biblioteca || biblioteca.libri.length === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="5" style="text-align:center; padding:20px;">
                    Nessun libro presente nella biblioteca
                </td>
            </tr>
        `;
        return;
    }

    // Altrimenti mostra i libri
    biblioteca.libri.forEach(l => {
        tbody.innerHTML += `
            <tr>
                <td>${l.categoria}</td>
                <td>${l.numero}</td>
                <td>${l.titolo}</td>
                <td>${l.autore}</td>
                <td>${l.edizione}</td>
            </tr>
        `;
    });
}