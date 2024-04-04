import requests
import matplotlib.pyplot as plt
import numpy as np


class StockPrice:
    def __init__(self, symbol, interval, data_format):
        self.symbol = symbol
        self.interval = interval
        self.data_format = data_format if data_format else 'json'
        self.data = None

    def get_stock_price_data(self):
        base_url = 'https://www.alphavantage.co/query'
        base_url += '?function=TIME_SERIES_INTRADAY'
        base_url += '&symbol='
        base_url += self.symbol
        base_url += '&interval='
        base_url += self.interval
        base_url += '&outputsize=full'
        base_url += '&apikey=2PMB2A1ST12JVPQT'
        base_url += '&datatype='
        base_url += self.data_format
        url = base_url

        response = requests.get(url)
        if response.status_code == 200:
            self.data = response.content
            return self.data
        else:
            return False

    def plot_stock_price_data(self):
        # Method implementation
        pass
