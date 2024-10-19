from FlaskApp.FlaskApp import FlaskApp
from Exchanger.Exchanger import Exchanger
from Parser.DataParser import DataParser
from ParserOption.JSONParserStrategy import JsonArrayParserOption
from DataProvider.WebDataAcquisition import WebDataAcquisition

# Inicjalizacja danych walutowych i aplikacji
web_data_acquisition: WebDataAcquisition = WebDataAcquisition("https://api.nbp.pl/api/exchangerates/tables/A?format=json")
json_parser: DataParser = DataParser(JsonArrayParserOption())
data: str = web_data_acquisition.acquire_data()
currency_collection = json_parser.parse_data(data)
exchanger: Exchanger = Exchanger(currency_collection)

# Utworzenie instancji aplikacji Flask jako Singleton
app_instance: FlaskApp = FlaskApp(exchanger)

if __name__ == "__main__":
    app_instance.run()
