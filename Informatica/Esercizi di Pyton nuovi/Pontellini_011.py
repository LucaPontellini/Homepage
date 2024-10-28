#Esercizio 11: Tipologie di Ricette

#Prerequisiti
#Conoscenza delle classi e dell'ereditarietà in Python.
#Comprensione dei metodi getter e setter.
#Familiarità con i magic methods (__str__, __repr__, ecc.) in Python.

#Obiettivo
#Creare una gerarchia di classi che rappresenti diverse tipologie di ricette in cucina.
#Utilizzare l'ereditarietà per definire una classe base Ricetta e classi derivate Primo, Secondo, e Dolce che ereditano dalla classe base.
#Implementare metodi specifici per ogni tipo di ricetta e aggiungere funzionalità avanzate come il calcolo del tempo totale di preparazione,
#la verifica della disponibilità degli ingredienti e la stampa delle informazioni sulle ricette.

#Istruzioni
#Definisci una classe base chiamata Ricetta con attributi di istanza nome, tempo_preparazione, ingredienti e difficolta.
#Implementa metodi di istanza nella classe Ricetta per accedere e modificare questi attributi.
#Aggiungi un metodo aggiungi_ingrediente che permette di aggiungere un ingrediente alla lista degli ingredienti.
#Definisci una classe derivata chiamata Primo che eredita dalla classe Ricetta. Aggiungi attributi di istanza specifici per Primo, come tipo_pasta e sugo.
#Definisci una classe derivata chiamata Secondo che eredita dalla classe Ricetta. Aggiungi attributi di istanza specifici per Secondo, come tipo_carne e cottura.
#Definisci una classe derivata chiamata Dolce che eredita dalla classe Ricetta. Aggiungi attributi di istanza specifici per Dolce, come zucchero e tipo_dolce.
#Implementa metodi di istanza nelle classi Primo, Secondo, e Dolce per accedere e modificare i loro attributi specifici.
#Aggiungi un metodo di calcolo del tempo totale di preparazione nella classe Ricetta che somma il tempo di preparazione di tutte le ricette in una lista.
#Implementa una funzione verifica_ingredienti che prende una lista di ricette e restituisce quelle che possono essere preparate con gli ingredienti disponibili.
#Implementa una funzione stampa_ricette che prende una lista di ricette e stampa le informazioni di tutte le ricette.
#Esempio di Utilizzo
#class Ricetta:
#    ...
#    def __str__(self):
#        return f"{self.nome} - {self.tempo_preparazione} min - Difficoltà: {self.difficolta}"

## Esempio di utilizzo
#primo = Primo("Spaghetti alla Carbonara", 20, ["Spaghetti", "Uova", "Pancetta"], "Media", "Spaghetti", "Carbonara")
#secondo = Secondo("Bistecca alla Fiorentina", 30, ["Bistecca", "Sale", "Pepe"], "Alta", "Manzo", "Media")
#dolce = Dolce("Tiramisù", 30, ["Mascarpone", "Caffè", "Savoiardi"], "Media", 200, "Dessert")

#ricette = [primo, secondo, dolce]
#ricette_possibili = verifica_ingredienti(ricette, ["Spaghetti", "Uova", "Pancetta", "Bistecca", "Sale", "Pepe", "Mascarpone", "Caffè", "Savoiardi", "Pane", "Pomodoro", "Basilico"])
#print(f"Ricette che possono essere preparate: {len(ricette_possibili)}")

#print("\nInformazioni sulle ricette:")
#stampa_ricette(ricette)
#Output Atteso
#Ricette che possono essere preparate: 4

#Informazioni sulle ricette:
#Primo: Spaghetti alla Carbonara - 20 min - Difficoltà: Media - Tipo Pasta: Spaghetti - Sugo: Carbonara
#Secondo: Bistecca alla Fiorentina - 30 min - Difficoltà: Alta - Tipo Carne: Manzo - Cottura: Media
#Dolce: Tiramisù - 30 min - Difficoltà: Media - Zucchero: 200g - Tipo Dolce: Dessert

