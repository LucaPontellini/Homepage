class Appetizer(Dish):
    def __init__(self, name: str, price: float, ingredients: list, portion: str, available: bool = True):
        super().__init__(name, price, available)
        self.ingredients = ingredients
        self.portion = portion

    def get_ingredients(self):
        return self.ingredients
        
    def set_ingredients(self, ingredients: list):
        self.ingredients = ingredients
    
    def get_portion(self):
        return self.portion
    
    def set_portion(self, portion: str):
        self.portion = portion

    def __str__(self):
        return f"{self.name} - {self.price}€ - {self.portion} - {'Available' if self.available else 'Unavailable'}"

class MainCourse(Dish):
    def __init__(self, name: str, price: float, type_of_pasta: str, sauce: str, available: bool = True):
        super().__init__(name, price, available)
        self.type_of_pasta = type_of_pasta
        self.sauce = sauce
    
    def get_type_of_pasta(self):
        return self.type_of_pasta
    
    def set_type_of_pasta(self, type_of_pasta: str):
        self.type_of_pasta = type_of_pasta
    
    def get_sauce(self):
        return self.sauce
    
    def set_sauce(self, sauce: str):
        self.sauce = sauce

    def __str__(self):
        return f"{self.name} - {self.price}€ - {self.type_of_pasta} with {self.sauce} - {'Available' if self.available else 'Unavailable'}"

class SecondCourse(Dish):
    def __init__(self, name: str, price: float, type_of_meat: str, cooking: str, available: bool = True):
        super().__init__(name, price, available)
        self.type_of_meat = type_of_meat
        self.cooking = cooking
    
    def get_type_of_meat(self):
        return self.type_of_meat
    
    def set_type_of_meat(self, type_of_meat: str):
        self.type_of_meat = type_of_meat

    def get_cooking(self):
        return self.cooking
    
    def set_cooking(self, cooking: str):
        self.cooking = cooking

    def __str__(self):
        return f"{self.name} - {self.price}€ - {self.type_of_meat} ({self.cooking}) - {'Available' if self.available else 'Unavailable'}"

class Dessert(Dish):
    def __init__(self, name: str, price: float, type_of_dessert: str, calories: int, available: bool = True):
        super().__init__(name, price, available)
        self.type_of_dessert = type_of_dessert
        self.calories = calories
    
    def get_type_of_dessert(self):
        return self.type_of_dessert
    
    def set_type_of_dessert(self, type_of_dessert: str):
        self.type_of_dessert = type_of_dessert
    
    def get_calories(self):
        return self.calories
    
    def set_calories(self, calories: int):
        self.calories = calories

    def __str__(self):
        return f"{self.name} - {self.price}€ - {self.type_of_dessert} - {self.calories} calories - {'Available' if self.available else 'Unavailable'}"

def calcola_conto(dishes):
    return sum(dish.get_price() for dish in dishes)

def stampa_menu(dishes):
    for dish in dishes:
        print(dish)

appetizer = Appetizer("Bruschetta", 5.0, ["Bread", "Tomato", "Basil"], "Small")
main_course = MainCourse("Spaghetti Carbonara", 12.0, "Spaghetti", "Carbonara")
second_course = SecondCourse("Florentine Steak", 25.0, "Beef", "Medium")
dessert = Dessert("Tiramisu", 6.0, "Tiramisu", 450)

ordered_dishes = [appetizer, main_course, second_course, dessert]
total_bill = calcola_conto(ordered_dishes)
print(f"The total bill is: {total_bill}€")  # Output: The total bill is: 48.0€

print("\nRestaurant Menu:")
stampa_menu(ordered_dishes)

# Esempio di ricerca
ricerca_per_nome = Dish.cerca_piatto(ordered_dishes, name="Tiramisu")
print("\nRicerca per nome 'Tiramisu':")
stampa_menu(ricerca_per_nome)

ricerca_per_prezzo = Dish.cerca_piatto(ordered_dishes, price=12.0)
print("\nRicerca per prezzo 12.0€:")
stampa_menu(ricerca_per_prezzo)