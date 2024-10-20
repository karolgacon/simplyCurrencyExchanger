from Currency.Currency import Currency
from CurrencyCollection.CurrencyCollection import CurrencyCollection
from interfaces.ICurrency import ICurrency
from interfaces.ICurrencyCollection import ICurrencyCollection
from interfaces.IDataParser import IDataParser
import json


class JsonArrayParser(IDataParser):
    def parse_data(self, data: str) -> ICurrencyCollection:
        json_data = json.loads(data)
        # Pobieramy id i timestamp z pierwszej tabeli
        id: str = json_data[0]['no']
        timestamp: str = json_data[0]['effectiveDate']

        # Tworzymy kolekcję walut z id i timestamp
        collection: ICurrencyCollection = CurrencyCollection(tid=id, timestamp=timestamp)

        # Przetwarzamy waluty
        for entry in json_data[0]['rates']:
            currency_code: str = entry.get('code')
            currency_name: str = entry.get('currency')
            currency_rate: float = entry.get('mid')

            if currency_code and currency_name and currency_rate is not None:
                currency: ICurrency = Currency(currency_code, currency_name, currency_rate)
                collection.add_currency(currency)
            else:
                print(f"Invalid entry: {entry}")
        return collection
