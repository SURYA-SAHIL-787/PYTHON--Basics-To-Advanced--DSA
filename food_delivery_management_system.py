class User:
    # BASE USER CLASS
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class Customer(User):
    # CUSTOMER CLASS
    def __init__(self, user_id, name, address):
        super().__init__(user_id, name)
        self.address = address


class DeliveryAgent(User):
    # DELIVERY AGENT CLASS
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.is_available = True

    def assign_order(self):
        self.is_available = False

    def complete_delivery(self):
        self.is_available = True


class MenuItem:
    # MENU ITEM CLASS
    def __init__(self, item_id, item_name, price):
        self.item_id = item_id
        self.item_name = item_name
        self.price = price


class Restaurant:
    # RESTAURANT CLASS
    def __init__(self, restaurant_id, name):
        self.restaurant_id = restaurant_id
        self.name = name
        self.menu = []

    def add_item(self, item):
        self.menu.append(item)

    def show_menu(self):
        print(f"\nMENU OF {self.name}")
        for item in self.menu:
            print(f"{item.item_id} - {item.item_name} - {item.price}")


class Order:
    # ORDER CLASS
    def __init__(self, order_id, customer, restaurant):
        self.order_id = order_id
        self.customer = customer
        self.restaurant = restaurant
        self.items = []
        self.total_amount = 0
        self.status = "PLACED"
        self.delivery_agent = None

    def add_item(self, item):
        self.items.append(item)
        self.total_amount += item.price

    def assign_agent(self, agent):
        self.delivery_agent = agent
        agent.assign_order()
        self.status = "OUT FOR DELIVERY"

    def deliver_order(self):
        if self.delivery_agent:
            self.delivery_agent.complete_delivery()
        self.status = "DELIVERED"

    def display_order(self):
        print(f"\nORDER ID: {self.order_id}")
        print(f"CUSTOMER NAME: {self.customer.name}")
        print(f"RESTAURANT: {self.restaurant.name}")
        print("ITEMS ORDERED:")
        for item in self.items:
            print(f"- {item.item_name} : {item.price}")
        print(f"TOTAL AMOUNT: {self.total_amount}")
        print(f"STATUS: {self.status}")
        if self.delivery_agent:
            print(f"DELIVERY AGENT: {self.delivery_agent.name}")


class FoodDeliverySystem:
    # MAIN FOOD DELIVERY SYSTEM
    def __init__(self):
        self.restaurants = []
        self.delivery_agents = []
        self.orders = []

    def add_restaurant(self, restaurant):
        self.restaurants.append(restaurant)

    def add_delivery_agent(self, agent):
        self.delivery_agents.append(agent)

    def place_order(self, order):
        self.orders.append(order)

    def assign_delivery_agent(self, order):
        for agent in self.delivery_agents:
            if agent.is_available:
                order.assign_agent(agent)
                print(f"AGENT {agent.name} ASSIGNED TO ORDER {order.order_id}")
                return
        print("NO DELIVERY AGENT AVAILABLE")


# MAIN PROGRAM
restaurant = Restaurant(1, "SPICE HUB")
item1 = MenuItem(101, "BIRYANI", 180)
item2 = MenuItem(102, "PIZZA", 250)
item3 = MenuItem(103, "BURGER", 120)

restaurant.add_item(item1)
restaurant.add_item(item2)
restaurant.add_item(item3)

customer = Customer(1, "SAHIL", "CHENNAI")
agent1 = DeliveryAgent(201, "RAJU")
agent2 = DeliveryAgent(202, "KIRAN")

system = FoodDeliverySystem()
system.add_restaurant(restaurant)
system.add_delivery_agent(agent1)
system.add_delivery_agent(agent2)

restaurant.show_menu()

order1 = Order(1, customer, restaurant)
order1.add_item(item1)
order1.add_item(item3)

system.place_order(order1)
system.assign_delivery_agent(order1)

order1.display_order()

order1.deliver_order()
order1.display_order()
