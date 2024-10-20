from interfaces.ICurrency import ICurrency

class Currency:
    def __init__(self,  code: str, name: str = None, rate: float = None):
        if name is None and rate is None:
            self.__code = code
        else:
            self.__name = name
            self.__code = code
            self.__rate = rate

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, ICurrency):
            return self.__code == __value.get_code()
        return False


    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def set_code(self, code: str) -> None:
        self.__code = code

    def get_code(self) -> str:
        return self.__code

    def set_rate(self, rate: float) -> None:
        self.__rate = rate

    def get_rate(self) -> float:
        return self.__rate