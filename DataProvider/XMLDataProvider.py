import requests
from DataProvider import IDataProvider

class XMLDataProvider(IDataProvider.IDataProvider):
    NBP_API_URL = "https://api.nbp.pl/api/exchangerates/tables/a/"

    def acquireData(self) -> str:
        response = requests.get(self.NBP_API_URL)
        return response.text