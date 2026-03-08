class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, holder_name, account_number, balance=0, min_balance=0):
        self.holder_name = holder_name
        self.account_number = account_number
        self.__balance = balance
        self.min_balance = min_balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        self.transaction_history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.__balance - amount < self.min_balance:
            raise InsufficientFundsError("Insufficient funds or minimum balance violation.")
        self.__balance -= amount
        self.transaction_history.append(f"Withdrew {amount}")

    def transfer(self, other_account, amount):
        if not isinstance(other_account, BankAccount):
            raise TypeError("Transfer target must be a BankAccount.")
        self.withdraw(amount)
        other_account.deposit(amount)
        self.transaction_history.append(
            f"Transferred {amount} to {other_account.account_number}"
        )

    @property
    def balance(self):
        return self.__balance

    def show_history(self):
        print(f"\nTransaction History for {self.holder_name}:")
        for t in self.transaction_history:
            print("-", t)


a1 = BankAccount("Sahil", "ACC101", 5000, 1000)
a2 = BankAccount("Rahul", "ACC102", 3000, 500)

a1.deposit(2000)
a1.withdraw(1000)
a1.transfer(a2, 1500)

print(a1.holder_name, "Balance:", a1.balance)
print(a2.holder_name, "Balance:", a2.balance)

a1.show_history()
a2.show_history()
