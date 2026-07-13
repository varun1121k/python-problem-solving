class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Invalid amount"

        self.__balance += amount
        return "Amount deposited successfully"

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid amount"

        if amount > self.__balance:
            return "Insufficient balance"

        self.__balance -= amount
        return "Withdrawal successful"

    def get_balance(self):
        return self.__balance


# Test
account = BankAccount(1000)

print(account.deposit(500))
print(account.withdraw(200))
print("Current Balance:", account.get_balance())

print(account.deposit(-100))
print(account.withdraw(5000))
print("Current Balance:", account.get_balance())
