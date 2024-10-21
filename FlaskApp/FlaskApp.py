from flask import Flask, render_template, request
from DataProvider.FileDataProvider import FileDataProvider
from DataProvider.WebDataProvider import WebDataProvider
from Exchanger.Exchanger import Exchanger
from typing import Self
from FlaskApp.FlaskRoutes import FlaskRoutes
from Parser.JSONParser import JsonArrayParser
from Parser.XMLParser import XMLArrayParser
from interfaces.ICurrencyCollection import ICurrencyCollection
from interfaces.IDataProvider import IDataProvider
from interfaces.IDataParser import IDataParser
from interfaces.IExchanger import IExchanger


class FlaskApp:
    _instance: Self = None

    @classmethod
    def get_instance(cls, exchanger: IExchanger, web_data_acquisition: IDataProvider, file_data_acquisition: IDataProvider, data_parser: IDataParser) -> Self:
        if cls._instance is None:
            cls._instance = cls(exchanger, web_data_acquisition, file_data_acquisition, data_parser)
        return cls._instance

    def __new__(cls) -> Self:
        if cls._instance is None:
            cls._instance = super(FlaskApp, cls).__new__(cls)
            cls._instance._exchanger: IExchanger = None
            cls._instance._web_data_acquisition: IDataProvider = None
            cls._instance._currency_collection: ICurrencyCollection = None
            cls._instance._data_parser: IDataParser = None
            cls._instance._file_data_acquisition:  IDataProvider = None
            cls._instance._app = Flask(__name__)
            cls._instance._configure_app()
        return cls._instance

    def _configure_app(self) -> None:
        self._web_data_provider = WebDataProvider("https://api.nbp.pl/api/exchangerates/tables/A?format=xml")
        self._file_data_provider = FileDataProvider("./A.xml")
        self._data_parser = XMLArrayParser()
        data: str = self._web_data_provider.acquire_data()
        self._currency_collection = self._data_parser.parse_data(data)
        self._exchanger = Exchanger(self._currency_collection)
        self._routes = FlaskRoutes(self._app, self._exchanger, self._web_data_provider, self._file_data_provider,
                                   self._data_parser)

    def run(self) -> None:
        self._app.run(debug=True)
