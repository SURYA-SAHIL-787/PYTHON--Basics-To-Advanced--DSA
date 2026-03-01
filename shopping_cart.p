from abc import ABC, abstractmethod

class Product(ABC):
    product_count = 0

    def __init__(self, name, price):
        self.name = name
        self.__price = price
        Product.product_count += 1

    def get_price(self):
        return self.__price

    @abstractmethod
    def display(self):
        pass

class Electronics(Product):
    def display(self):
        return f"Electronic Product: {self.name}, Price: {self.get_price()}"

class Clothing(Product):
    def display(self):
        return f"Clothing Product: {self.name}, Price: {self.get_price()}"

class Grocery(Product):
    def display(self):
        return f"Grocery Product: {self.name}, Price: {self.get_price()}"

products = [Electronics("Laptop", 55000), Clothing("Shirt", 1200), Grocery("Rice", 900)]

for p in products:
    print(p.display())

print("Total Products:", Product.product_count)
