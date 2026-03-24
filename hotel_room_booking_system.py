# FILE NAME: hotel_room_booking_system.py

class Customer:
    # CUSTOMER CLASS
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name


class Room:
    # ROOM BASE CLASS
    def __init__(self, room_no, price):
        self.room_no = room_no
        self.price = price
        self.is_booked = False

    def book_room(self):
        if not self.is_booked:
            self.is_booked = True
            return True
        return False

    def checkout_room(self):
        self.is_booked = False


class StandardRoom(Room):
    # STANDARD ROOM CLASS
    def __init__(self, room_no):
        super().__init__(room_no, 2000)


class DeluxeRoom(Room):
    # DELUXE ROOM CLASS
    def __init__(self, room_no):
        super().__init__(room_no, 4000)


class Booking:
    # BOOKING CLASS
    def __init__(self, booking_id, customer, room, days):
        self.booking_id = booking_id
        self.customer = customer
        self.room = room
        self.days = days
        self.total_bill = room.price * days

    def display_booking(self):
        print(f"BOOKING ID: {self.booking_id}")
        print(f"CUSTOMER NAME: {self.customer.name}")
        print(f"ROOM NO: {self.room.room_no}")
        print(f"PRICE PER DAY: {self.room.price}")
        print(f"DAYS: {self.days}")
        print(f"TOTAL BILL: {self.total_bill}")
        print("-" * 30)


class Hotel:
    # HOTEL CLASS
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.bookings = []

    def add_room(self, room):
        self.rooms.append(room)

    def show_available_rooms(self):
        print("\nAVAILABLE ROOMS")
        for room in self.rooms:
            if not room.is_booked:
                print(f"ROOM NO: {room.room_no}, PRICE: {room.price}")

    def make_booking(self, customer, room_no, days):
        for room in self.rooms:
            if room.room_no == room_no and not room.is_booked:
                room.book_room()
                booking = Booking(len(self.bookings) + 1, customer, room, days)
                self.bookings.append(booking)
                print("ROOM BOOKED SUCCESSFULLY")
                booking.display_booking()
                return
        print("ROOM NOT AVAILABLE")

    def checkout(self, room_no):
        for room in self.rooms:
            if room.room_no == room_no and room.is_booked:
                room.checkout_room()
                print(f"ROOM {room_no} CHECKED OUT SUCCESSFULLY")
                return
        print("ROOM NOT FOUND OR ALREADY EMPTY")


# MAIN PROGRAM
hotel = Hotel("STAR HOTEL")

hotel.add_room(StandardRoom(101))
hotel.add_room(StandardRoom(102))
hotel.add_room(DeluxeRoom(201))
hotel.add_room(DeluxeRoom(202))

customer1 = Customer(1, "SAHIL")
customer2 = Customer(2, "RAHUL")

hotel.show_available_rooms()

hotel.make_booking(customer1, 101, 3)
hotel.make_booking(customer2, 201, 2)

hotel.show_available_rooms()

hotel.checkout(101)
hotel.show_available_rooms()
