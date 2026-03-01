import unittest
from bankaccount import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount(100)  # starting balance of 100

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

    def test_deposit(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    def test_withdraw(self):
        self.account.withdraw(30)
        self.assertEqual(self.account.get_balance(), 70)

    def test_withdraw_more_than_balance_raises_exception(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    def test_multiple_transactions(self):
        self.account.deposit(50)     # 150
        self.account.withdraw(20)    # 130
        self.account.deposit(70)     # 200
        self.account.withdraw(100)   # 100
        self.assertEqual(self.account.get_balance(), 100)


if __name__ == "__main__":
    unittest.main()