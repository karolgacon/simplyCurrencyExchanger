from abc import ABC, abstractmethod

class IDataParser(ABC):
    @abstractmethod
    def parse_data(self, data):
        pass