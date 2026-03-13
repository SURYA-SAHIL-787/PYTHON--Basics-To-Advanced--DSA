class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name


class Order:
    order_count = 0

    def __init__(self, customer):
        self.customer = customer
        self.products = []
        self.status = "Placed"
        Order.order_count += 1
        self.order_id = Order.order_count

    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        return sum(product.price for product in self.products)

    def update_status(self, new_status):
        self.status = new_status

    def display_order(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.customer.name}")
        print("Products:")
        for product in self.products:
            print(f"- {product.name}: {product.price}")
        print("Total:", self.calculate_total())
        print("Status:", self.status)


# Driver Code
c1 = Customer(1, "Sahil")
p1 = Product(101, "Laptop", 65000)
p2 = Product(102, "Mouse", 1200)
p3 = Product(103, "Keyboard", 2500)

order = Order(c1)
order.add_product(p1)
order.add_product(p2)
order.add_product(p3)
order.update_status("Shipped")
order.display_order()
