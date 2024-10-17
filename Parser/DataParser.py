from interfaces.IDataParser import IDataParser
from interfaces.IParserOption import IParserOption
from CurrencyCollection.CurrencyCollection import CurrencyCollection

class DataParser(IDataParser):
    def __init__(self, strategy: IParserOption):
        self.strategy: IParserOption = strategy

    def parse_data(self, data: str) -> CurrencyCollection:
        return self.strategy.parse(data)
