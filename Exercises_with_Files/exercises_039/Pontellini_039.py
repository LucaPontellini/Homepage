#Esercizio:

#Esercizio: di applicazione della flashcard
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
#Sulla pagina verrà visualizzato un messaggio che indica se la risposta è corretta o meno. Se la risposta non è corretta, verrà visualizzata anche la risposta corretta.

#Bonus
#Se finisci la parte principale dell'esercizio e vuoi una sfida in più, prova ad aggiungere le seguenti funzionalità:

#Flashcard casuale: Aggiungi un pulsante "Casuale" che porta l'utente a una flashcard casuale ./flashcard/random

from flask import Flask, render_template, request, redirect, url_for
import json
import random

app = Flask(__name__)

with open('/home/pontellini/Homepage/Exercises_with_Files/exercises_039/flashcards.json', 'r') as f:
    flashcards = json.load(f)

@app.route('/flashcard/<int:id>', methods=['GET', 'POST'])
def flashcard(id):
    flashcard = next((f for f in flashcards if f['id'] == id), None)
    if flashcard is None:
        return "Flashcard non trovata", 404

    message = None
    if request.method == 'POST':
        answer = request.form.get('answer')
        if answer == flashcard['answer']:
            message = "Corretto!"
        else:
            message = f"Sbagliato! La risposta corretta era: {flashcard['answer']}"

    return render_template('/home/pontellini/Homepage/Exercises_with_Files/exercises_039/flashcard.html', flashcard=flashcard, message=message)

@app.route('/flashcard/random')
def random_flashcard():
    flashcard = random.choice(flashcards)
    return redirect(url_for('flashcard', id=flashcard['id']))

if __name__ == '__main__':
    app.run(debug=True, port=12345)