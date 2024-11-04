# pylint: disable=redefined-outer-name
import pytest
from Pontellini_001 import Person

# The @pytest.fixture decorator in pytest is used to define a fixture function.
# Fixtures are a way to provide a fixed baseline upon which tests can reliably and repeatedly execute.
# They are used to set up some context (like creating objects, connecting to databases, etc.)
# before running tests and to clean up afterward.

@pytest.fixture
def person():
    return Person("Mario", 30, "Roma")

def test_greets(person):
    assert person.greets() == "Hello, my name is Mario."

def test_description(person):
    assert person.description() == "I'm 30 and i live in Rome."