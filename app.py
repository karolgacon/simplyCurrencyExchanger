from flask import Flask, render_template, request
from DataProvider import XMLDataProvider, IDataProvider
from Exchanger import Exchanger
from CurrencyCollection import CurrencyCollection, ICurrencyCollection
from Parser import JSONToDictParser, IParser


app = Flask(__name__)


data_provider: IDataProvider = XMLDataProvider.XMLDataProvider()
json_data = data_provider.acquireData()

parser: IParser = JSONToDictParser.JSONToDictParser()
currency_dict = parser.parse(json_data)

currency_collection: ICurrencyCollection = CurrencyCollection.CurrencyCollection()
currency_collection.addCurrencies(currency_dict)

exchanger = Exchanger.Exchanger()  # Singleton instance


@app.route('/')
def index():
    currencies = currency_collection.getCurrencies()
    return render_template('index.html', currencies=currencies)


@app.route('/exchange', methods=['POST'])
def exchange():
    from_currency_code = request.form['from_currency']
    to_currency_code = request.form['to_currency']
    amount = float(request.form['amount'])

    from_currency = currency_collection.getCurrencyByCode(from_currency_code)
    to_currency = currency_collection.getCurrencyByCode(to_currency_code)

    result = exchanger.exchange(from_currency, to_currency, amount)

    return render_template('result.html',
                           from_currency_code=from_currency_code,
                           to_currency_code=to_currency_code,
                           from_currency=from_currency.getName(),
                           to_currency=to_currency.getName(),
                           amount=amount,
                           result=result)


if __name__ == '__main__':
    app.run(debug=True)
