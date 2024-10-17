
class Currency:
    def __init__(self,  code: str, name: str = None, rate: float = None):
        if name is None and rate is None:
            self.code = code
        else:
            self.name = name
            self.code = code
            self.rate = rate

    def __eq__(self, __value: object) -> bool:
        if self.code == __value.get_code():
            return True
        else:
            return False

    def set_name(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_code(self, code: str) -> None:
        self.code = code

    def get_code(self) -> str:
        return self.code

    def set_rate(self, rate: float) -> None:
        self.rate = rate

    def get_rate(self) -> float:
        return self.rate