class Recipe:
    def __init__(self, name: str, preparation_time: float, ingredients: list, difficulty: str):
        self.name = name
        self.preparation_time = preparation_time
        self.ingredients = ingredients
        self.difficulty = difficulty
    
    def __str__(self):
        return f"{self.name} - {self.preparation_time} min - Difficulty: {self.difficulty}"
    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
    
    def get_preparation_time(self):
        return self.preparation_time

    def set_preparation_time(self, preparation_time):
        self.preparation_time = preparation_time
    
    def get_ingredients(self):
        return self.ingredients

    def set_ingredients(self, ingredients):
        self.ingredients = ingredients
    
    def get_difficulty(self):
        return self.difficulty

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
    
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

class FirstCourse(Recipe):
    def __init__(self, name, preparation_time, ingredients, difficulty, type_of_pasta, sauce):
        super().__init__(name, preparation_time, ingredients, difficulty)
        self.type_of_pasta = type_of_pasta
        self.sauce = sauce

    def get_pasta_type(self):
        return self.type_of_pasta

    def set_pasta_type(self, type_of_pasta):
        self.type_of_pasta = type_of_pasta

    def get_sauce(self):
        return self.sauce

    def set_sauce(self, sauce):
        self.sauce = sauce

    def __str__(self):
        return f"FirstCourse: {self.name} - {self.preparation_time} min - Difficulty: {self.difficulty} - Type of pasta : {self.type_of_pasta} - Sauce: {self.sauce}"

class SecondCourse(Recipe):
    def __init__(self, name, preparation_time, ingredients, difficulty, type_of_meat, cooking):
        super().__init__(name, preparation_time, ingredients, difficulty)
        self.type_of_meat = type_of_meat
        self.cooking = cooking

    def get_type_of_meat(self):
        return self.type_of_meat

    def set_type_of_meat(self, type_of_meat):
        self.type_of_meat = type_of_meat

    def get_cooking(self):
        return self.cooking

    def set_cooking(self, cooking):
        self.cooking = cooking
    
    def __str__(self):
        return f"SecondCourse: {self.name} - {self.preparation_time} min - Difficulty: {self.difficulty} - Type of meat : {self.type_of_meat} - Cooking: {self.cooking}"

class Dessert(Recipe):
    def __init__(self, name, preparation_time, ingredients, difficulty, sugar, type_of_dessert):
        super().__init__(name, preparation_time, ingredients, difficulty)
        self.sugar = sugar
        self.type_of_dessert = type_of_dessert

    def get_sugar(self):
        return self.sugar

    def set_sugar(self, sugar):
        self.sugar = sugar

    def get_dessert_type(self):
        return self.type_of_dessert

    def set_dessert_type(self, type_of_dessert):
        self.type_of_dessert = type_of_dessert
    
    def __str__(self):
        return f"Dessert: {self.name} - {self.preparation_time} min - Difficulty: {self.difficulty} - Sugar : {self.sugar} - Type of dessert: {self.type_of_dessert}"

def calculate_total_time(recipes):
    total_time = 0
    for recipe in recipes:
        total_time += recipe.preparation_time
    return total_time

def check_ingredients(recipes, available_ingredients):
    possible_recipes = []
    for recipe in recipes:
        can_make = True
        for ingredient in recipe.ingredients:
            if ingredient not in available_ingredients:
                can_make = False
                break
        if can_make:
            possible_recipes.append(recipe)
    return possible_recipes

def print_recipes(recipes):
    for recipe in recipes:
        print(recipe)

first_course = FirstCourse("Spaghetti alla Carbonara", 20, ["Spaghetti", "Eggs", "Bacon"], "Medium", "Spaghetti", "Carbonara")
second_course = SecondCourse("Bistecca alla Fiorentina", 30, ["Steak", "Salt", "Pepper"], "High", "Beef", "Medium")
dessert = Dessert("Tiramisù", 30, ["Mascarpone", "Coffee", "Ladyfingers"], "Medium", 200, "Dessert")

recipes = [first_course, second_course, dessert]
possible_recipes = check_ingredients(recipes, ["Spaghetti", "Eggs", "Bacon", "Steak", "Salt", "Pepper", "Mascarpone", "Coffee", "Ladyfingers", "Bread", "Tomato", "Basil"])
print(f"Recipes that can be prepared: {len(possible_recipes)}")

print("\nRecipe information:")
print_recipes(recipes)