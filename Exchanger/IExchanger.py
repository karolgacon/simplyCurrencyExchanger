from abc import ABC, abstractmethod

class IExchanger(ABC):
    @abstractmethod
    def exchange(self, from_currency, to_currency, amount: float): pass