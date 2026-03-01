from abc import ABC, abstractmethod

class Payment(ABC):
    total_payments = 0

    def __init__(self, amount):
        self.__amount = amount
        Payment.total_payments += 1

    def get_amount(self):
        return self.__amount

    @abstractmethod
    def pay(self):
        pass

class CreditCardPayment(Payment):
    def pay(self):
        return f"Paid {self.get_amount()} using Credit Card"

class UpiPayment(Payment):
    def pay(self):
        return f"Paid {self.get_amount()} using UPI"

class WalletPayment(Payment):
    def pay(self):
        return f"Paid {self.get_amount()} using Wallet"

class PaymentProcessor:
    def process(self, payment):
        print(payment.pay())

p1 = CreditCardPayment(2000)
p2 = UpiPayment(1500)
p3 = WalletPayment(500)

processor = PaymentProcessor()
processor.process(p1)
processor.process(p2)
processor.process(p3)

print("Total payments made:", Payment.total_payments)
