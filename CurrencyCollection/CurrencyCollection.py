from ICurrencyCollection import ICurrencyCollection
from Currency import Currency

class CurrencyCollection(ICurrencyCollection):
    def __init__(self):
        self.currencies = {}

    def addCurrency(self, currency: Currency) -> None:
        self.currencies[currency.getCode()] = currency

    def getCurrencies(self) -> list:
        return list(self.currencies.values())

    def getCurrencyByCode(self, code: str) -> str:
        return self.currencies.get(code)