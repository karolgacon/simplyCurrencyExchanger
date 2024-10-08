from ICurrency import ICurrency

class Currency(ICurrency):
    def __init__(self, name:str, code:str, rate:float):
        self.name = name
        self.code = code
        self.rate = rate

    def setName(self, name: str) -> None:
        self.name = name

    def getName(self) -> str:
        return self.name

    def setCode(self, code: str) -> None:
        self.code = code

    def getCode(self) -> str:
        return self.code

    def setRate(self, rate: float) -> None:
        self.rate = rate

    def getRate(self) -> float:
        return self.rate