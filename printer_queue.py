# File: printer_queue.py
# Real-world application of Queue: Printer Job Management

from collections import deque

class PrinterQueue:
    def __init__(self):
        self.queue = deque()

    def add_job(self, job_name):
        self.queue.append(job_name)
        print(f"Added print job: {job_name}")

    def process_job(self):
        if not self.queue:
            print("No print jobs in queue.")
            return

        job = self.queue.popleft()
        print(f"Printing: {job}")

    def show_queue(self):
        if not self.queue:
            print("Printer queue is empty.")
            return

        print("Pending Print Jobs:")
        for job in self.queue:
            print(job)


def main():
    printer = PrinterQueue()

    printer.add_job("Resume.pdf")
    printer.add_job("Assignment.docx")
    printer.add_job("Invoice.pdf")
    print()

    printer.show_queue()
    print()

    printer.process_job()
    printer.process_job()
    print()

    printer.show_queue()


if __name__ == "__main__":
    main()
