from abc import ABC, abstractmethod
from interfaces.ICurrencyCollection import ICurrencyCollection

class IParserOption(ABC):
    @abstractmethod
    def parse(self, data: str) -> ICurrencyCollection:
        pass
