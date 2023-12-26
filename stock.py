import requests
import json


API = "";



class Stock:

    stock_symbol: str
    market_price: float
    market_change: float
    market_open_price: float
    day_low: float
    day_high: float

    def __init__(self, stock_symbol: str):
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=' + API;
        response = requests.get(url)
        data = response.json()
        #json_data = json.loads(response.text)
        #stocks = json_data["quoteResponse"]["result"]
        print(data['Time Series (Daily)']['2023-12-08'])
        self.market_open_price = data['Time Series (Daily)']['2023-12-08']['1. open']

    def __str__(self):
        return "Open Price: " + self.market_open_price



testing = Stock("tsla")

print(Stock("tsla"))


