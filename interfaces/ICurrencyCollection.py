from abc import ABC, abstractmethod

class ICurrencyCollection(ABC):
    @abstractmethod
    def add_currency(self, currency):
        pass
    @abstractmethod
    def add_currencies(self, currency_dict):
        pass
    @abstractmethod
    def get_currencies(self):
        pass
    @abstractmethod
    def get_currency_by_code(self, code):
        pass
    @abstractmethod
    def get_timestamp(self) -> str:
        pass
    @abstractmethod
    def get_id(self) -> str:
        pass