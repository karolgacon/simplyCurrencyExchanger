from Currency.ICurrency import ICurrency


class Currency(ICurrency):
    def __init__(self,  code:str, name:str = None, rate:float = None):
        if name is None and rate is None:
            self.code = code
        else:
            self.name = name
            self.code = code
            self.rate = rate

    def __eq__(self, __value: object) -> bool:
        if self.code == __value.getCode():
            return True
        else:
            return False

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