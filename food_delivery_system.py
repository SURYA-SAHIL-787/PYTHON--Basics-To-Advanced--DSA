from abc import ABC, abstractmethod

class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = {}

    def add_item(self, item_name, price):
        self.menu[item_name] = price

    def show_menu(self):
        print(f"Menu of {self.name}:")
        for item, price in self.menu.items():
            print(item, ":", price)


class Order(ABC):
    def __init__(self, user, restaurant):
        self.user = user
        self.restaurant = restaurant
        self.items = []

    def add_item(self, item_name):
        if item_name in self.restaurant.menu:
            self.items.append(item_name)

    @abstractmethod
    def calculate_total(self):
        pass


class RegularOrder(Order):
    def calculate_total(self):
        return sum(self.restaurant.menu[item] for item in self.items)


class PremiumOrder(Order):
    def calculate_total(self):
        total = sum(self.restaurant.menu[item] for item in self.items)
        return total * 0.9


# Driver Code
u1 = User("Sahil", "Chennai")
r1 = Restaurant("Pizza Hub")
r1.add_item("Pizza", 250)
r1.add_item("Burger", 120)
r1.add_item("Pasta", 180)

order1 = RegularOrder(u1, r1)
order1.add_item("Pizza")
order1.add_item("Burger")

order2 = PremiumOrder(u1, r1)
order2.add_item("Pizza")
order2.add_item("Pasta")

print("Regular Order Total:", order1.calculate_total())
print("Premium Order Total:", order2.calculate_total())
