from abc import ABC, abstractmethod

class IParserOption(ABC):
    @abstractmethod
    def parse(self, data):
        pass
