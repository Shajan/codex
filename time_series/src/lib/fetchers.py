import pandas as pd
from data_fetcher import DataFetcher

class CSVDataFetcher(DataFetcher):
    def fetch_data(self, file_path: str, **kwargs) -> pd.DataFrame:
        return pd.read_csv(file_path, **kwargs)

class TSVDataFetcher(DataFetcher):
    def fetch_data(self, file_path: str, **kwargs) -> pd.DataFrame:
        return pd.read_csv(file_path, sep='\t', **kwargs)
