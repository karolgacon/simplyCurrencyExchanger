from interfaces import IDataAcquisition
from urllib.request import urlopen

class WebDataAcquisition(IDataAcquisition):
    def __init__(self, url: str):
        self.url: str = url

    def acquire_data(self) -> str:
        with urlopen(self.url) as response:
            return response.read().decode('utf-8')
