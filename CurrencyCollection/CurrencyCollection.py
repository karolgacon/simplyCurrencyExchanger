from interfaces.ICurrency import ICurrency
from Currency.Currency import Currency
from interfaces.ICurrencyCollection import ICurrencyCollection

class CurrencyCollection(ICurrencyCollection):
    def __init__(self, tid: str = "", timestamp: str = ""):
        self.__currencies: list[ICurrency] = []  # Użycie listy zamiast słownika
        self.__id = tid
        self.__timestamp = timestamp
        self.add_currency(Currency('PLN', 'Polish zloty', 1.0))

    def add_currency(self, currency: ICurrency) -> None:
        self.__currencies.append(currency)  # Dodawanie waluty do listy

    def add_currencies(self, currency_list: list[ICurrency]) -> None:
        self.__currencies.extend(currency_list)  # Dodawanie wielu walut do listy

    def get_currencies(self) -> list[ICurrency]:
        return self.__currencies  # Zwracanie listy walut

    def get_currency_by_code(self, code: str) -> ICurrency:
        for currency in self.__currencies:
            if currency.get_code() == code:
                return currency
        return None  # Jeśli waluta nie zostanie znaleziona, zwróć None

    def get_timestamp(self) -> str:
        return self.__timestamp

    def get_id(self) -> str:
        return self.__id
