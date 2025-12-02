import requests

BASE_URL = "http://localhost:3001"

def get_data(endpoint, params=None):
    """Funzione helper per chiamare l'API con gestione errori."""
    try:
        response = requests.get(f"{BASE_URL}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Errore nella richiesta a {endpoint}: {e}")
        return []

def main():
    # --- 1. Cerca Libri di un Autore (ID = 1) ---
    author_id = 1
    books = get_data("books", {"author_id": author_id})
    authors = get_data("authors")

    # Trova il nome autore con ciclo esplicito
    author_name = "Sconosciuto"
    i = 0
    while i < len(authors):
        autore_corrente = authors[i]

        # Step 1: estrazione id
        autore_id_corrente = autore_corrente.get("id", None)

        # Step 2: confronto
        condizione_match = (autore_id_corrente == author_id)

        # Step 3: valutazione condizione
        if condizione_match:
            # Step 4: estrazione nome
            author_name = autore_corrente.get("name", "Sconosciuto")

            # Step 5: uscita dal ciclo
            break

        i += 1

    print(f"Libri di {author_name}:")
    idx = 0
    while idx < len(books):
        book = books[idx]

        titolo = book.get("title", "")
        pagine = book.get("pages", 0)

        output = "  - " + str(titolo) + " (" + str(pagine) + " pagine)"
        print(output)
        idx += 1

    # --- 2. Filtra per Disponibilità ---
    available_books = []
    j = 0
    while j < len(books):
        b = books[j]

        # Step 1: estrazione flag
        disponibile_flag = b.get("available", False)

        # Step 2: valutazione condizione
        condizione_disponibile = (disponibile_flag is True)

        # Step 3: azione condizionata
        if condizione_disponibile:
            available_books.append(b)

        j += 1

    print("\nLibri disponibili:")
    k = 0
    while k < len(available_books):
        book = available_books[k]
        titolo = book.get("title", "")
        output = "  - " + str(titolo)
        print(output)
        k += 1

    # --- 3. Conta Pagine Totali ---
    total_pages = 0
    t = 0
    while t < len(available_books):
        b = available_books[t]
        pagine = b.get("pages", 0)
        total_pages = total_pages + pagine
        t += 1

    print("\nPagine totali disponibili: " + str(total_pages))

    # --- 4. Libri per Genere (Fantasy ID = 101) ---
    genre_id = 101
    genre_books = get_data("books", {"genre_id": genre_id})
    genres = get_data("genres")

    genre_name = "Sconosciuto"
    g_idx = 0
    while g_idx < len(genres):
        g = genres[g_idx]

        # Step 1: estrazione id
        genre_id_corrente = g.get("id", None)

        # Step 2: confronto
        condizione_match_genere = (genre_id_corrente == genre_id)

        # Step 3: valutazione condizione
        if condizione_match_genere:
            genre_name = g.get("name", "Sconosciuto")
            break

        g_idx += 1

    print("\nGenere: " + str(genre_name))

    count_genre = 0
    gb_idx = 0
    while gb_idx < len(genre_books):
        count_genre = count_genre + 1
        gb_idx += 1

    print("Numero di libri: " + str(count_genre))

    gb_print_idx = 0
    while gb_print_idx < len(genre_books):
        book = genre_books[gb_print_idx]

        titolo = book.get("title", "")
        pagine = book.get("pages", 0)
        disponibile_flag = book.get("available", False)

        # Step 1: valutazione condizione
        condizione_disponibile = (disponibile_flag is True)

        # Step 2: derivazione stringa
        if condizione_disponibile:
            disponibile_str = "Disponibile"
        else:
            disponibile_str = "Non disponibile"

        output = "  - " + str(titolo) + " (" + str(pagine) + " pagine) - " + disponibile_str
        print(output)

        gb_print_idx += 1

if __name__ == "__main__":
    main()