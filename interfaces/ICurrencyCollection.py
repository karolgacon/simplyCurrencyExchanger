from abc import ABC, abstractmethod

class ICurrencyCollection(ABC):
    @abstractmethod
    def add_currency(self, currency):
        pass

    def add_currencies(self, currency_dict):
        pass

    def get_currencies(self):
        pass

    def get_currency_by_code(self, code):
        pass
