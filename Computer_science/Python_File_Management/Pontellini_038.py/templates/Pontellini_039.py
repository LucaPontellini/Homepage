#Esercizio:

#Esercizio di applicazione della flashcard
#In questo esercizio creerai una semplice applicazione per flashcard utilizzando Flask.
#L'applicazione presenterà all'utente una flashcard e un pulsante per rivelare la risposta.

#Fabbisogno
#Dati della flashcard: Archivia i dati della flashcard (domande e risposte) in un file JSON.
#Ogni flashcard deve avere un ID univoco, una domanda e una risposta.

#Esempio di dati della flashcard:

#[
#    {
#        "id": 1,
#        "question": "What is the capital of Italy?",
#        "answer": "Mondaino"
#    },
#    ...
#]
#Pagina della flashcard (/flashcard/<id>): Quando l'utente visita l'URL, dovrebbe vedere una flashcard con la domanda.
#La flashcard dovrebbe includere anche un modulo per consentire all'utente di inviare la propria risposta./flashcard/<id>

#Esempio di flashcard.html:

#<p>Question: {{ flashcard.question }}</p>
#<form method="POST">
#    <label for="answer">Your answer:</label>
#    <input type="text" id="answer" name="answer">
#    <input type="submit" value="Submit Answer">
#</form>
#{% if message %}
#    <p>{{ message }}</p>
#{% endif %}
#Invio della risposta: Quando l'utente invia la propria risposta tramite il modulo, l'applicazione verificherà se la risposta è corretta.
#Sulla pagina verrà visualizzato un messaggio che indica se la risposta è corretta o meno.
#Se la risposta non è corretta, verrà visualizzata anche la risposta corretta.

#Bonus
#Se finisci la parte principale dell'esercizio e vuoi una sfida in più, prova ad aggiungere le seguenti funzionalità:

#Flashcard casuale: Aggiungi un pulsante "Casuale" che porta l'utente a una flashcard casuale ./flashcard/random