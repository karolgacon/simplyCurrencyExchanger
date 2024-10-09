from abc import ABC, abstractmethod

class ICurrency(ABC):

    @abstractmethod
    def setName(self, name: str) -> None:
        pass

    @abstractmethod
    def getName(self) -> str:
        pass

    @abstractmethod
    def setCode(self, code: str) -> None:
        pass

    @abstractmethod
    def getCode(self) -> str:
        pass

    @abstractmethod
    def setRate(self, rate: float) -> None:
        pass

    @abstractmethod
    def getRate(self) -> float:
        pass
