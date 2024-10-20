from abc import ABC, abstractmethod

class ICurrency(ABC):
    @abstractmethod
    def set_name(self, name: str) -> None:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def set_code(self, code: str) -> None:
        pass

    @abstractmethod
    def get_code(self) -> str:
        pass

    @abstractmethod
    def set_rate(self, rate: float) -> None:
        pass

    @abstractmethod
    def get_rate(self) -> float:
        pass

    @abstractmethod
    def __eq__(self, __value: object) -> bool:
        pass
