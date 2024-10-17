from typing import List

from Currency.Currency import Currency
from interfaces import ICurrencyCollection


class CurrencyCollection(ICurrencyCollection):
    def __init__(self):
        self.currencies: dict[str, Currency] = {}

    def add_currency(self, currency: Currency) -> None:
        self.currencies[currency.get_code()] = currency

    def add_currencies(self, currency_dict: dict) -> None:
        self.currencies.update(currency_dict)

    def get_currencies(self) -> list[Currency]:
        return list(self.currencies.values())

    def get_currency_by_code(self, code: str) -> Currency:
        return self.currencies.get(code)