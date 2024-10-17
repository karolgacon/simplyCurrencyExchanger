import xml.etree.ElementTree as Et
from Currency.Currency import Currency
from CurrencyCollection.CurrencyCollection import CurrencyCollection
from interfaces import IParserOption

class XmlStringToCollectionParserStrategy(IParserOption):
    @staticmethod
    def parse(data: str) -> CurrencyCollection:
        root = Et.fromstring(data)
        collection: CurrencyCollection = CurrencyCollection()
        for currency_node in root.findall('currency'):
            code: str = currency_node.find('code').text
            rate: float = float(currency_node.find('rate').text)
            name: str = currency_node.find('name').text
            currency: Currency = Currency(code, name, rate)
            collection.add_currency(currency)
        return collection
