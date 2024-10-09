from Currency import Currency, ICurrency
import json
from Parser.IParser import IParser


class JSONToDictParser(IParser):
    def parse(self, dataset:list) -> dict:
        currency_dict = {}
        data = dataset[0]
        for item in data["rates"]:
            name = item["currency"]
            code = item["code"]
            rate = float(item["mid"])
            currency = Currency.Currency(code, name, rate)
            currency_dict[code] = currency

        code_pln = "PLN"
        name_pln = "Polski złoty"
        rate = 1
        currency = Currency.Currency(code_pln, name_pln, rate)
        currency_dict[code_pln] = currency
        return currency_dict