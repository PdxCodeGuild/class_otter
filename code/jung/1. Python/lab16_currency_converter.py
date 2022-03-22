import requests
import pprint

amount = int(input("Amount: "))
to_currency = input("what currency do you want to convert to?: ").upper()
from_currency = "USD"

class Currency_converter():
    def __init__(self, url):
        self.data = requests.get(url).json()
        # pprint.pprint(self.data)
        self.currencies = self.data["rates"]

    def convert(self, from_currency, to_currency, amount):
        if from_currency != "USD":
            amount = amount / self.currencies[from_currency]
        amount = round(amount * self.currencies[to_currency], 2)
        return amount


url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = Currency_converter(url)
print(f"{amount} {to_currency} = {converter.convert(to_currency, from_currency, amount)} US dollars")


