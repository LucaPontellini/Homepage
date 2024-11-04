import pytest
from auto_engine import Car, Engine  # Ensure the path is correct

def test_car_attributes():
    car = Car("Fiat", "500")
    assert car.brand == "Fiat"
    assert car.model == "500"
    assert car.engine is None

def test_engine_attributes():
    engine = Engine("ENG123456", "Gasoline")
    assert engine.serial_number == "ENG123456"
    assert engine.type == "Gasoline"
    assert engine.car is None

def test_car_engine_association():
    car = Car("Fiat", "500")
    engine = Engine("ENG123456", "Gasoline")

    car.associate_engine(engine)

    assert car.engine == engine
    assert engine.car == car

def test_one_to_one_association():
    car1 = Car("Fiat", "500")
    engine1 = Engine("ENG123456", "Gasoline")
    car2 = Car("Toyota", "Corolla")
    engine2 = Engine("ENG654321", "Diesel")

    car1.associate_engine(engine1)
    car2.associate_engine(engine2)

    assert car1.engine == engine1
    assert engine1.car == car1
    assert car2.engine == engine2
    assert engine2.car == car2

def test_overwrite_association():
    car = Car("Fiat", "500")
    engine1 = Engine("ENG123456", "Gasoline")
    engine2 = Engine("ENG654321", "Diesel")

    car.associate_engine(engine1)
    assert car.engine == engine1
    assert engine1.car == car

    car.associate_engine(engine2)
    assert car.engine == engine2
    assert engine2.car == car
    assert engine1.car is None