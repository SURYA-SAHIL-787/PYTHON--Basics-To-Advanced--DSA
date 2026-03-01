from abc import ABC, abstractmethod

class Room(ABC):
    room_count = 0

    def __init__(self, room_number, price):
        self.room_number = room_number
        self.__price = price
        Room.room_count += 1

    def get_price(self):
        return self.__price

    @abstractmethod
    def room_type(self):
        pass

class StandardRoom(Room):
    def room_type(self):
        return f"Room {self.room_number} is a Standard Room with price {self.get_price()}"

class DeluxeRoom(Room):
    def room_type(self):
        return f"Room {self.room_number} is a Deluxe Room with price {self.get_price()}"

class SuiteRoom(Room):
    def room_type(self):
        return f"Room {self.room_number} is a Suite Room with price {self.get_price()}"

rooms = [StandardRoom(101, 2000), DeluxeRoom(102, 4000), SuiteRoom(103, 7000)]

for room in rooms:
    print(room.room_type())

print("Total Rooms:", Room.room_count)
