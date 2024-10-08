from Currency import Currency, ICurrency
from IParser import IParser
import xml.etree.ElementTree as ET

class XMLToDictParser(IParser):
    def parse(self, data:str) -> dict:
        currency_dict = {}
        root=ET.fromstring(data)
        for item in root.findall(".//Rate"):
            name=item.find("Currency").text
            code=item.find("Code").text
            rate=float(item.find("Mid").text)
            currency = Currency.Currency(code, name, rate)
            currency_dict[code]=currency
        return currency_dict