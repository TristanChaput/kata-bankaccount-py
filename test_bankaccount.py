import unittest
from bankaccount import BankAccount


class TestBankAccount(unittest.TestCase):

    def test_withdraw_amount_should_be_75(self):
        self.bankaccount = BankAccount("ABC", 100)
        self.bankaccount.withdraw(25)
        self.assertEqual(self.bankaccount.get_balance(), 75)

if __name__ == '__main__':
    unittest.main()
