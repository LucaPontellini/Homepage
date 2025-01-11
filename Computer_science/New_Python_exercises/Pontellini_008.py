#Esercizio 8: Sistema di Gestione di Ristorante con Calcolo del Conto e Stampa del Menu

#Obiettivo
#Creare una gerarchia di classi che rappresenti diversi tipi di piatti in un ristorante.
#Utilizzare l'ereditarietà per definire una classe base Piatto e classi derivate Antipasto, Primo, Secondo e Dolce che ereditano dalla classe base.
#Implementare metodi specifici per ogni tipo di piatto e aggiungere funzionalità avanzate come la gestione degli ordini, la ricerca di piatti, il calcolo del conto totale e la stampa del menu.

#Istruzioni
#Definisci una classe base chiamata Piatto con attributi di istanza nome, prezzo e disponibile.
#Implementa metodi di istanza nella classe Piatto per accedere e modificare questi attributi.
#Aggiungi un metodo ordina che imposta l'attributo disponibile a False e un metodo disponi che lo imposta a True.
#Definisci una classe derivata chiamata Antipasto che eredita dalla classe Piatto. Aggiungi attributi di istanza specifici per Antipasto, come ingredienti e porzione.
#Definisci una classe derivata chiamata Primo che eredita dalla classe Piatto. Aggiungi attributi di istanza specifici per Primo, come tipo_pasta e sugo.
#Definisci una classe derivata chiamata Secondo che eredita dalla classe Piatto. Aggiungi attributi di istanza specifici per Secondo, come tipo_carne e cottura.
#Definisci una classe derivata chiamata Dolce che eredita dalla classe Piatto. Aggiungi attributi di istanza specifici per Dolce, come tipo_dolce e calorie.
#Implementa metodi di istanza nelle classi Antipasto, Primo, Secondo e Dolce per accedere e modificare i loro attributi specifici.
#Aggiungi un metodo di ricerca nella classe Piatto che permette di cercare piatti per nome o prezzo.
#Implementa una funzione calcola_conto che prende una lista di piatti ordinati e restituisce il totale del conto.
#Implementa una funzione stampa_menu che prende una lista di piatti e stampa le informazioni di tutti i piatti.

#Esempio di Utilizzo
#class Piatto:
#    ...
#    def __str__(self):
#        return f"{self.nome} - {self.prezzo}€ - {'Disponibile' if self.disponibile else 'Non disponibile'}"

# Esempio di utilizzo
#antipasto = Antipasto("Bruschetta", 5.0, ["Pane", "Pomodoro", "Basilico"], "Piccola")
#primo = Primo("Spaghetti alla Carbonara", 12.0, "Spaghetti", "Carbonara")
#secondo = Secondo("Bistecca alla Fiorentina", 25.0, "Manzo", "Media")
#dolce = Dolce("Tiramisù", 6.0, "Tiramisù", 450)

#piatti_ordinati = [antipasto, primo, secondo, dolce]
#conto_totale = calcola_conto(piatti_ordinati)
#print(f"Il conto totale è: {conto_totale}€")  # Output: Il conto totale è: 48.0€

#print("\nMenu del Ristorante:")
#stampa_menu(piatti_ordinati)
#Output Atteso
#Il conto totale è: 48.0€

#Menu del Ristorante:
#Antipasto: Bruschetta - 5.0€ - Disponibile - Ingredienti: Pane, Pomodoro, Basilico - Porzione: Piccola
#Primo: Spaghetti alla Carbonara - 12.0€ - Disponibile - Tipo Pasta: Spaghetti - Sugo: Carbonara
#Secondo: Bistecca alla Fiorentina - 25.0€ - Disponibile - Tipo Carne: Manzo - Cottura: Media
#Dolce: Tiramisù - 6.0€ - Disponibile - Tipo Dolce: Tiramisù - Calorie: 450

class Dish:
    def __init__(self, name: str, price: float, available: bool = True):
        self.name = name
        self.price = price
        self.available = available
    
    def __str__(self):
        return f"{self.name} - {self.price}€ - {'Available' if self.available else 'Unavailable'}"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def is_available(self):
        return self.available

    def set_available(self, available):
        self.available = available

    def order(self):
        self.available = False

    def make_available(self):
        self.available = True

def search_dishes(dishes, name=None, price=None):
    results = []
    for dish in dishes:
        if name and name in dish.name:
            results.append(dish)
        elif price and dish.price == price:
            results.append(dish)
    return results

def calculate_bill(ordered_dishes):
    total_bill = 0
    for dish in ordered_dishes:
        total_bill += dish.price
    return total_bill

def print_menu(dishes):
    for dish in dishes:
        print(dish)

class Appetizer(Dish):
    def __init__(self, name: str, price: float, ingredients: list, portion: str, available: bool = True):
        super().__init__(name, price, available)
        self.ingredients = ingredients
        self.portion = portion
    
    def __str__(self):
        return f"Appetizer: {self.name} - {self.price}€ - {'Available' if self.available else 'Unavailable'} - Ingredients: {', '.join(self.ingredients)} - Portion: {self.portion}"

    def get_ingredients(self):
        return self.ingredients
        
    def set_ingredients(self, ingredients: list):
        self.ingredients = ingredients
    
    def get_portion(self):
        return self.portion
    
    def set_portion(self, portion: str):
        self.portion = portion

class FirstCourse(Dish):
    def __init__(self, name: str, price: float, pasta_type: str, sauce: str, available: bool = True):
        super().__init__(name, price, available)
        self.pasta_type = pasta_type
        self.sauce = sauce
    
    def __str__(self):
        return f"FirstCourse: {self.name} - {self.price}€ - {'Available' if self.available else 'Unavailable'} - Type of pasta: {self.pasta_type} - Sauce: {self.sauce}"
    
    def get_pasta_type(self):
        return self.pasta_type
    
    def set_pasta_type(self, pasta_type: str):
        self.pasta_type = pasta_type
    
    def get_sauce(self):
        return self.sauce
    
    def set_sauce(self, sauce: str):
        self.sauce = sauce

class MainCourse(Dish):
    def __init__(self, name: str, price: float, meat_type: str, cooking_level: str, available: bool = True):
        super().__init__(name, price, available)
        self.meat_type = meat_type
        self.cooking_level = cooking_level
    
    def __str__(self):
        return f"MainCourse: {self.name} - {self.price}€ - {'Available' if self.available else 'Unavailable'} - Type of meat: {self.meat_type} - Cooking level: {self.cooking_level}"
    
    def get_meat_type(self):
        return self.meat_type
    
    def set_meat_type(self, meat_type: str):
        self.meat_type = meat_type
    
    def get_cooking_level(self):
        return self.cooking_level
    
    def set_cooking_level(self, cooking_level: str):
        self.cooking_level = cooking_level

class Dessert(Dish):
    def __init__(self, name: str, price: float, dessert_type: str, calories: int, available: bool = True):
        super().__init__(name, price, available)
        self.dessert_type = dessert_type
        self.calories = calories
    
    def __str__(self):
        return f"Dessert: {self.name} - {self.price}€ - {'Available' if self.available else 'Unavailable'} - Type of dessert: {self.dessert_type} - Calories: {self.calories}"
    
    def get_dessert_type(self):
        return self.dessert_type
    
    def set_dessert_type(self, dessert_type: str):
        self.dessert_type = dessert_type
    
    def get_calories(self):
        return self.calories
    
    def set_calories(self, calories: int):
        self.calories = calories

appetizer = Appetizer("Bruschetta", 5.0, ["Bread", "Tomato", "Basil"], "Small")
first_course = FirstCourse("Spaghetti Carbonara", 12.0, "Spaghetti", "Carbonara")
main_course = MainCourse("Florentine Steak", 25.0, "Beef", "Medium")
dessert = Dessert("Tiramisu", 6.0, "Tiramisu", 450)

ordered_dishes = [appetizer, first_course, main_course, dessert]
total_bill = calculate_bill(ordered_dishes)
print(f"The total bill is: {total_bill}€")  # Output: The total bill is: 48.0€

print("\nRestaurant Menu:")
print_menu(ordered_dishes)