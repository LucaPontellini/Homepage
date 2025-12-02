# Esercizio 10: Gestione dei Todos per un Utente su JSONPlaceholder

#Usa la libreria `requests` per interagire con l'API JSONPlaceholder. Implementa uno script Python che esegua le seguenti operazioni:

#1. Recupera tutti i todos pubblicati dall'utente con ID = 1.
#2. Trova il primo todo incompleto (ovvero con `completed: false`).
#3. Se trovato, marca quel todo come completato utilizzando una richiesta PUT. Altrimenti, segnala che non ci sono todos incompleti.

#Utilizza l'endpoint `https://jsonplaceholder.typicode.com/todos?userId=1` per recuperare i todos e `https://jsonplaceholder.typicode.com/todos/{todo_id}` per aggiornare un todo specifico.

#Assicurati di gestire gli errori HTTP e di stampare i risultati in modo leggibile.

#### Esempio di Output

#```
#--- Todos dell'utente 1 ---
#Todos totali: 20
#Completati: 11
#Incompleti: 9

#--- Primo todo incompleto trovato ---
#ID: 2, Titolo: quis ut nam facilis et officia qui, Completato: False

#--- Todo aggiornato ---
#ID: 2, Titolo: quis ut nam facilis et officia qui, Completato: True
#```

#Oppure, se non ci sono incompleti:

#```
#--- Todos dell'utente 1 ---
#Todos totali: 20
#Completati: 20
#Incompleti: 0

#Nessun todo incompleto trovato.
#```

import requests

def main():
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId=1"
    response = requests.get(todos_url)
    
    if response.status_code != 200:
        print(f"Errore nel recupero dei todos: {response.status_code}")
        return
    
    todos = response.json()
    
    total_todos = len(todos)
    
    completed_todos = 0
    incomplete_todos = 0
    
    for todo in todos:
        if todo["completed"]:
            completed_todos += 1
        else:
            incomplete_todos += 1
    
    print(f"--- Todos dell'utente 1 ---")
    print(f"Todos totali: {total_todos}")
    print(f"Completati: {completed_todos}")
    print(f"Incompleti: {incomplete_todos}\n")
    
    first_incomplete_todo = None
    for todo in todos:
        if not todo["completed"]:
            first_incomplete_todo = todo
            break
    
    if first_incomplete_todo:
        print(f"--- Primo todo incompleto trovato ---")
        print(f"ID: {first_incomplete_todo['id']}, Titolo: {first_incomplete_todo['title']}, Completato: {first_incomplete_todo['completed']}\n")
        
        update_url = f"https://jsonplaceholder.typicode.com/todos/{first_incomplete_todo['id']}"
        updated_data = {
            "userId": first_incomplete_todo['userId'],
            "id": first_incomplete_todo['id'],
            "title": first_incomplete_todo['title'],
            "completed": True
        }
        
        update_response = requests.put(update_url, json=updated_data)
        
        if update_response.status_code != 200:
            print(f"Errore nell'aggiornamento del todo: {update_response.status_code}")
            return
        
        updated_todo = update_response.json()
        
        print(f"--- Todo aggiornato ---")
        print(f"ID: {updated_todo['id']}, Titolo: {updated_todo['title']}, Completato: {updated_todo['completed']}")
    else:
        print("Nessun todo incompleto trovato.")

if __name__ == "__main__":
    main()