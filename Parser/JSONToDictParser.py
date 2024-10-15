from Currency import Currency
from Parser.IParser import IParser


class JSONToDictParser(IParser):
    def parse(self, dataset: list) -> dict:
        currency_dict = {}
        data = dataset[0]
        for item in data["rates"]:
            name = item["currency"]
            code = item["code"]
            rate = float(item["mid"])
            currency = Currency.Currency(code, name, rate)
            currency_dict[code] = currency

        code_pln = "PLN"
        name_pln = "Polish zloty"
        rate = 1
        currency = Currency.Currency(code_pln, name_pln, rate)
        currency_dict[code_pln] = currency
        return currency_dict

    # TODO add binary decoding and parser to xml from binary,txt
