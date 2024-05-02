#Esercizio di applicazione della flashcard
#In questo esercizio creerai una semplice applicazione per flashcard utilizzando Flask. L'applicazione presenterà all'utente una flashcard e un pulsante per rivelare la risposta.
#
#Fabbisogno
#Dati della flashcard: Archivia i dati della flashcard (domande e risposte) in un file JSON. Ogni flashcard deve avere un ID univoco, una domanda e una risposta.
#
#Esempio di dati della flashcard:
#
#[
#    {
#        "id": 1,
#        "question": "What is the capital of Italy?",
#        "answer": "Mondaino"
#    },
#    ...
#]
#Pagina della flashcard (/flashcard/<id>): Quando l'utente visita l'URL, dovrebbe vedere una flashcard con la domanda. La flashcard dovrebbe includere anche un modulo per consentire all'utente di inviare la propria risposta./flashcard/<id>
#
#Esempio di flashcard.html:
#
#<p>Question: {{ flashcard.question }}</p>
#<form method="POST">
#    <label for="answer">Your answer:</label>
#    <input type="text" id="answer" name="answer">
#    <input type="submit" value="Submit Answer">
#</form>
#{% if message %}
#    <p>{{ message }}</p>
#{% endif %}
#Invio della risposta: Quando l'utente invia la propria risposta tramite il modulo, l'applicazione verificherà se la risposta è corretta. Sulla pagina verrà visualizzato un messaggio che indica se la risposta è corretta o meno. Se la risposta non è corretta, verrà visualizzata anche la risposta corretta.
#
#Bonus
#Se finisci la parte principale dell'esercizio e vuoi una sfida in più, prova ad aggiungere le seguenti funzionalità:
#
#Flashcard casuale: Aggiungi un pulsante "Casuale" che porta l'utente a una flashcard casuale ./flashcard/random
#Configurare l'ambiente
#Creare un nuovo repository:
#
#Apri il tuo terminale e vai alla directory in cui desideri creare il tuo nuovo repository o aprirne uno esistente.
#Creare un ambiente virtuale:
#
#Sempre nel terminale, eseguire per creare un nuovo ambiente virtuale in una directory denominata .python3 -m venv .venv.venv
#Attivare l'ambiente virtuale:
#
#In Linux, eseguire per attivare l'ambiente virtuale.source .venv/bin/activate
#Installare i moduli richiesti:
#
#Se si dispone di un file, eseguire per installare tutti i moduli richiesti.requirements.txtpip install -r requirements.txt
#Aggiungi un file .gitignore:
#
#Creare un nuovo file denominato nel repository..gitignore
#Aggiungi e qualsiasi altra directory o file che vuoi che Git ignori..venv
#Approccio dall'alto verso il basso
#Ricorda, questo è un approccio dall'alto verso il basso. Puoi iniziare a lavorare su ogni passaggio, testarlo a fondo prima di passare a quello successivo. In questo modo, è possibile assicurarsi che ogni parte dell'applicazione funzioni come previsto prima di aggiungere ulteriore complessità.
#
#Leggere e stampare i dati JSON (read_flashcards):
#
#Creare un file JSON con i dati della flashcard, come descritto nell'esercizio.
#Scrivere una funzione Python per leggere questo file JSON e stampare i dati.read_flashcards(filename: str) -> None:
#Accedere alle singole flashcard (get_flashcard_by_id):
#
#Modificare la funzione in modo che accetti un ID come parametro, rinominarla in .read_flashcardsget_flashcard_by_id(id: int) -> None:
#La funzione dovrebbe stampare la flashcard con l'ID specificato.get_flashcard_by_id
#Creare un'interfaccia CLI semplice (prompt_for_id):
#
#Scrivere una funzione per richiedere all'utente un ID.prompt_for_id() -> int:
#Chiamare la funzione dal passaggio 2 con l'input dell'utente.get_flashcard_by_id
#Stampa la domanda dalla flashcard.
#Consenti all'utente di rispondere a una domanda (prompt_for_answer e check_answer):
#
#Dopo aver stampato la domanda, richiedere all'utente una risposta utilizzando la funzione .prompt_for_answer() -> str:
#
#Scrivi una funzione per verificare se la risposta dell'utente corrisponde alla risposta nella flashcard.check_answer(user_answer: str, correct_answer: str) -> bool:
#
#Chiama con la risposta dell'utente e la risposta corretta dalla flashcard.check_answer
#
#Stampare un messaggio che indica se l'utente ha avuto ragione.
#
#def prompt_for_id() -> int:
#    ...
#    flashcard = get_flashcard_by_id(id)
#    ...
#    user_answer = prompt_for_answer()
#    is_correct = check_answer(user_answer, flashcard['answer'])
#    ...
#Convertire l'interfaccia della riga di comando in un'applicazione Flask:
#
#Per iniziare, importare i moduli necessari e creare una nuova istanza dell'applicazione Flask:
#
#from flask import Flask, render_template, request
#app = Flask(__name__)
#Sostituire i prompt dell'interfaccia della riga di comando con route e viste Flask. Ogni route in un'applicazione Flask è associata a una funzione Python. Quando si accede al percorso tramite un browser Web, viene eseguita la funzione associata.
#
#Ad esempio, crea un percorso per ottenere una flashcard in base all'ID:
#
#@app.route('/flashcard/<int:id>')
#def flashcard(id):
#    flashcard = get_flashcard_by_id(id)
#    return render_template('flashcard.html', flashcard=flashcard)
#Creare un file modello HTML denominato 'flashcard.html' in una cartella templates nella directory del progetto. Questo file deve contenere la struttura HTML della flashcard e del modulo, con segnaposto per i dati della flashcard.
#
#Per esempio:
#
#<h1>{{ flashcard.question }}</h1>
#<form action="/answer/{{ flashcard.id }}" method="post">
#    <input type="text" name="answer">
#    <input type="submit" value="Submit">
#</form>
#Il codice HTML fornito è un modello per la visualizzazione di una flashcard e un modulo per l'invio di una risposta. Il modello utilizza il linguaggio di template Jinja2 di Flask.
#
#<h1>{{ flashcard.question }}</h1>: Questa riga mostra la domanda della flashcard. È un segnaposto che viene sostituito con la domanda effettiva quando viene eseguito il rendering del modello.{{ flashcard.question }}
#
#<form action="/answer/{{ flashcard.id }}" method="post">: questa riga inizia un modulo. L'attributo specifica dove inviare i dati del modulo quando il modulo viene inviato. In questo caso, i dati del modulo vengono inviati all'URL. È un segnaposto che viene sostituito con l'ID effettivo della flashcard quando viene eseguito il rendering del modello. L'attributo specifica che il metodo HTTP POST deve essere utilizzato per l'invio dei dati del modulo.action/answer/{{ flashcard.id }}{{ flashcard.id }}method="post"
#
#<input type="text" name="answer">: questa riga crea un campo di immissione di testo in cui l'utente può inserire la propria risposta.
#
#<input type="submit" value="Submit">: questa riga crea un pulsante di invio. Quando l'utente fa clic su questo pulsante, i dati del modulo vengono inviati all'URL specificato nell'attributo.action
#
#Gestire gli invii dei moduli:
#
#Aggiungere una route per gestire le richieste POST dal modulo.
#
#Per esempio:
#
#@app.route('/answer/<int:id>', methods=['POST'])
#def answer(id):
#    user_answer = request.form.get('answer')
#    flashcard = get_flashcard_by_id(id)
#    is_correct = check_answer(user_answer, flashcard['answer'])
#    return render_template('result.html', is_correct=is_correct)
#Creare un file modello HTML denominato 'result.html' nella cartella dei modelli. Questo file dovrebbe visualizzare un messaggio in base al fatto che la risposta dell'utente sia corretta.
#
#Per esempio:
#
#{% if is_correct %}
#    <h1>Correct!</h1>
#{% else %}
#    <h1>Incorrect.</h1>
#{% endif %}
#Aggiungi una funzione flashcard casuale (get_random_flashcard):
#
#Scrivi una funzione per ottenere una flashcard casuale.get_random_flashcard() -> dict:
#
#Aggiungere una route per l'utilizzo di questa funzione./flashcard/random
#
#Per esempio:
#
#@app.route('/flashcard/random')
#def random_flashcard():
#    flashcard = get_random_flashcard()
#    return render_template('flashcard.html', flashcard=flashcard)
#È possibile utilizzare lo stesso modello 'flashcard.html' per questo percorso.