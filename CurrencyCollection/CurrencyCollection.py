
from Currency import ICurrency
from CurrencyCollection.ICurrencyCollection import ICurrencyCollection


class CurrencyCollection(ICurrencyCollection):
    def __init__(self):
        self.currencies = {}

    def addCurrency(self, currency: ICurrency) -> None:
        self.currencies[currency.getCode()] = currency

    def addCurrencies(self, currency_dict: dict) -> None:
        self.currencies.update(currency_dict)

    def getCurrencies(self):
        return list(self.currencies.values())

    def getCurrencyByCode(self, code: str) -> ICurrency:
        return self.currencies.get(code)