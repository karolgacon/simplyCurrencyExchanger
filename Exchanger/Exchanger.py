from interfaces.ICurrency import ICurrency
from interfaces.ICurrencyCollection import ICurrencyCollection
from typing import Self
from interfaces.IExchanger import IExchanger


class Exchanger(IExchanger):
    _instance: Self = None  # Zmienna klasowa przechowująca jedyną instancję

    def __new__(cls, currency_collection: ICurrencyCollection = None):
        if cls._instance is None:
            if currency_collection is None:
                raise ValueError("Musisz przekazać currency_collection przy pierwszej inicjalizacji.")
            cls._instance = super(Exchanger, cls).__new__(cls)
            cls._instance.currency_collection = currency_collection
        return cls._instance

    @classmethod
    def get_instance(cls, currency_collection: ICurrencyCollection = None) -> Self:
        if cls._instance is None:
            if currency_collection is None:
                raise ValueError("Musisz przekazać currency_collection przy pierwszej inicjalizacji.")
            cls._instance = cls(currency_collection)
        return cls._instance

    def exchange(self, from_code: str, to_code: str, amount: float) -> float:
        from_currency: ICurrency = self.currency_collection.get_currency_by_code(from_code)
        to_currency: ICurrency = self.currency_collection.get_currency_by_code(to_code)

        if not from_currency or not to_currency:
            raise ValueError("Niepoprawny kod waluty")

        exchanged_amount: float = (amount * from_currency.get_rate()) / to_currency.get_rate()
        return round(exchanged_amount, 2)
