import yfinance as yf
from typing import List

def get_data(stocks: str |  List[str], timeframe: str):
    if isinstance(stocks, str):
        data = yf.Ticker(stocks)
    else:
        data = yf.Tickers(stocks)
    return data.history(timeframe)

