# Fetcher implementations have been moved to src/lib/fetchers.py

import pandas as pd
from data_fetcher import DataFetcher

class CSVDataFetcher(DataFetcher):
    def fetch_data(self, file_path: str, **kwargs) -> pd.DataFrame:
        """
        Fetch data from a CSV file.
        Args:
            file_path (str): Path to the CSV file.
            **kwargs: Additional arguments for pandas.read_csv.
        Returns:
            pd.DataFrame: The loaded data.
        """
        return pd.read_csv(file_path, **kwargs)

class TSVDataFetcher(DataFetcher):
    def fetch_data(self, file_path: str, **kwargs) -> pd.DataFrame:
        """
        Fetch data from a TSV file.
        Args:
            file_path (str): Path to the TSV file.
            **kwargs: Additional arguments for pandas.read_csv.
        Returns:
            pd.DataFrame: The loaded data.
        """
        return pd.read_csv(file_path, sep='\t', **kwargs)
