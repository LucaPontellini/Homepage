class Vehicle:
    def __init__(self, brand: str, model: str, fuel: str):
        self.brand = brand
        self.model = model
        self.fuel = fuel

    def __str__(self):
        return f"Brand: {self.brand} - Model: {self.model} - Fuel: {self.fuel}"
    
class Car(Vehicle):
    def __init__(self, brand: str, model: str, fuel: str):
        super().__init__(brand, model, fuel)

    def __str__(self):
        return f"Brand: {self.brand} - Model: {self.model} - Fuel: {self.fuel}"

class Truck(Vehicle):
    def __init__(self, brand: str, model: str, fuel: str):
        super().__init__(brand, model, fuel)

    def __str__(self):
        return f"Brand: {self.brand} - Model: {self.model} - Fuel: {self.fuel}"

class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def view_vehicles_information(self, brand: str, model: str, fuel: str):
        for vehicle in self.vehicles:
            print(vehicle)

def main():
    fleet = Fleet()
    
    car = str(input("Enter the car brand: "))
    model = str(input("Enter the car model: "))
    fuel = str(input("Enter the car fuel: "))

    vehicle = Vehicle(car, model, fuel)
    fleet.add_vehicle(vehicle)
    fleet.view_vehicles_information(car, model, fuel)
    
if __name__ == "__main__":
    main()