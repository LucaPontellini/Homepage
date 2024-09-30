from flask import Flask, render_template
import json

#Esercizio: Creazione di un'applicazione meteo semplice con Flask

#Passaggio 1: configurazione di base
#Impostare un nuovo progetto Flask.
#Creare un nuovo file Python e importare i moduli necessari (Flask, render_template e json).
#Inizializzare un nuovo server Web Flask.
#Crea un percorso di base per la home page ("/") che restituisce "Benvenuto nella nostra applicazione meteo!".

#Passaggio 2: utilizzo dei modelli
#Crea una nuova directory nel tuo progetto chiamata "templates".
#All'interno di questa directory, creare un file HTML list.html per l'elenco delle città.
#Questo file dovrebbe includere un messaggio di benvenuto e un elenco di città.
#Crea un percorso di base "/cities" che restituisce l'elenco delle città in HTML.

#Passaggio 3: instradamento dinamico
#Aggiungere un nuovo percorso che accetta il nome di una città come parametro.
#Questo percorso dovrebbe restituire un messaggio con il nome della città.
#Ad esempio, se l'itinerario è "/meteo/Parigi", la pagina dovrebbe visualizzare "Meteo per Parigi".

#Passaggio 4: Lettura dei dati da JSON
#Creare un file JSON nella directory del progetto che contenga i dati meteorologici per alcune città.
#I dati dovrebbero includere il nome della città e alcune informazioni meteorologiche (come temperatura e umidità).
#Aggiorna il percorso dinamico per leggere i dati meteo da questo file JSON e visualizzarli nella pagina.
#Ad esempio:
#{
#    "Parigi": {
#        "temperatura": "15C",
#        "umidità": "70%"
#    },
#    "Londra": {
#        "temperatura": "17C",
#        "umidità": "65%"
#    },
#    "New York": {
#        "temperatura": "20C",
#        "umidità": "60%"
#    }
#}

#Passaggio 5: visualizzazione dei dettagli meteo
#Crea un nuovo modello per la pagina meteo della città weather.html.
#Questo modello dovrebbe visualizzare il nome della città e le relative informazioni meteorologiche.
#Aggiornare il percorso dinamico per eseguire il rendering di questo modello, passando i dati meteo come parametro.

#<h1>Meteo per {{ città }}</h1>
#<p>Temperatura: {{ weather_info.temperatura }}</p>
#<p>Umidità: {{ weather_info.umidità }}</p>

#Passaggio 6: recupero di dati meteorologici reali da un'API
#Questo è molto difficile!
#In questo passaggio, modificherai la tua applicazione Flask per recuperare i dati meteorologici reali dall'API Open-Meteo.

app = Flask(__name__)

@app.route('/')

def home():
    return "Welcome to our weather app!"

@app.route('/cities')

def cities():
    city_list = ["Paris", "London", "New York"]
    return render_template('list.html', cities=city_list)

@app.route('/weather/<city>')  

def weather(city):
    with open('weather_data.json') as file:
        data = json.load(file)
    return render_template('weather.html', city=city, weather_info=data[city])

if __name__ == '__main__':
    app.run(debug=True)