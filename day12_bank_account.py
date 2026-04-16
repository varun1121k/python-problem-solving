# Day 12 - Bank Account

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def display(self):
        print(self.owner, "Balance:", self.balance)


acc = BankAccount("Varun", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.display()
