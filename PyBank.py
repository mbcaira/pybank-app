import Currencies
import Account


def check_amount_validity(amount: str) -> bool:
    """
    Static method to check whether a given amount is valid for a monetary value
    (i.e. cannot be negative or contain letters).

    :param amount: String value that will be checked for monetary validity.
    :return: True if valid, False otherwise.
    """
    try:
        amount = float(amount)
        if amount < 0:
            print("Error, inputs cannot be negative! Please try again.\n")
            return False
        return True
    except ValueError:
        print("Sorry, there were illegal characters in that request! "
              "Please try again.\n")
        return False


class PyBank:
    """
    PyBank class that performs bank functionality, such ass withdrawing, depositing, etc.
    """
    __instance = None
    _accounts = []  # Keeps track of active accounts.

    @staticmethod
    def get_instance():
        """
        Returns the instance of PyBank.

        :return: Instance of PyBank.
        """
        if PyBank.__instance is None:
            PyBank()
        return PyBank.__instance

    def __init__(self):
        """
        Singleton constructor for PyBank.
        """
        if PyBank.__instance is None:
            PyBank.__instance = self

    def get_account(self, account_number: str):
        """
        Retrieves an account object given the account number from the list of active accounts.

        :param account_number: String value of the desired account's account number.
        :return: If the account is found its account object is returned, otherwise None is returned.
        """
        for account in self._accounts:
            if account.get_account_number() == account_number:
                return account
        return None

    def get_accounts(self) -> int:
        """
        Gets the number of active accounts.

        :return: Returns an integer representing the number of active accounts.
        """
        return len(self._accounts)

    def clear_accounts(self) -> None:
        """
        Deletes all active accounts.

        :return: None
        """
        self._accounts.clear()

    def create_account(self, account_number: str, balance: float) -> None:
        """
        Creates an Account and adds it to the PyBank's list of active accounts.

        :param account_number: String value to denote account number.
        :param balance: String float representing the initial account balance.
        :return: None
        """
        if check_amount_validity(balance):
                if not self.get_account(account_number):
                    self._accounts.append(Account.Account(account_number, float(balance)))
                else:
                    print("Error, account with this number already exists, please try again!")

    def get_balance(self, account_number: str) -> float:
        """
        Returns the balance of an account given its account number by performing a look-up.

        :param account_number: String value of the desired account's account number.
        :return: Float representation of the account's balance if it is  found, otherwise returns None.
        """
        account = self.get_account(account_number)
        if account is None:
            print("Error, account does not exist.\n")
            return
        return account.get_balance()

    def deposit_funds(self, account_number: str, amount: float, currency: Currencies) -> None:
        """
        Deposits the desired amount of money in the selected currency to the given account number.

        :param account_number: String value of the desired account's account number.
        :param amount: Float (desired) or String (accepted) value of the amount to be deposited.
        :param currency: List of information for the currency in which the deposit is being performed in.
        :return: None.
        """
        if check_amount_validity(amount):
            account = self.get_account(account_number)
            if account is None:
                print("Error, account does not exist.\n")
                return
            old_bal = self.get_balance(account_number)
            account.set_balance(old_bal + float(amount) * currency.get_rate())
            print(f"Account Number: {account.get_account_number()}")
            old_bal = "CA${:,.2f}".format(old_bal)
            print(f"Old balance: {old_bal}")
            deposit = currency.get_prefix() + "{:,.2f}".format(float(amount))
            print(f"Deposit of {deposit} to account {account_number}")
            new_bal = "CA${:,.2f}".format(account.get_balance())
            print(f"New balance: {new_bal}\n")

    def withdraw_funds(self, account_number: str, amount: float, currency: Currencies) -> None:
        """
        Withdraws the desired amount of money in the selected currency from the given account number.

        :param account_number: String value of the desired account's account number.
        :param amount: Float (desired) or String (accepted) value of the amount to be withdrawn.
        :param currency: List of information for the currency in which the withdrawal is being performed in.
        :return: None.
        """
        if check_amount_validity(amount):
            account = self.get_account(account_number)
            if account is None:
                print("Error, account does not exist.\n")
                return
            if account.get_balance() < float(amount) * currency.get_rate():
                print("Error, insufficient balance to withdraw the requested amount!\n")
            else:
                old_bal = self.get_balance(account_number)
                account.set_balance(old_bal - float(amount) * currency.get_rate())
                print(f"Account Number: {account.get_account_number()}")
                old_bal = "CA${:,.2f}".format(old_bal)
                print(f"Old balance: {old_bal}")
                withdraw = currency.get_prefix() + "{:,.2f}".format(float(amount))
                print(f"Withdrawal of {withdraw} from account {account_number}")
                new_bal = "CA${:,.2f}".format(account.get_balance())
                print(f"New balance: {new_bal}\n")

    def transfer_funds(self, incoming_account_number: str, outgoing_account_number: str, amount: float) -> None:
        """
        Transfers the specified amount from the outgoing account to the incoming account.

        :param incoming_account_number: String value of the desired incoming account's account number.
        :param outgoing_account_number: String value of the desired outgoing account's account number.
        :param amount: Float (desired) or String (accepted) value of the amount to be withdrawn.
        :return: None.
        """
        if check_amount_validity(amount):
            out_acc = self.get_account(outgoing_account_number)
            if out_acc is None:
                print("Error, outgoing account does not exist.\n")
                return
            if out_acc.get_balance() < float(amount):
                print("Error, insufficient balance to transfer the requested amount!\n")
            else:
                inc_acc = self.get_account(incoming_account_number)
                if inc_acc is None:
                    print("Error, account does not exist.\n")
                    return
                inc_acc.set_balance(inc_acc.get_balance() + float(amount))
                out_acc.set_balance(out_acc.get_balance() - float(amount))
                trans_bal = "CA${:,.2f}".format(float(amount))
                print(f"Transfer from {out_acc.get_account_number()} to {inc_acc.get_account_number()} "
                      f"of {trans_bal} completed.")
                print(f"Account Number: {out_acc.get_account_number()}")
                bal_str = "CA${:,.2f}".format(self.get_balance(outgoing_account_number))
                print(f"Balance: {bal_str}\n")
                print(f"Account Number: {inc_acc.get_account_number()}")
                bal_str = "CA${:,.2f}".format(self.get_balance(incoming_account_number))
                print(f"Balance: {bal_str}\n")
