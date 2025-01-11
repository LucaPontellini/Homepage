from Pontellini_013 import House, Room  # type: ignore

def test_house_attributes():
    house = House("Via delle Rose 15", "Maria Rossi")
    assert house.address == "Via delle Rose 15"
    assert house.owner == "Maria Rossi"
    assert house.rooms == []

def test_room_attributes():
    room = Room("Living room", 30)
    assert room.name == "Living room"
    assert room.surface == 30

def test_add_room():
    house = House("Via delle Rose 15", "Maria Rossi")
    room = Room("Living room", 30)
    house.add_room(room)
    assert room in house.rooms

def test_multi_add_room():
    house = House("Via delle Rose 15", "Maria Rossi")
    room1 = Room("Living room", 30)
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
    house = House("Via delle Rose 15", "Maria Rossi")
    room1 = Room("Living room", 30)
    room2 = Room("Kitchen", 15)
    house.add_room(room1)
    house.add_room(room2)

    house.print_rooms()
    captured = capfd.readouterr()
    assert "Living room (30 sqm)" in captured.out
    assert "Kitchen (15 sqm)" in captured.out