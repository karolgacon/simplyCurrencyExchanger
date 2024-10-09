from abc import ABC, abstractmethod


class ICurrencyCollection(ABC):
    @abstractmethod
    def addCurrency(self, currency):
        pass

    @abstractmethod
    def addCurrencies(self, currencies):
        pass

    @abstractmethod
    def getCurrencies(self):
        pass

    @abstractmethod
    def getCurrencyByCode(self, code: str):
        pass
