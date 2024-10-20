from flask import Flask, render_template, request
from DataProvider.FileDataProvider import FileDataProvider
from DataProvider.WebDataProvider import WebDataProvider
from Exchanger.Exchanger import Exchanger
from typing import Self
from Parser.JSONParser import JsonArrayParser
from Parser.XMLParser import XMLArrayParser
from interfaces.IDataProvider import IDataProvider
from interfaces.IDataParser import IDataParser

class FlaskApp:
    _instance: Self = None

    @classmethod
    def get_instance(cls, exchanger: Exchanger, web_data_acquisition: IDataProvider, file_data_acquisition: IDataProvider, data_parser: IDataParser) -> 'FlaskApp':
        """Zwraca instancję FlaskApp, tworząc ją jeśli nie istnieje."""
        if cls._instance is None:
            cls._instance = cls(exchanger, web_data_acquisition, file_data_acquisition, data_parser)
        return cls._instance

    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = super(FlaskApp, cls).__new__(cls)
            cls._instance._exchanger = None
            cls._instance._web_data_acquisition = None
            cls._instance._currency_collection = None
            cls._instance._data_parser = None
            cls._instance._file_data_acquisition = None
            cls._instance._app = Flask(__name__)
            cls._instance._configure_routes()
        return cls._instance

    def _configure_routes(self) -> None:

        @self._app.route('/')
        def index() -> str:
            return render_template('index.html', currency_collection=self._exchanger.currency_collection.get_currencies())

        @self._app.route('/exchange', methods=['POST'])
        def exchange() -> str:
            from_currency_code: str = request.form['from_currency'].upper()
            to_currency_code: str = request.form['to_currency'].upper()
            amount: float = float(request.form['amount'])

            from_currency = self._exchanger.currency_collection.get_currency_by_code(from_currency_code).get_name()
            to_currency = self._exchanger.currency_collection.get_currency_by_code(to_currency_code).get_name()

            try:
                result: float = self._exchanger.exchange(from_currency_code, to_currency_code, amount)
                return render_template('result.html', result=result, from_currency_code=from_currency_code, to_currency_code=to_currency_code, amount=amount, from_currency=from_currency, to_currency=to_currency)
            except ValueError as e:
                return render_template('result.html', error=str(e))

        @self._app.route('/currencies', methods=['POST'])
        def currencies() -> str:
            return render_template('currencies.html', currencies=self._exchanger.currency_collection.get_currencies(), timestamp=self._exchanger.currency_collection.get_timestamp(), id_collection=self._exchanger.currency_collection.get_id())

        # Obsługa wczytania danych z pliku
        @self._app.route('/load_file', methods=['POST'])
        def load_file():
            data = self._file_data_acquisition.acquire_data()  # Pobieranie danych z pliku
            self._exchanger.currency_collection = self._data_parser.parse_data(data)  # Przypisujemy dane do kolekcji walut
            return render_template('index.html', currency_collection=self._exchanger.currency_collection.get_currencies())

        @self._app.route('/load_api', methods=['POST'])
        def load_api():
            data = self._web_data_acquisition.acquire_data()  # Pobieranie danych z pliku
            self._exchanger.currency_collection = self._data_parser.parse_data(data)  # Przypisujemy dane do kolekcji walut
            return render_template('index.html', currency_collection=self._exchanger.currency_collection.get_currencies())

    def run(self) -> None:
        self._web_data_acquisition = WebDataProvider("https://api.nbp.pl/api/exchangerates/tables/A")
        self._file_data_acquisition = FileDataProvider("./data.json")
        self._data_parser = JsonArrayParser()
        self._currency_collection = self._data_parser.parse_data(self._web_data_acquisition.acquire_data())
        self._exchanger = Exchanger(self._currency_collection)
        self._app.run(debug=True)
