from abc import ABC, abstractmethod


class Currency(ABC):
    """
    Abstract factory class of Currency.
    """

    def __init__(self):
        prefix = ""
        rate = None

    @abstractmethod
    def get_prefix(self) -> str:
        """
        Gets the string pre-fix of the currency.

        :return: String currency pre-fix.
        """
        pass

    @abstractmethod
    def get_rate(self) -> float:
        """
        Gets the exchange rate of the currency to CAD.
        :return: Float of the exchange rate to CAD.
        """
        pass


class CAD(Currency):
    """
    CAD currency class.
    """
    def __init__(self):
        self.prefix = "CA$"
        self.rate = 1.00

    def get_prefix(self):
        return self.prefix

    def get_rate(self):
        return self.rate


class USD(Currency):
    """
    USD currency class.
    """
    def __init__(self):
        self.prefix = "US$"
        self.rate = 1.50

    def get_prefix(self):
        return self.prefix

    def get_rate(self):
        return self.rate


class EUR(Currency):
    """
    EUR currency class.
    """
    def __init__(self):
        self.prefix = "€"
        self.rate = 2.00

    def get_prefix(self):
        return self.prefix

    def get_rate(self):
        return self.rate
