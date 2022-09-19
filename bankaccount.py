class BankAccount:

    def __init__(self, iban, balance):
        self._iban = iban
        self._balance = balance

    def withdraw(self, amount):
        self._balance -= amount

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance
