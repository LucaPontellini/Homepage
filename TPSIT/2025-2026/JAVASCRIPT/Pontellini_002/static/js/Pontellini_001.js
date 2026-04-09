document.getElementById("formStudente").addEventListener("submit", function (e) {
    e.preventDefault(); // blocca il comportamento di default della form

    // Reset degli errori
    let inputs = document.querySelectorAll("input, select");
    inputs.forEach(i => i.classList.remove("error"));

    let errorDiv = document.getElementById("errori");
    errorDiv.innerHTML = "";
    errorDiv.style.display = "none";

    let errori = [];

    // Recupero dei valori
    let nome = document.getElementById("nome");
    let cognome = document.getElementById("cognome");
    let data = document.getElementById("dataNascita");
    let cf = document.getElementById("codiceFiscale");
    let classe = document.getElementById("classe");
    let sezione = document.getElementById("sezione");
    let ripetente = document.getElementById("ripetente");
    let anniRipetuti = document.getElementById("anniRipetuti");
    let uscita = document.getElementById("uscita");

    // Validazioni
    if (nome.value.trim() === "") {
        errori.push("Nome obbligatorio");
        nome.classList.add("error");
    }

    if (cognome.value.trim() === "") {
        errori.push("Cognome obbligatorio");
        cognome.classList.add("error");
    }

    if (data.value === "") {
        errori.push("Data di nascita obbligatoria");
        data.classList.add("error");
    }

    if (cf.value.length !== 16) {
        errori.push("Codice fiscale deve avere 16 caratteri");
        cf.classList.add("error");
    }

    if (classe.value === "") {
        errori.push("Selezionare una classe");
        classe.classList.add("error");
    }

    if (sezione.value === "") {
        errori.push("Selezionare una sezione");
        sezione.classList.add("error");
    }

    if (uscita.value === "") {
        errori.push("Selezionare uscita");
        uscita.classList.add("error");
    }

    // Logica del ripetente
    if (ripetente.checked) {
        if (anniRipetuti.value === "" || anniRipetuti.value < 1) {
            errori.push("Inserire anni ripetuti (>=1)");
            anniRipetuti.classList.add("error");
        }
    }

    // Mostra gli errori se sono presenti
    if (errori.length > 0) {
        errorDiv.innerHTML = errori.join("<br>");
        errorDiv.style.color = "red";
        errorDiv.style.display = "block";
        return; // blocca il submit
    }

    // Creazione del JSON
    let dati = {
        nome: nome.value.trim(),
        cognome: cognome.value.trim(),
        dataNascita: data.value,
        codiceFiscale: cf.value.trim(),
        classe: classe.value,
        sezione: sezione.value,
        ripetente: ripetente.checked,
        anniRipetuti: ripetente.checked ? parseInt(anniRipetuti.value) : 0,
        uscita: uscita.value
    };

    // Salvataggio su localStorage per la pagina dei dati dello studente
    localStorage.setItem("studente", JSON.stringify(dati));

    // Redirect alla pagina dei dati
    window.location.href = "Pontellini_001_b.html";
});