import json
from Currency.Currency import Currency
from CurrencyCollection.CurrencyCollection import CurrencyCollection
from interfaces.IParserOption import IParserOption

class JsonArrayParserStrategy(IParserOption):
    def parse(self, data: str) -> CurrencyCollection:
        json_data = json.loads(data)

        # Pobieramy id i timestamp z pierwszej tabeli
        id = json_data[0]['no']
        timestamp = json_data[0]['effectiveDate']

        # Tworzymy kolekcję walut z id i timestamp
        collection = CurrencyCollection(id=id, timestamp=timestamp)

        # Przetwarzamy waluty
        for entry in json_data[0]['rates']:
            currency_code = entry.get('code')
            currency_name = entry.get('currency')
            currency_rate = entry.get('mid')

            if currency_code and currency_name and currency_rate is not None:
                currency = Currency(currency_code, currency_name, currency_rate)
                collection.add_currency(currency)
            else:
                print(f"Invalid entry: {entry}")

        return collection
