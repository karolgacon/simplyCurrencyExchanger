from abc import ABC, abstractmethod

class ICurrency(ABC):

    @abstractmethod
    def setName(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def getName(self) -> str:
        return self.name

    @abstractmethod
    def setCode(self, code: str) -> None:
        self.code = code

    @abstractmethod
    def getCode(self) -> str:
        return self.code

    @abstractmethod
    def setRate(self, rate: float) -> None:
        self.rate = rate

    @abstractmethod
    def getRate(self) -> float:
        return self.rate
