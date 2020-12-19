import Currency


class Currencies:
    """
    Stores in use currencies and provides access to the individual objects.
    """
    _CAD = Currency.CAD()
    _USD = Currency.USD()
    _EUR = Currency.EUR()
    __instance = None

    @staticmethod
    def get_instance():
        """
        Returns the instance of Currencies.

        :return: Instance of Currencies..
        """
        if Currencies.__instance is None:
            Currencies()
        return Currencies.__instance

    def __init__(self):
        """
        Singleton pattern for the Currencies class.
        """
        if Currencies.__instance is None:
            Currencies.__instance = self

    def get_currency(self, option: str) -> Currency:
        """
        Maps the option string to the desired currency and returns it.

        :param option: String that maps to a respective currency.
        :return: Currency object.
        """
        valid = False
        while not valid:
            if option == "1":
                return self._CAD
            if option == "2":
                return self._USD
            if option == "3":
                return self._EUR
            else:
                option = input("Invalid currency selection! Please try again.\n"
                               "Please select the currency you would like to perform "
                               "the transaction in:\n(1) CAD\n(2) USD\n(3) EUR\n")
