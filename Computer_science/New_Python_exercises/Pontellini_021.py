class Room:
    def __init__(self, number: int, type: str, availability: bool):
        self.number = number
        self.type = type
        self.availability = availability
    
    def __str__(self):
        return f"Room {self.number} is a {self.type} room and is {'available' if self.availability else 'not available'}"

class Hotel:
    def __init__(self, rooms: list, reservations: list):
        self.rooms = rooms
        self.reservations = reservations

    def __str__(self):
        return f"Hotel has {len(self.rooms)} rooms and {len(self.reservations)} reservations"
    
    def add_room(self, room: Room):

        if room in self.rooms:
            return "Room already exists"
        else: self.rooms.append(room)
    
    def room_booking(self, room: Room):
        if room.availability:
            room.availability = False
            self.reservations.append(room)
            return "Room booked"
        else: return "Room not available"
    
    def availability(self):
        for room in self.rooms:
            if room.availability:
                print(room)

def main():
    room1 = Room(1, "single", True)
    room2 = Room(2, "double", True)
    room3 = Room(3, "single", False)

    hotel = Hotel([room1, room2, room3], [])
    print(hotel)

    hotel.add_room(room1)
    print(hotel)

    hotel.add_room(Room(4, "double", True))
    print(hotel)

    print(hotel.room_booking(room1))
    print(hotel.room_booking(room3))
    print(hotel.room_booking(room3))

    hotel.availability()
    hotel.reservations = [room1, room3]

if __name__ == "__main__":
    main()