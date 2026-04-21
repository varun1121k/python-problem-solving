# Day 13 - Bank Account (Encapsulation)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


acc = BankAccount("Varun", 1000)
acc.deposit(500)
acc.withdraw(200)
print("Balance:", acc.get_balance())
