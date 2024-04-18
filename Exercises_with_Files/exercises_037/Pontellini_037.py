#Esercizio:
#Elenco ordinato con collegamenti da json
#Caricare il file JSON contenente i collegamenti.
#Creare un'app Flask.
#Definire una route che gestirà la richiesta GET per visualizzare l'elenco dei collegamenti. Il modello deve ottenere i collegamenti in modo dinamico dal file json.
#Nota: Ricordati di semplificare il problema e risolverlo passo dopo passo.
#
#File JSON
#[
#    {
#        "text": "Google",
#        "href": "https://www.google.com"
#    },
#    {
#        "text": "GitHub",
#        "href": "https://github.com"
#    },
#    {
#        "text": "Stack Overflow",
#        "href": "https://stackoverflow.com"
#    }
#]
#File HTML
#Il modello deve ottenere i collegamenti dinamicamente dal file json.
#
#<!DOCTYPE html>
#<html>
#<head>
#    <title>Links Page</title>
#</head>
#<body>
#    <h1>Links</h1>
#    <ol>
#        <li><a href="https://www.google.com">Google</a></li>
#        <li><a href="https://github.com">GitHub</a></li>
#        <li><a href="https://stackoverflow.com">Stack Overflow</a></li>
#    </ol>
#</body>
#</html>

import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def view_the_file():
    with open('/home/pontellini/Homepage/Exercises_with_Files/exercises_037/websites.json',"r") as f:
        websites = json.load(f)
    return render_template('websites.html', websites=websites)

if __name__ == '__main__':
    app.run(debug=True, port=12345)