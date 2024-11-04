from Pontellini_007 import Library_Material, Book, Magazine, DVD  # type: ignore

def test_library_material():
    material = Library_Material("Generic Material", 2020)
    assert material.get_title() == "Generic Material"
    assert material.get_publication_year() == 2020
    assert material.is_available()

    material.borrow()
    assert not material.is_available()

    material.return_material()
    assert material.is_available()

def test_book():
    book = Book("The Lord of the Rings", 1954, "J.R.R. Tolkien", 1178)
    assert book.get_title() == "The Lord of the Rings"
    assert book.get_publication_year() == 1954
    assert book.get_author() == "J.R.R. Tolkien"
    assert book.get_page_count() == 1178

    book.borrow()
    assert not book.is_available()

    book.return_material()
    assert book.is_available()

def test_magazine():
    magazine = Magazine("National Geographic", 2023, 5, "May")
    assert magazine.get_title() == "National Geographic"
    assert magazine.get_publication_year() == 2023
    assert magazine.get_issue_number() == 5
    assert magazine.get_publication_month() == "May"

    magazine.borrow()
    assert not magazine.is_available()

    magazine.return_material()
    assert magazine.is_available()

def test_dvd():
    dvd = DVD("Inception", 2010, "Christopher Nolan", 148)
    assert dvd.get_title() == "Inception"
    assert dvd.get_publication_year() == 2010
    assert dvd.get_director() == "Christopher Nolan"
    assert dvd.get_duration() == 148

    dvd.borrow()
    assert not dvd.is_available()

    dvd.return_material()
    assert dvd.is_available()

def test_search():
    book = Book("The Lord of the Rings", 1954, "J.R.R. Tolkien", 1178)
    magazine = Magazine("National Geographic", 2023, 5, "May")
    dvd = DVD("Inception", 2010, "Christopher Nolan", 148)

    materials = [book, magazine, dvd]
    result = Library_Material.search(materials, title="Inception")
    assert result.get_title() == "Inception"