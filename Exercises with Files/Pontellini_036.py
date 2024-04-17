#Esercizio:
#Tabella con i voti degli studenti da un file JSON
#Carica il file JSON contenente i voti degli studenti.
#Creare un'app Flask.
#Definire una route che gestirà la richiesta GET per visualizzare la tabella.
#Nella funzione route, eseguire il rendering di un modello che visualizzerà i voti degli studenti in una tabella. Il modello deve ottenere i voti in modo dinamico dal file json.

#<table>
#    <tr>
#        <th>Student</th>
#        <th>Vote</th>
#    </tr>
#    <tr>
#        <td>Alice</td>
#        <td>5</td>
#    </tr>
#    ...
#</table>
#[
#    {
#        "student": "Alice",
#        "vote": 5
#    },
#    {
#        "student": "Bob",
#        "vote": 3
#    },
#    {
#        "student": "Charlie",
#        "vote": 4
#    },
#    {
#        "student": "Dave",
#        "vote": 2
#    }
#]

import json
from flask import Flask, render_template

app = Flask(__name__)

file_json = 'student_grades.json'

with open(file_json) as f:
    grades = json.load(f)

@app.route('/')
def view_the_table():
    return render_template('table.html', grades=grades)

if __name__ == '__main__':
    app.run(debug=True, port=1234)