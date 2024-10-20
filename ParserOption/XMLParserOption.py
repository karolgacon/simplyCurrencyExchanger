import xml.etree.ElementTree as Et
from Currency.Currency import Currency
from CurrencyCollection.CurrencyCollection import CurrencyCollection
from interfaces.IParserOption import IParserOption

class XMLToCollectionOption(IParserOption):
    def parse(self, data: str) -> CurrencyCollection:
        root = Et.fromstring(data)
        id = root.find("ExchangeRatesTable").find("No").text
        timestamp = root.find("ExchangeRatesTable").find("EffectiveDate").text

        # Tworzymy kolekcję walut z id i timestamp
        collection = CurrencyCollection(tableID=id, timestamp=timestamp)

        collection: CurrencyCollection = CurrencyCollection()
        for currency_node in root.find("ExchangeRatesTable").find("Rates").findall("Rate"):
            code: str = currency_node.find('Code').text
            rate: float = float(currency_node.find('Mid').text)
            name: str = currency_node.find('Currency').text
            currency: Currency = Currency(code, name, rate)
            collection.add_currency(currency)
        return collection
