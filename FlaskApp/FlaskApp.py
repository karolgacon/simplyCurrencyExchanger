from flask import Flask, render_template, request
from Exchanger.Exchanger import Exchanger
from typing import Optional

class FlaskApp:
    _instance: Optional['FlaskApp'] = None

    def __new__(cls, exchanger: Exchanger) -> 'FlaskApp':
        if cls._instance is None:
            cls._instance = super(FlaskApp, cls).__new__(cls)
            cls._instance._exchanger = exchanger
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

        @self._app.route('/currencies')
        def currencies() -> str:
            return render_template('currencies.html', currencies=self._exchanger.currency_collection.get_currencies(), timestamp=self._exchanger.currency_collection.get_timestamp(), id_collection=self._exchanger.currency_collection.get_id())

    def run(self) -> None:
        self._app.run(debug=True)
