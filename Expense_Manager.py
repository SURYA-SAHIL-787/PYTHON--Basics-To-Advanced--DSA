import json
import statistics

class ExpenseManager:
    def __init__(self, filename):
        self.filename = filename
        try:
            with open(filename, "r") as f:
                self.expenses = json.load(f)
        except:
            self.expenses = []

    def add_expense(self, category, amount):
        self.expenses.append({"category": category, "amount": amount})
        self.save()

    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.expenses, f, indent=4)

    def total(self):
        return sum(e["amount"] for e in self.expenses)

    def average(self):
        amounts = [e["amount"] for e in self.expenses]
        return statistics.mean(amounts) if amounts else 0

    def highest(self):
        return max(self.expenses, key=lambda x: x["amount"]) if self.expenses else None

    def show_all(self):
        for e in sorted(self.expenses, key=lambda x: x["amount"], reverse=True):
            print(e["category"], e["amount"])

manager = ExpenseManager("expenses.json")

while True:
    print("\n1.Add 2.Show 3.Total 4.Avg 5.Highest 6.Exit")
    choice = input("Choice: ")

    if choice == "1":
        cat = input("Category: ")
        amt = float(input("Amount: "))
        manager.add_expense(cat, amt)
    elif choice == "2":
        manager.show_all()
    elif choice == "3":
        print("Total:", manager.total())
    elif choice == "4":
        print("Average:", manager.average())
    elif choice == "5":
        print("Highest:", manager.highest())
    elif choice == "6":
        break
    else:
        print("Invalid choice")
