# File: ticket_counter_queue.py
# Real-world application of Queue: People waiting at a ticket counter

from collections import deque

class TicketCounter:
    def __init__(self):
        self.queue = deque()

    def join_queue(self, person):
        self.queue.append(person)
        print(f"{person} joined the queue.")

    def serve_person(self):
        if not self.queue:
            print("No one is waiting.")
            return

        person = self.queue.popleft()
        print(f"Serving ticket to: {person}")

    def show_queue(self):
        if not self.queue:
            print("Queue is empty.")
            return

        print("People in queue:")
        for person in self.queue:
            print(person)


def main():
    counter = TicketCounter()

    counter.join_queue("Sahil")
    counter.join_queue("Rahul")
    counter.join_queue("Anjali")
    print()

    counter.show_queue()
    print()

    counter.serve_person()
    counter.serve_person()
    print()

    counter.show_queue()


if __name__ == "__main__":
    main()
