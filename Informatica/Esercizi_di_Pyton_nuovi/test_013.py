import pytest
from house_room import House, Room  # Ensure the path is correct

def test_house_attributes():
    house = House("15 Rose Street", "Maria Rossi")
    assert house.address == "15 Rose Street"
    assert house.owner == "Maria Rossi"
    assert house.rooms == []

def test_room_attributes():
    room = Room("Living Room", 30)
    assert room.name == "Living Room"
    assert room.area == 30

def test_add_room():
    house = House("15 Rose Street", "Maria Rossi")
    room = Room("Living Room", 30)
    house.add_room(room)
    assert room in house.rooms

def test_multi_add_room():
    house = House("15 Rose Street", "Maria Rossi")
    room1 = Room("Living Room", 30)
    room2 = Room("Kitchen", 15)
    room3 = Room("Bedroom", 20)
    house.add_room(room1)
    house.add_room(room2)
    house.add_room(room3)
    assert len(house.rooms) == 3
    assert room1 in house.rooms
    assert room2 in house.rooms
    assert room3 in house.rooms

def test_print_rooms(capfd):
    house = House("15 Rose Street", "Maria Rossi")
    room1 = Room("Living Room", 30)
    room2 = Room("Kitchen", 15)
    house.add_room(room1)
    house.add_room(room2)

    house.print_rooms()
    captured = capfd.readouterr()
    assert "Living Room (30 sqm)" in captured.out
    assert "Kitchen (15 sqm)" in captured.out