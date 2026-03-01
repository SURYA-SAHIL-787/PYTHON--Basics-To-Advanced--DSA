from abc import ABC, abstractmethod

class Vehicle(ABC):
    vehicle_count = 0

    def __init__(self, brand, rent):
        self.brand = brand
        self.__rent = rent
        Vehicle.vehicle_count += 1

    def get_rent(self):
        return self.__rent

    @abstractmethod
    def vehicle_type(self):
        pass

class Car(Vehicle):
    def vehicle_type(self):
        return f"{self.brand} Car rent is {self.get_rent()} per day"

class Bike(Vehicle):
    def vehicle_type(self):
        return f"{self.brand} Bike rent is {self.get_rent()} per day"

class Bus(Vehicle):
    def vehicle_type(self):
        return f"{self.brand} Bus rent is {self.get_rent()} per day"

v1 = Car("Toyota", 3000)
v2 = Bike("Yamaha", 800)
v3 = Bus("Volvo", 7000)

for v in [v1, v2, v3]:
    print(v.vehicle_type())

print("Total Vehicles:", Vehicle.vehicle_count)
