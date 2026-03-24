class Passenger:
    # PASSENGER CLASS
    def __init__(self, passenger_id, name, age):
        self.passenger_id = passenger_id
        self.name = name
        self.age = age


class Train:
    # TRAIN CLASS
    def __init__(self, train_no, train_name, total_seats, fare):
        self.train_no = train_no
        self.train_name = train_name
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.fare = fare
        self.booked_tickets = []
        self.waiting_list = []

    def book_ticket(self, passenger):
        if self.available_seats > 0:
            ticket = Ticket(len(self.booked_tickets) + 1, passenger, self, "CONFIRMED")
            self.booked_tickets.append(ticket)
            self.available_seats -= 1
            return ticket
        else:
            ticket = Ticket(len(self.booked_tickets) + len(self.waiting_list) + 1, passenger, self, "WAITING")
            self.waiting_list.append(ticket)
            return ticket

    def cancel_ticket(self, ticket_id):
        for ticket in self.booked_tickets:
            if ticket.ticket_id == ticket_id:
                self.booked_tickets.remove(ticket)
                self.available_seats += 1
                print(f"TICKET {ticket_id} CANCELLED SUCCESSFULLY")

                if self.waiting_list:
                    next_ticket = self.waiting_list.pop(0)
                    next_ticket.status = "CONFIRMED"
                    self.booked_tickets.append(next_ticket)
                    self.available_seats -= 1
                    print(f"WAITING TICKET {next_ticket.ticket_id} MOVED TO CONFIRMED")
                return

        for ticket in self.waiting_list:
            if ticket.ticket_id == ticket_id:
                self.waiting_list.remove(ticket)
                print(f"WAITING TICKET {ticket_id} CANCELLED SUCCESSFULLY")
                return

        print("TICKET NOT FOUND")

    def display_status(self):
        print(f"\nTRAIN NO: {self.train_no}")
        print(f"TRAIN NAME: {self.train_name}")
        print(f"TOTAL SEATS: {self.total_seats}")
        print(f"AVAILABLE SEATS: {self.available_seats}")
        print(f"CONFIRMED TICKETS: {len(self.booked_tickets)}")
        print(f"WAITING TICKETS: {len(self.waiting_list)}")


class Ticket:
    # TICKET CLASS
    def __init__(self, ticket_id, passenger, train, status):
        self.ticket_id = ticket_id
        self.passenger = passenger
        self.train = train
        self.status = status

    def display_ticket(self):
        print(f"TICKET ID: {self.ticket_id}")
        print(f"PASSENGER NAME: {self.passenger.name}")
        print(f"AGE: {self.passenger.age}")
        print(f"TRAIN: {self.train.train_name}")
        print(f"FARE: {self.train.fare}")
        print(f"STATUS: {self.status}")
        print("-" * 30)


# MAIN PROGRAM
train1 = Train(12627, "KARNATAKA EXPRESS", 2, 750)

passenger1 = Passenger(1, "SAHIL", 19)
passenger2 = Passenger(2, "ARUN", 22)
passenger3 = Passenger(3, "MEENA", 21)

ticket1 = train1.book_ticket(passenger1)
ticket2 = train1.book_ticket(passenger2)
ticket3 = train1.book_ticket(passenger3)

ticket1.display_ticket()
ticket2.display_ticket()
ticket3.display_ticket()

train1.display_status()

train1.cancel_ticket(1)
train1.display_status()

for ticket in train1.booked_tickets:
    ticket.display_ticket()
