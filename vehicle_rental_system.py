from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, vehicle_id, brand, model, rent_per_day):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rent_per_day = rent_per_day
        self.is_available = True

    @abstractmethod
    def calculate_rent(self, days):
        pass

    def rent_vehicle(self):
        if not self.is_available:
            raise Exception(f"{self.brand} {self.model} is already rented.")
        self.is_available = False

    def return_vehicle(self):
        if self.is_available:
            raise Exception(f"{self.brand} {self.model} was not rented.")
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Rented"
        return f"[{self.vehicle_id}] {self.brand} {self.model} - {status}"


class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, rent_per_day, seats):
        super().__init__(vehicle_id, brand, model, rent_per_day)
        self.seats = seats

    def calculate_rent(self, days):
        return self.rent_per_day * days


class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, rent_per_day, engine_cc):
        super().__init__(vehicle_id, brand, model, rent_per_day)
        self.engine_cc = engine_cc

    def calculate_rent(self, days):
        insurance_charge = 100
        return (self.rent_per_day * days) + insurance_charge


class Truck(Vehicle):
    def __init__(self, vehicle_id, brand, model, rent_per_day, load_capacity):
        super().__init__(vehicle_id, brand, model, rent_per_day)
        self.load_capacity = load_capacity

    def calculate_rent(self, days):
        service_fee = 500
        return (self.rent_per_day * days) + service_fee


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.rented_vehicles = []

    def rent(self, vehicle, days):
        vehicle.rent_vehicle()
        cost = vehicle.calculate_rent(days)
        self.rented_vehicles.append((vehicle, days, cost))
        return cost

    def return_rented_vehicle(self, vehicle):
        for record in self.rented_vehicles:
            if record[0] == vehicle:
                vehicle.return_vehicle()
                self.rented_vehicles.remove(record)
                return
        raise Exception(f"{self.name} did not rent this vehicle.")

    def __str__(self):
        return f"Customer[{self.customer_id}] {self.name}"


class RentalSystem:
    def __init__(self):
        self.vehicles = {}
        self.customers = {}

    def add_vehicle(self, vehicle):
        self.vehicles[vehicle.vehicle_id] = vehicle

    def add_customer(self, customer):
        self.customers[customer.customer_id] = customer

    def show_available_vehicles(self):
        print("Available Vehicles:")
        for vehicle in self.vehicles.values():
            if vehicle.is_available:
                print(vehicle)


if __name__ == "__main__":
    system = RentalSystem()

    v1 = Car(1, "Toyota", "Innova", 2500, 7)
    v2 = Bike(2, "Yamaha", "R15", 800, 155)
    v3 = Truck(3, "Tata", "Ace", 4000, 1000)

    c1 = Customer(101, "Sahil")

    system.add_vehicle(v1)
    system.add_vehicle(v2)
    system.add_vehicle(v3)
    system.add_customer(c1)

    system.show_available_vehicles()
    print()

    rent_cost = c1.rent(v2, 3)
    print(f"{c1.name} rented {v2.brand} {v2.model} for 3 days. Total cost = {rent_cost}")
    print()

    system.show_available_vehicles()
    print()

    c1.return_rented_vehicle(v2)
    print(f"{c1.name} returned {v2.brand} {v2.model}")
    print()

    system.show_available_vehicles()
