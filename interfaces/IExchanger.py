from abc import ABC, abstractmethod
from typing import Self

from interfaces.ICurrencyCollection import ICurrencyCollection


class IExchanger(ABC):
    @abstractmethod
    def exchange(self, from_code: str, to_code: str, amount: float) -> float:
        pass

    @classmethod
    @abstractmethod
    def get_instance(cls, currency_collection: ICurrencyCollection = None) -> Self:
        pass