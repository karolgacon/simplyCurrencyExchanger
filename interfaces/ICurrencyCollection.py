from abc import ABC, abstractmethod

class ICurrencyCollection(ABC):
    @abstractmethod
    def add_currency(self, currency):
        pass