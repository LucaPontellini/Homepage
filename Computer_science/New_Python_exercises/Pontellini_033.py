import datetime

class Order:
    def __init__(self, order_number: str, date_time: datetime.datetime, status: str, items: list):
        self._order_number = order_number
        self._date_time = date_time
        self._status = status
        self._items = items

    def get_order_number(self):
        return self._order_number

    def get_date_time(self):
        return self._date_time

    def get_status(self):
        return self._status

    def set_status(self, status):
        self._status = status

    def add_item(self, item):
        self._items.append(item)

    def remove_item(self, item):
        self._items.remove(item)

    def calculate_total(self):
        total = 0
        for item in self._items:
            total += item.get_price()
        return total

class MenuItem:
    def __init__(self, code: str, name: str, price: float, preparation_time: int, allergens: list, available: bool):
        self._code = code
        self._name = name
        self._price = price
        self._preparation_time = preparation_time
        self._allergens = allergens
        self._available = available

    def get_code(self):
        return self._code

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_preparation_time(self):
        return self._preparation_time

    def get_allergens(self):
        return self._allergens

    def is_available(self):
        return self._available

    def set_available(self, state):
        self._available = state

    def to_string(self):
        return f"{self._code} - {self._name} - {self._price}€ - {self._preparation_time} minutes"

class FirstCourse(MenuItem):
    def __init__(self, code: str, name: str, price: float, preparation_time: int, allergens: list, available: bool, pasta_type: str, vegetarian: bool):
        super().__init__(code, name, price, preparation_time, allergens, available)
        self._pasta_type = pasta_type
        self._vegetarian = vegetarian

    def get_pasta_type(self):
        return self._pasta_type
    
    def set_pasta_type(self, pasta_type):
        self._pasta_type = pasta_type

    def is_vegetarian(self):
        return self._vegetarian
    
class SecondCourse(MenuItem):
    def __init__(self, code: str, name: str, price: float, preparation_time: int, allergens: list, available: bool, default_cooking: str):
        super().__init__(code, name, price, preparation_time, allergens, available)
        self._default_cooking = default_cooking

    def get_default_cooking(self):
        return self._default_cooking
    
    def set_default_cooking(self, cooking):
        self._default_cooking = cooking

class Table:
    def __init__(self, number: int, seats: int, status: str):
        self._number = number
        self._seats = seats
        self._status = status
        self._orders = []

    def get_number(self):
        return self._number
    
    def get_seats(self):
        return self._seats
    
    def is_free(self):
        return self._status == "free"

    def set_status(self, status):
        self._status = status

    def add_order(self, order):
        self._orders.append(order)

    def remove_order(self, order):
        self._orders.remove(order)

    def get_active_orders(self):
        return self._orders

# Creazione elementi del menu
first = FirstCourse("P1", "Spaghetti Carbonara", 12.0, 15, ["eggs", "gluten"], True, "spaghetti", False)
second = SecondCourse("S1", "Steak", 18.0, 20, [], True, "medium")

# Creazione del tavolo e dell'ordine
table = Table(1, 4, "free")
order = Order("ORD1", datetime.datetime.now(), "pending", [])

# Aggiunta elementi all'ordine
order.add_item(first)
order.add_item(second)

# Collegamento dell'ordine al tavolo
table.add_order(order)
table.set_status("occupied")

# Calcoli
print(f"Order total: {order.calculate_total()}€")  # Output: Order total: 30.0€

# Gestione stato ordine
order.set_status("in preparation")
print(f"Order status: {order.get_status()}")  # Output: Order status: in preparation

# Informazioni tavolo
print(f"Table number: {table.get_number()}")
print(f"Table status: {'free' if table.is_free() else 'occupied'}")
print(f"Active orders: {len(table.get_active_orders())}")