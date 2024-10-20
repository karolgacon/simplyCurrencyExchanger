from interfaces.IDataParser import IDataParser
from interfaces.IParserOption import IParserOption
from ParserOption.JSONParserOption import JsonArrayParserOption
from ParserOption.XMLParserOption import XMLToCollectionOption
from CurrencyCollection.CurrencyCollection import CurrencyCollection
import json
import xml.etree.ElementTree as ET


class DataParser(IDataParser):
    def __init__(self):
        self.strategy: IParserOption = None

    def parse_data(self, data: str) -> CurrencyCollection:
        # Rozpoznawanie formatu danych
        if self._is_json(data):
            self.strategy = JsonArrayParserOption()  # Wybór parsera JSON
        elif self._is_xml(data):
            self.strategy = XMLToCollectionOption()  # Wybór parsera XML
        else:
            raise ValueError("Unsupported data format")

        return self.strategy.parse(data)

    def _is_json(self, data: str) -> bool:
        # Sprawdzenie, czy dane są w formacie JSON
        try:
            json.loads(data)
            return True
        except ValueError:
            return False

    def _is_xml(self, data: str) -> bool:
        # Sprawdzenie, czy dane są w formacie XML
        try:
            ET.fromstring(data)
            return True
        except ET.ParseError:
            return False
