#Esercizio:

#Esercizio del modulo di registrazione dell'utente
#In questo esercizio verrà creato un semplice modulo di registrazione utente utilizzando Flask.
#L'applicazione presenterà all'utente un modulo per inserire il nome utente, l'e-mail e la password.
#Al momento dell'invio, l'applicazione restituirà un messaggio di esito positivo.

#Fabbisogno
#Pagina del modulo (/):
#Quando l'utente visita l'URL principale (), dovrebbe visualizzare un modulo con campi per nome utente, e-mail e password.
#Il modulo dovrebbe anche includere un pulsante "Invia" per consentire all'utente di inviare la propria registrazione.

#Pagina di successo (/success):
#Quando l'utente invia il modulo, l'applicazione deve visualizzare un messaggio di esito positivo in una nuova pagina.
#Il messaggio deve includere il nome utente e l'indirizzo e-mail immessi dall'utente.

#Gestione dei dati:
#I dati del modulo devono essere inviati dal client al server quando l'utente invia il modulo.
#Il server deve estrarre il nome utente e l'e-mail dai dati del modulo da includere nel messaggio di successo.

#Metodi HTTP:
#La pagina del modulo deve essere accessibile tramite una richiesta GET all'URL radice ().
#Il modulo deve essere inviato tramite una richiesta POST all'URL.//success

#Bonus
#Se finisci la parte principale dell'esercizio e vuoi una sfida in più, prova ad aggiungere le seguenti funzionalità:

#Convalida dell'input:
#Verifica che il nome utente, l'e-mail e la password soddisfino determinati requisiti (ad esempio, lunghezza minima, contiene determinati caratteri).
#Se l'input non è valido, mostra un messaggio di errore all'utente.

#Hashing delle password:
#Invece di inviare la password come testo normale, eseguirne l'hashing sul lato client prima di inviarla al server.

#Esempio:
#https://github.com/angelogalantiscuola/IT/blob/main/python/modules_library_packages/examples/flask_request_example.py

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        e_mail = request.form.get('email')
        password = request.form.get('password')
        return f"You posted:<br> Name: {str(name)}, e-mail: {str(e_mail)} and password: {str(password)}"
    else:
        return render_template('user_table.html')

if __name__ == '__main__':
    app.run(debug=True, port=12345)