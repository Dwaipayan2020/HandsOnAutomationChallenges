"""Create a class BankAccount, which contains attributes
balance and name, and methods deposit() and withdraw(),
to add and deposit some money in account.
the balance should be set to 0 in the constructor,
and withdrawal should be allowed only if sufficient balance is there.
Also overload the str method to allow printing the details
directly."""


class BankAccount:
    def __init__(self, name):
        self.balance = 0
        self.name = name

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        print(f'{self.name} has deposited {amount}$ in current account.')

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f'{self.name} has withdrawn {amount}$ from current account.')

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f'user -> {self.name} has amount {self.balance}$ left in his/her account.'


bank_acc = BankAccount('Rohan')
bank_acc.deposit(5000)
bank_acc.withdraw(2000)
print(bank_acc)
