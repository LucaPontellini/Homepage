import pytest
from Pontellini_003 import Vehicle

@pytest.fixture(autouse=True)
def reset_number_vehicles():
    Vehicle.number_of_vehicles = 0

def test_number_vehicles_initial():
    assert Vehicle.get_number_of_vehicles() == 0

def test_creation_vehicle():
    car1 = Vehicle("Car", "Toyota")
    assert Vehicle.get_number_of_vehicles() == 1

def test_creation_of_vehicles():
    car1 = Vehicle("Car", "Toyota")
    motion1 = Vehicle("Motion", "Honda")
    assert Vehicle.get_number_of_vehicles() == 2

def test_creation_of_three_vehicles():
    car1 = Vehicle("Car", "Toyota")
    motion1 = Vehicle("Motion", "Honda")
    bike1 = Vehicle("Bike", "Bianchi")
    assert Vehicle.get_number_of_vehicles() == 3