from FlaskApp.FlaskApp import FlaskApp
from Exchanger.Exchanger import Exchanger
from Parser.DataParser import DataParser
from ParserOption.JSONParserOption import JsonArrayParserOption
from DataProvider.WebDataProvider import WebDataProvider
from DataProvider.FileDataProvider import FileDataProvider
from interfaces.ICurrencyCollection import ICurrencyCollection
from interfaces.IDataProvider import IDataProvider
from interfaces.IDataParser import IDataParser

# Inicjalizacja danych walutowych i aplikacji
web_data_acquisition: IDataProvider = WebDataProvider("https://api.nbp.pl/api/exchangerates/tables/A?format=json")
file_data_acquisition: IDataProvider = FileDataProvider("./A.xml")
json_parser: IDataParser = DataParser()
data: str = web_data_acquisition.acquire_data()
currency_collection: ICurrencyCollection = json_parser.parse_data(data)
exchanger: Exchanger = Exchanger(currency_collection)

# Utworzenie instancji aplikacji Flask jako Singleton
app_instance: FlaskApp = FlaskApp(exchanger, web_data_acquisition, file_data_acquisition, json_parser)

if __name__ == "__main__":
    app_instance.run()