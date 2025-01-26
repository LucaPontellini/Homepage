from datetime import date, datetime

class Reservation:
    def __init__(self, customer_name: str, date: date, number_of_people: int, status: str):
        self.name = customer_name
        self.date = date
        self.number_of_people = number_of_people
        self.status = status

    def __str__(self):
        return f"{self.name} - {self.date} - {self.number_of_people} - {self.status}"
    
class ReservationManager:
    def __init__(self):
        self.reservations = []
    
    def add_reservation(self, customer_name: str, date: date, number_of_people: int, status: str):
        self.reservations.append(Reservation(customer_name, date, number_of_people, status))
    
    def search_reservation_by_name(self, customer_name: str):
        for reservation in self.reservations:
            if reservation.name == customer_name:
                return reservation
    
    def search_reservation_by_date(self, date: date):
        for reservation in self.reservations:
            if reservation.date == date:
                return reservation
    
    def view_all_reservations(self):
        return self.reservations
    
    def cancel_reservation(self, customer_name: str, date: date):
        for reservation in self.reservations:
            if reservation.name == customer_name and reservation.date == date:
                reservation.status = "Cancelled"
                return True
        return False

def main():
    reservation_manager = ReservationManager()
    customer_name = input("Enter customer name: ")
    date_str = input("Enter date (YYYY-MM-DD): ")
    date_obj = datetime.strptime(date_str, "%Y-%m-%d").date()
    number_of_people = int(input("Enter number of people: "))
    status = input("Enter status: ")

    reservation_manager.add_reservation(customer_name, date_obj, number_of_people, status)
    print("Reservation added successfully!")

    name_search = input("Enter customer name to search: ")
    reservations_by_name = reservation_manager.search_reservation_by_name(name_search)
    print("Reservations by name:")
    for reservation in reservations_by_name:
        print(reservation)

    date_search_str = input("Enter date (YYYY-MM-DD) to search: ")
    date_search_obj = datetime.strptime(date_search_str, "%Y-%m-%d").date()
    reservations_by_date = reservation_manager.search_reservation_by_date(date_search_obj)
    print("Reservations by date:")
    for reservation in reservations_by_date:
        print(reservation)

    print("All reservations:")
    for reservation in reservation_manager.view_all_reservations():
        print(reservation)

    cancel_name = input("Enter customer name to cancel: ")
    cancel_date_str = input("Enter date (YYYY-MM-DD) to cancel: ")
    cancel_date_obj = datetime.strptime(cancel_date_str, "%Y-%m-%d").date()
    if reservation_manager.cancel_reservation(cancel_name, cancel_date_obj):
        print("Reservation cancelled successfully!")
    else: print("Reservation not found.")

if __name__ == "__main__":
    main()