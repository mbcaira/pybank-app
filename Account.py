class Account:
    """
    Account object providing access to account number and balance.
    """
    def __init__(self, account_number: str, balance: float):
        self._account_number = account_number
        self._balance = balance

    def get_balance(self) -> float:
        """
        Gets the account balance.
        :return: Account balance as a float.
        """
        return self._balance

    def set_balance(self, amount: float) -> None:
        """
        Sets the account balance to the desired amount.
        :param amount: Float representation of the desired balance.
        :return: None.
        """
        self._balance = amount

    def get_account_number(self) -> str:
        """
        Returns the account number.
        :return: Account number as a string.
        """
        return self._account_number
