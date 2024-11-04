from Pontellini_009 import Book  # type: ignore

def test_book_getter_setter():
    book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1200)
    assert book.title == "The Lord of the Rings"
    assert book.author == "J.R.R. Tolkien"
    assert book.pages == 1200

    book.title = "The Hobbit"
    assert book.title == "The Hobbit"

    book.author = "J.R.R. Tolkien"
    assert book.author == "J.R.R. Tolkien"

    book.pages = 310
    assert book.pages == 310

def test_book_invalid_title():
    book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1200)
    try:
        book.title = ""
    except ValueError as e:
        assert str(e) == "The title cannot be an empty string."

def test_book_invalid_author():
    book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1200)
    try:
        book.author = ""
    except ValueError as e:
        assert str(e) == "The author cannot be an empty string."

def test_book_invalid_pages():
    book = Book("The Lord of the Rings", "J.R.R. Tolkien", 1200)
    try:
        book.pages = -1
    except ValueError as e:
        assert str(e) == "The number of pages must be a positive number."