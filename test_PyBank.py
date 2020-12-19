from unittest import TestCase
import PyBank
import Currencies

BANK = PyBank.PyBank.get_instance()
C = Currencies.Currencies.get_instance()


class TestPyBank(TestCase):
    """
    Contains the test cases for this assignment that are run from bottom to top.
    """

    def test_get_balance(self):
        BANK.create_account("1", 100)
        balances = [BANK.get_balance("1"), BANK.get_balance("10")]
        self.assertEqual(balances, [100, None])
        BANK.clear_accounts()

    def test_deposit_funds(self):
        BANK.create_account("2", 100)
        BANK.deposit_funds("2", 100, C.get_currency("1"))
        self.assertEqual(BANK.get_balance("2"), 200)
        BANK.deposit_funds("2", 100, C.get_currency("2"))
        self.assertEqual(BANK.get_balance("2"), 350)
        BANK.deposit_funds("2", 100, C.get_currency("3"))
        self.assertEqual(BANK.get_balance("2"), 550)
        BANK.deposit_funds("2", -100, C.get_currency("1"))
        self.assertEqual(BANK.get_balance("2"), 550)
        BANK.clear_accounts()

    def test_withdraw_funds(self):
        BANK.create_account("3", 550)
        BANK.withdraw_funds("3", 100, C.get_currency("1"))
        self.assertEqual(BANK.get_balance("3"), 450)
        BANK.withdraw_funds("3", 100, C.get_currency("2"))
        self.assertEqual(BANK.get_balance("3"), 300)
        BANK.withdraw_funds("3", 100, C.get_currency("3"))
        self.assertEqual(BANK.get_balance("3"), 100)
        BANK.withdraw_funds("3", 101, C.get_currency("1"))
        self.assertEqual(BANK.get_balance("3"), 100)
        BANK.withdraw_funds("3", -100, C.get_currency("1"))
        self.assertEqual(BANK.get_balance("3"), 100)
        BANK.clear_accounts()

    def test_transfer_funds(self):
        BANK.create_account("4", 100)
        BANK.create_account("5", 100)
        BANK.transfer_funds("5", "4", 10)
        self.assertEqual(BANK.get_balance("4"), 90)
        self.assertEqual(BANK.get_balance("5"), 110)
        BANK.transfer_funds("5", "4", 91)
        self.assertEqual(BANK.get_balance("4"), 90)
        self.assertEqual(BANK.get_balance("5"), 110)
        BANK.transfer_funds("5", "5", -10)
        self.assertEqual(BANK.get_balance("4"), 90)
        self.assertEqual(BANK.get_balance("5"), 110)
        BANK.clear_accounts()

    def test_check_amount_validity(self):
        self.assertFalse(PyBank.check_amount_validity("this is not valid"))
        self.assertFalse(PyBank.check_amount_validity("-123"))
        self.assertTrue(PyBank.check_amount_validity("123"))
        self.assertTrue(PyBank.check_amount_validity("0"))
        BANK.clear_accounts()

    def test_create_account(self):
        BANK.create_account("6", 100)
        self.assertEqual(BANK.get_accounts(), 1)
        self.assertEqual(BANK.get_account("6").get_account_number(), "6")
        BANK.create_account("6", 100)
        self.assertEqual(BANK.get_accounts(), 1)
        BANK.create_account("7", -100)
        self.assertEqual(BANK.get_accounts(), 1)
        BANK.clear_accounts()

    def test_get_account(self):
        BANK.create_account("8", 100)
        self.assertEqual(BANK.get_account("8").get_balance(), 100)
        self.assertEqual(BANK.get_account("9"), None)
        BANK.clear_accounts()

    def test_get_accounts(self):
        BANK.create_account("321", 100)
        self.assertEqual(BANK.get_accounts(), 1)
        BANK.clear_accounts()

    def test_clear_accounts(self):
        BANK.create_account("3543", 300)
        BANK.clear_accounts()
        self.assertEqual(BANK.get_accounts(), 0)
        BANK.clear_accounts()

    def test_case_a(self):
        BANK.create_account("0808", 1000.00)
        BANK.deposit_funds("0808", 500.00, C.get_currency("2"))
        BANK.withdraw_funds("0808", 100.00, C.get_currency("1"))
        self.assertEqual(BANK.get_balance("0808"), 1650.00)
        BANK.clear_accounts()

    def test_case_b(self):
        BANK.create_account("0903", 100.00)
        BANK.create_account("0875", 6000.00)
        BANK.withdraw_funds("0875", 700, C.get_currency("2"))
        BANK.deposit_funds("0903", 2500.00, C.get_currency("3"))
        BANK.transfer_funds("0875", "0903", 1100.00)
        self.assertEqual(BANK.get_balance("0903"), 4000.00)
        self.assertEqual(BANK.get_balance("0875"), 6050.00)
        BANK.clear_accounts()

    def test_case_c(self):
        BANK.create_account("8888", 100.00)
        BANK.create_account("7777", 6000.00)
        BANK.withdraw_funds("8888", 50, C.get_currency("3"))
        BANK.transfer_funds("8888", "7777", 6000)
        BANK.withdraw_funds("8888", 4000, C.get_currency("2"))
        self.assertEqual(BANK.get_balance("8888"), 0)
        self.assertEqual(BANK.get_balance("7777"), 0)
        BANK.clear_accounts()

    def test_case_d(self):
        BANK.create_account("1234", 0)
        BANK.create_account("0", 2000)
        BANK.transfer_funds("1234", "0", 2000)
        self.assertEqual(BANK.get_balance("1234"), 2000)
        self.assertEqual(BANK.get_balance("0"), 0)
        BANK.create_account("9999", 12000)
        BANK.withdraw_funds("9999", 3000, C.get_currency("2"))
        self.assertEqual(BANK.get_balance("9999"), 7500)
        BANK.clear_accounts()
