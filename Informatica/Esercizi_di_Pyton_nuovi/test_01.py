import pytest
from Homepage.Informatica.Esercizi_di_Pyton_nuovi.Pontellini_001 import Person

@pytest.fixture()
def test_greets():
    assert Person.greets()

def test_description():
    assert Person.description()