from interfaces.ICurrencyCollection import ICurrencyCollection
from interfaces.IDataParser import IDataParser
from interfaces.IParserOption import IParserOption
from ParserOption.JSONParserOption import JsonArrayParserOption
from ParserOption.XMLParserOption import XMLToArrayOption
import json
import xml.etree.ElementTree as ET


class DataParser(IDataParser):
    def __init__(self):
        self.__option: IParserOption = None

    def parse_data(self, data: str) -> ICurrencyCollection:
        # Rozpoznawanie formatu danych
        if self._is_json(data):
            self.__option = JsonArrayParserOption()  # Wybór parsera JSON
        elif self._is_xml(data):
            self.__option = XMLToArrayOption()  # Wybór parsera XML
        else:
            raise ValueError("Unsupported data format")

        return self.__option.parse(data,)

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
