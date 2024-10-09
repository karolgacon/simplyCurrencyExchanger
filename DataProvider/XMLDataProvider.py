import requests
from DataProvider import IDataProvider

class XMLDataProvider(IDataProvider.IDataProvider):
    def __init__(self):
        self.link = "https://api.nbp.pl/api/exchangerates/tables/a/"

    def acquireData(self) -> list:
        response = requests.get(self.link)
        return response.json()