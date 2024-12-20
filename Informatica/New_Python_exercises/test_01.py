import pytest
from Pontellini_001 import Person

@pytest.fixture
def person():
    return Person("Mario", 30, "Rome")

def test_greets(person):
    assert person.greets() == "Hello, my name is Mario."

def test_description(person):
    assert person.description() == "I'm 30 and i live in Rome."