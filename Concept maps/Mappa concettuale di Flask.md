# Mappa Concettuale di Flask

## Concetti Principali
- Flask
  - Microframework per Python
  - Utilizzato per sviluppare web application

## Concetti Fondamentali
- Routes
  - URL mapping a funzioni Python
  - Definite con il decoratore `@app.route()`
- Views
  - Le funzioni Python associate alle routes
  - Eseguono azioni e restituiscono risposte HTTP
- Templates
  - File HTML con placeholders dinamici
  - Renderizzati con Flask per produrre pagine web dinamiche

## Struttura di Base
- `app.py`
  - Punto di partenza dell'applicazione Flask
  - Contiene l'istanza principale dell'app (`app`)
- `templates/`
  - Directory per i file HTML (Jinja2 templates)
- `static/`
  - Directory per file statici (CSS, JS, immagini)

## Concetti Avanzati
- Flask Extensions
  - Pacchetti aggiuntivi per funzionalità specifiche
  - Esempi: Flask-SQLAlchemy, Flask-WTF
- Middleware
  - Funzionalità di pre-elaborazione e post-elaborazione
  - Esempi: logging, autenticazione
- Flask CLI
  - Interfaccia a riga di comando per gestire l'applicazione
  - Esempi: `flask run`, `flask shell`

## Flask in un Contesto di Produzione
- WSGI
  - Interfaccia standard Python per server web
  - Esempi: Gunicorn, uWSGI
- Deployment
  - Distribuzione dell'applicazione Flask su server
  - Esempi: Heroku, AWS, Docker

## Ecosistema di Flask
- Flask-SQLAlchemy
  - Integrazione di SQLAlchemy con Flask
- Flask-WTF
  - Supporto per gestione dei form in Flask
- Flask-Login
  - Gestione dell'autenticazione degli utenti

## Esempio di Applicazione
```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Home')

if __name__ == '__main__':
    app.run(debug=True)
