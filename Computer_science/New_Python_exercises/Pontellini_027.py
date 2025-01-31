from datetime import datetime

class Flight:
    def __init__(self, flight_number: int, destination: str, date_and_time_of_departure: datetime, maximum_number_of_passengers: int):
        self.flight_number = flight_number
        self.destination = destination
        self.date_and_time_of_departure = date_and_time_of_departure
        self.maximum_number_of_passengers = maximum_number_of_passengers

    def __str__(self):
        return f"Flight {self.flight_number} to {self.destination} departs at {self.date_and_time_of_departure} with a maximum of {self.maximum_number_of_passengers} passengers."

class Reservation:
    def __init__(self, passenger_name: str, class_type: str, flight: Flight):
        self.passenger_name = passenger_name
        self.class_type = class_type
        self.flight = flight

    def __str__(self):
        return f"Reservation for {self.passenger_name} in {self.class_type} class on flight {self.flight.flight_number}."

class BookingSystem:
    def __init__(self):
        self.list_of_flights = []
        self.list_of_reservations = []

    def add_flight(self, flight: Flight):
        self.list_of_flights.append(flight)

    def add_reservation(self, reservation: Reservation):
        self.list_of_reservations.append(reservation)

    def view_all_flights(self):
        for flight in self.list_of_flights:
            print(flight)

    def view_all_reservations(self):
        for reservation in self.list_of_reservations:
            print(reservation)

if __name__ == "__main__":
    booking_system = BookingSystem()

    flight1 = Flight(101, "Roma", datetime(2025, 1, 27, 18, 30), 150)
    booking_system.add_flight(flight1)
    reservation1 = Reservation("Mario Rossi", "premium", flight1)
    booking_system.add_reservation(reservation1)
    booking_system.view_all_flights()
    booking_system.view_all_reservations()