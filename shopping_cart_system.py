class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class CartItem:
    def __init__(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        self.product = product
        self.quantity = quantity

    def total_price(self):
        return self.product.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        for item in self.items:
            if item.product.product_id == product.product_id:
                item.quantity += quantity
                return
        self.items.append(CartItem(product, quantity))

    def remove_item(self, product_id):
        self.items = [item for item in self.items if item.product.product_id != product_id]

    def calculate_total(self):
        return sum(item.total_price() for item in self.items)

    def apply_discount(self, percent):
        total = self.calculate_total()
        return total - (total * percent / 100)

    def show_cart(self):
        print("\nShopping Cart:")
        for item in self.items:
            print(
                f"{item.product.name} - Price: {item.product.price}, "
                f"Qty: {item.quantity}, Total: {item.total_price()}"
            )
        print("Grand Total:", self.calculate_total())


p1 = Product(101, "Laptop", 60000)
p2 = Product(102, "Mouse", 1000)
p3 = Product(103, "Keyboard", 2000)

cart = ShoppingCart()
cart.add_item(p1, 1)
cart.add_item(p2, 2)
cart.add_item(p3, 1)

cart.show_cart()
print("After 10% Discount:", cart.apply_discount(10))
