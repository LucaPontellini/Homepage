class Car:
    def __init__(self, plate: str, model: str, category: str, availability: bool):
        self.model = model
        self.category = category
        self.plate = plate
        self.availability = availability
    
    def __str__(self):
        return f"Car {self.model} with plate {self.plate} is a {self.category} car"

class CarRentalAgency:
    def __init__(self, list: list[Car]):
        self.cars = list[Car]

    def __str__(self):
        return f"CarRentalAgency with {len(self.cars)} cars"
    
    def add_cars(self, car: Car):
        self.cars.append(car)
    
    def renting_a_car(self, plate: str):
        for car in self.cars:
            if car.plate == plate:
                car.availability = False
                return car
        return None
    
    def view_available_cars(self):
        available_cars = []
        for car in self.cars:
            if car.availability:
                available_cars.append(car)
        return available_cars
    
    def view_the_rentals_made(self):
        rentals = []
        for car in self.cars:
            if not car.availability:
                rentals.append(car)
        return rentals