# Moved YahooFinanceDataFetcher from src/yahoo_fetcher.py
import yfinance as yf
import pandas as pd
from data_fetcher import DataFetcher

class YahooFinanceDataFetcher(DataFetcher):
    def fetch_data(self, ticker: str, period: str = '1y', interval: str = '1d', **kwargs) -> pd.DataFrame:
        stock = yf.Ticker(ticker)
        return stock.history(period=period, interval=interval, **kwargs)
