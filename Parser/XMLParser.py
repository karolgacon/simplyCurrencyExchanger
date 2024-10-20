import xml.etree.ElementTree as Et
from Currency.Currency import Currency
from CurrencyCollection.CurrencyCollection import CurrencyCollection
from interfaces.ICurrency import ICurrency
from interfaces.ICurrencyCollection import ICurrencyCollection
from interfaces.IDataParser import IDataParser

class XMLArrayParser(IDataParser):
    def parse_data(self, data: str) -> ICurrencyCollection:
        root = Et.fromstring(data)
        id: str = root.find("ExchangeRatesTable").find("No").text
        timestamp: str = root.find("ExchangeRatesTable").find("EffectiveDate").text

        # Tworzymy kolekcję walut z id i timestamp
        collection: ICurrencyCollection = CurrencyCollection(tid=id, timestamp=timestamp)

        for currency_node in root.find("ExchangeRatesTable").find("Rates").findall("Rate"):
            code: str = currency_node.find('Code').text
            rate: float = float(currency_node.find('Mid').text)
            name: str = currency_node.find('Currency').text
            currency: ICurrency = Currency(code, name, rate)
            collection.add_currency(currency)
        return collection
