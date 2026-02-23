
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amt):
        self.__balance += amt
    def withdraw(self, amt):
        if amt <= self.__balance: self.__balance -= amt
    def balance(self):
        return self.__balance
acc = BankAccount("Sahil", 100)
acc.deposit(50); acc.withdraw(30)
print("1) Encapsulation:", acc.balance())
class Animal:
    def speak(self):
        return "..."
class Dog(Animal):
    def speak(self):
        return "Woof!"
print("2) Inheritance + Override:", Dog().speak())
class Cat(Animal):
    def speak(self):
        return "Meow!"
def make_it_talk(animal):
    return animal.speak()
print("3) Polymorphism:", make_it_talk(Dog()), make_it_talk(Cat()))
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1
    @classmethod
    def how_many(cls):
        return cls.count
    @staticmethod
    def is_even(n):
        return n % 2 == 0
a = Counter(); b = Counter(); c = Counter()
print("4) classmethod:", Counter.how_many())
print("   staticmethod:", Counter.is_even(10), Counter.is_even(7))
