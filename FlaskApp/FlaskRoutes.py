from flask import Flask, render_template, request
from Exchanger.Exchanger import Exchanger
from interfaces.IDataProvider import IDataProvider
from interfaces.IDataParser import IDataParser
from interfaces.IExchanger import IExchanger


class FlaskRoutes:
    def __init__(self, app: Flask, exchanger: IExchanger, web_data_provider: IDataProvider, file_data_provider: IDataProvider, data_parser: IDataParser):
        self._app = app
        self._exchanger = exchanger
        self._web_data_provider = web_data_provider
        self._file_data_provider = file_data_provider
        self._data_parser = data_parser
        self._configure_routes()

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

        @self._app.route('/load_file', methods=['POST'])
        def load_file():
            data = self._file_data_provider.acquire_data()  # Pobieranie danych z pliku
            self._update_currency_collection(data)
            return render_template('index.html', currency_collection=self._exchanger.currency_collection.get_currencies())

        @self._app.route('/load_api', methods=['POST'])
        def load_api():
            data = self._web_data_provider.acquire_data()  # Pobieranie danych z API
            self._update_currency_collection(data)
            return render_template('index.html', currency_collection=self._exchanger.currency_collection.get_currencies())

    def _update_currency_collection(self, data: str) -> None:
        self._exchanger.currency_collection = self._data_parser.parse_data(data)
