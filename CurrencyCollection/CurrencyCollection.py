from interfaces.ICurrency import ICurrency
from Currency.Currency import Currency
from interfaces.ICurrencyCollection import ICurrencyCollection


class CurrencyCollection(ICurrencyCollection):
    def __init__(self, tid: str = "", timestamp: str = ""):
        self.__currencies: dict[str, ICurrency] = {}
        self.__id = tid
        self.__timestamp = timestamp
        self.add_currency(Currency('PLN', 'Polish zloty', 1.0))

    def add_currency(self, currency: ICurrency) -> None:
        self.__currencies[currency.get_code()] = currency

    def add_currencies(self, currency_dict: dict) -> None:
        self.__currencies.update(currency_dict)

    def get_currencies(self) -> list[ICurrency]:
        return list(self.__currencies.values())

    def get_currency_by_code(self, code: str) -> ICurrency:
        return self.__currencies.get(code)

    def get_timestamp(self) -> str:
        return self.__timestamp

    def get_id(self) -> str:
        return self.__id