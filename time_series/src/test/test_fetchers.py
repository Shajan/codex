# Moved tests from src/test_fetchers.py
import unittest
import pandas as pd
import os
import sys
import pathlib

SRC_PATH = str(pathlib.Path(__file__).parent.parent)
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

from lib.fetchers import CSVDataFetcher, TSVDataFetcher
from lib.http_fetcher import HTTPPaginatedDataFetcher
from lib.yahoo_fetcher import YahooFinanceDataFetcher
from unittest.mock import patch, MagicMock

class TestCSVDataFetcher(unittest.TestCase):
    def setUp(self):
        self.fetcher = CSVDataFetcher()
        self.test_file = 'test.csv'
        pd.DataFrame({'a': [1, 2], 'b': [3, 4]}).to_csv(self.test_file, index=False)

    def tearDown(self):
        os.remove(self.test_file)

    def test_fetch_data(self):
        df = self.fetcher.fetch_data(self.test_file)
        self.assertEqual(list(df.columns), ['a', 'b'])
        self.assertEqual(df.shape, (2, 2))

class TestTSVDataFetcher(unittest.TestCase):
    def setUp(self):
        self.fetcher = TSVDataFetcher()
        self.test_file = 'test.tsv'
        pd.DataFrame({'a': [1, 2], 'b': [3, 4]}).to_csv(self.test_file, sep='\t', index=False)

    def tearDown(self):
        os.remove(self.test_file)

    def test_fetch_data(self):
        df = self.fetcher.fetch_data(self.test_file)
        self.assertEqual(list(df.columns), ['a', 'b'])
        self.assertEqual(df.shape, (2, 2))

class TestHTTPPaginatedDataFetcher(unittest.TestCase):
    @patch('lib.http_fetcher.requests.get')
    @patch('lib.http_fetcher.BeautifulSoup')
    def test_fetch_data(self, mock_bs, mock_get):
        fetcher = HTTPPaginatedDataFetcher()
        # Mock the response and soup
        # ...existing code...
