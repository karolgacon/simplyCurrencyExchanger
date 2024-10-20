import xml.etree.ElementTree as Et
from Currency.Currency import Currency
from CurrencyCollection.CurrencyCollection import CurrencyCollection
from interfaces.ICurrencyCollection import ICurrencyCollection
from interfaces.IParserOption import IParserOption

class XMLToArrayOption(IParserOption):
    @staticmethod
    def parse(data: str) -> ICurrencyCollection:
        root = Et.fromstring(data)
        id: str = root.find("ExchangeRatesTable").find("No").text
        timestamp: str = root.find("ExchangeRatesTable").find("EffectiveDate").text

        # Tworzymy kolekcję walut z id i timestamp
        collection: ICurrencyCollection = CurrencyCollection(tid=id, timestamp=timestamp)

        for currency_node in root.find("ExchangeRatesTable").find("Rates").findall("Rate"):
            code: str = currency_node.find('Code').text
            rate: float = float(currency_node.find('Mid').text)
            name: str = currency_node.find('Currency').text
            currency: Currency = Currency(code, name, rate)
            collection.add_currency(currency)
        return collection
