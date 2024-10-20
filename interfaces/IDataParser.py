from abc import ABC, abstractmethod
from interfaces.ICurrencyCollection import ICurrencyCollection

class IDataParser(ABC):
    @abstractmethod
    def parse_data(self, data: str) -> ICurrencyCollection:
        pass
