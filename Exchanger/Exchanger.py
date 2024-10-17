from CurrencyCollection import CurrencyCollection
from Currency.Currency import Currency

class Exchanger:
    def __init__(self, currency_collection: CurrencyCollection):
        self.currency_collection: CurrencyCollection = currency_collection

    def exchange(self, from_code: str, to_code: str, amount: float) -> float:
        from_currency: Currency = self.currency_collection.get_currency_by_code(from_code)
        to_currency: Currency = self.currency_collection.get_currency_by_code(to_code)

        if not from_currency or not to_currency:
            raise ValueError("Niepoprawny kod waluty")

        exchanged_amount: float = (amount * from_currency.get_rate()) / to_currency.get_rate()
        return round(exchanged_amount,2)
