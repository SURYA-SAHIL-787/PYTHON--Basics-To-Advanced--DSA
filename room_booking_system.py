from abc import ABC, abstractmethod


class Room(ABC):
    def __init__(self, room_number, price_per_night):
        self.room_number = room_number
        self.price_per_night = price_per_night
        self.is_booked = False

    @abstractmethod
    def calculate_bill(self, nights):
        pass

    def book_room(self):
        if self.is_booked:
            raise Exception(f"Room {self.room_number} is already booked.")
        self.is_booked = True

    def checkout_room(self):
        if not self.is_booked:
            raise Exception(f"Room {self.room_number} is not currently booked.")
        self.is_booked = False

    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"Room {self.room_number} - {self.__class__.__name__} - {status}"


class StandardRoom(Room):
    def calculate_bill(self, nights):
        return self.price_per_night * nights


class DeluxeRoom(Room):
    def calculate_bill(self, nights):
        extra_service_charge = 1000
        return (self.price_per_night * nights) + extra_service_charge


class SuiteRoom(Room):
    def calculate_bill(self, nights):
        luxury_tax = 2000
        return (self.price_per_night * nights) + luxury_tax


class Guest:
    def __init__(self, guest_id, name):
        self.guest_id = guest_id
        self.name = name
        self.bookings = []

    def book(self, room, nights):
        room.book_room()
        bill = room.calculate_bill(nights)
        self.bookings.append((room, nights, bill))
        return bill

    def checkout(self, room):
        for booking in self.bookings:
            if booking[0] == room:
                room.checkout_room()
                self.bookings.remove(booking)
                return
        raise Exception(f"{self.name} has no booking for Room {room.room_number}.")


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = {}
        self.guests = {}

    def add_room(self, room):
        self.rooms[room.room_number] = room

    def add_guest(self, guest):
        self.guests[guest.guest_id] = guest

    def show_available_rooms(self):
        print(f"Available Rooms in {self.name}:")
        for room in self.rooms.values():
            if not room.is_booked:
                print(room)


if __name__ == "__main__":
    hotel = Hotel("Grand Palace")

    r1 = StandardRoom(101, 2000)
    r2 = DeluxeRoom(102, 4000)
    r3 = SuiteRoom(103, 7000)

    g1 = Guest(1, "Sahil")

    hotel.add_room(r1)
    hotel.add_room(r2)
    hotel.add_room(r3)
    hotel.add_guest(g1)

    hotel.show_available_rooms()
    print()

    total_bill = g1.book(r3, 2)
    print(f"{g1.name} booked Room {r3.room_number} for 2 nights. Total bill = {total_bill}")
    print()

    hotel.show_available_rooms()
    print()

    g1.checkout(r3)
    print(f"{g1.name} checked out from Room {r3.room_number}")
    print()

    hotel.show_available_rooms()
