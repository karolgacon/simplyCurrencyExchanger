import IExchanger

class Exchanger(IExchanger):
    __instance = None  # Singleton instance

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Exchanger, cls).__new__(cls)
        return cls.__instance

    def exchange(self, from_currency, to_currency, amount:float) ->float:
        rate_from = from_currency.getRate()
        rate_to = to_currency.getRate()
        return amount * rate_from / rate_to