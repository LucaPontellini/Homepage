# Esercizio 9: Interazione Avanzata con JSONPlaceholder

# Usa la libreria `requests` per consumare l'API JSONPlaceholder. Implementa uno script Python che esegua le seguenti operazioni:

# 1. Recupera tutti i post pubblicati dall'utente con ID = 1 e stampali.
# 2. Recupera i commenti per il primo post e stampali.
# 3. Crea un nuovo commento per il primo post dell'utente, utilizzando una richiesta POST.

# Utilizza la documentazione di JSONPlaceholder per gli endpoint: `https://jsonplaceholder.typicode.com/posts?userId=1` per i post, `https://jsonplaceholder.typicode.com/posts/{post_id}/comments` per i commenti, e `https://jsonplaceholder.typicode.com/comments` per creare un commento.

# Assicurati di gestire gli errori HTTP e di stampare i risultati in modo leggibile.

### Esempio di Output

# ```
# --- Post dell'utente 1 ---
# ID Post: 1, Titolo: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
# ID Post: 2, Titolo: qui est esse
# ID Post: 3, Titolo: ea molestias quasi exercitationem repellat qui ipsa sit aut

# --- Commenti per il primo post ---
# - id labore ex et quam laborum: laudantium enim quasi est quidem magnam voluptate ipsam eos
# - quo vero reiciendis velit similique earum: est natus enim nihil est dolore omnis voluptatem numquam

# --- Nuovo Commento Creato ---
# {
#     "postId": 1,
#     "id": 501,
#     "name": "Nuovo Commentatore",
#     "email": "nuovo@example.com",
#     "body": "Questo è un commento aggiunto tramite API!"
# }
# ```

# Esercizio 9: Interazione Avanzata con JSONPlaceholder

# Usa la libreria `requests` per consumare l'API JSONPlaceholder. Implementa uno script Python che esegua le seguenti operazioni:

# 1. Recupera tutti i post pubblicati dall'utente con ID = 1 e stampali.
# 2. Recupera i commenti per il primo post e stampali.
# 3. Crea un nuovo commento per il primo post dell'utente, utilizzando una richiesta POST.

# Utilizza la documentazione di JSONPlaceholder per gli endpoint: `https://jsonplaceholder.typicode.com/posts?userId=1` per i post, `https://jsonplaceholder.typicode.com/posts/{post_id}/comments` per i commenti, e `https://jsonplaceholder.typicode.com/comments` per creare un commento.

# Assicurati di gestire gli errori HTTP e di stampare i risultati in modo leggibile.

### Esempio di Output

# ```
# --- Post dell'utente 1 ---
# ID Post: 1, Titolo: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
# ID Post: 2, Titolo: qui est esse
# ID Post: 3, Titolo: ea molestias quasi exercitationem repellat qui ipsa sit aut

# --- Commenti per il primo post ---
# - id labore ex et quam laborum: laudantium enim quasi est quidem magnam voluptate ipsam eos
# - quo vero reiciendis velit similique earum: est natus enim nihil est dolore omnis voluptatem numquam

# --- Nuovo Commento Creato ---
# {
#     "postId": 1,
#     "id": 501,
#     "name": "Nuovo Commentatore",
#     "email": "nuovo@example.com",
#     "body": "Questo è un commento aggiunto tramite API!"
# }
# ```

import requests
import json

user_id = 1
url_user = f"https://jsonplaceholder.typicode.com/users/{user_id}"

try:
    response = requests.get(url_user)
    response.raise_for_status()
    dati_utente = response.json()

    print("--- Dati Utente Ricevuti ---")
    print(json.dumps(dati_utente, indent=4))

    print("\n--- Informazioni Specifiche ---")
    print(f"Nome: {dati_utente['name']}")
    print(f"Email: {dati_utente['email']}")
    print(f"Città: {dati_utente['address']['city']}")
except requests.exceptions.RequestException as err:
    print(f"Errore nel recupero utente: {err}")

url_posts = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"

try:
    response = requests.get(url_posts)
    response.raise_for_status()
    posts = response.json()

    print("\n--- Post dell'utente 1 ---")
    for post in posts:
        print(f"ID Post: {post['id']}, Titolo: {post['title']}")

    first_post_id = posts[0]["id"]
except requests.exceptions.RequestException as err:
    print(f"Errore nel recupero dei post: {err}")

url_comments = f"https://jsonplaceholder.typicode.com/posts/{first_post_id}/comments"

try:
    response = requests.get(url_comments)
    response.raise_for_status()
    comments = response.json()

    print("\n--- Commenti per il primo post ---")
    for c in comments[:5]:
        print(f"- {c['name']}: {c['body']}")
except requests.exceptions.RequestException as err:
    print(f"Errore nel recupero dei commenti: {err}")

url_new_comment = "https://jsonplaceholder.typicode.com/comments"
nuovo_commento = {
    "postId": first_post_id,
    "name": "Nuovo Commentatore",
    "email": "nuovo@example.com",
    "body": "Questo è un commento aggiunto tramite API!"
}

try:
    response = requests.post(url_new_comment, json=nuovo_commento)
    response.raise_for_status()
    commento_creato = response.json()

    print("\n--- Nuovo Commento Creato ---")
    print(json.dumps(commento_creato, indent=4))
except requests.exceptions.RequestException as err:
    print(f"Errore nella creazione del commento: {err}")

url_new_post = "https://jsonplaceholder.typicode.com/posts"
nuovo_post = {
    "title": "Il Mio Nuovo Post",
    "body": "Questo è il contenuto del mio primo post creato tramite API!",
    "userId": user_id
}

try:
    response = requests.post(url_new_post, json=nuovo_post)
    response.raise_for_status()
    post_creato = response.json()

    print("\n--- Nuovo Post Creato ---")
    print(f"Status Code: {response.status_code}")
    print(json.dumps(post_creato, indent=4))
    print(f"\nIl nostro post è stato creato con ID: {post_creato['id']}")
except requests.exceptions.RequestException as err:
    print(f"Errore nella creazione del post: {err}")