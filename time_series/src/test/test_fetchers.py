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
        url = 'http://example.com'
        # Mock the response
        mock_get.return_value.text = '<html></html>'
        # Mock soup and row/cell structure
        mock_soup = MagicMock()
        mock_bs.return_value = mock_soup
        # Create two mock rows, each with two mock cells
        mock_row1 = MagicMock()
        mock_row2 = MagicMock()
        mock_cell1 = MagicMock()
        mock_cell2 = MagicMock()
        mock_cell3 = MagicMock()
        mock_cell4 = MagicMock()
        mock_cell1.get_text.return_value = 'A1'
        mock_cell2.get_text.return_value = 'B1'
        mock_cell3.get_text.return_value = 'A2'
        mock_cell4.get_text.return_value = 'B2'
        mock_row1.find_all.return_value = [mock_cell1, mock_cell2]
        mock_row2.find_all.return_value = [mock_cell3, mock_cell4]
        mock_soup.select.return_value = [mock_row1, mock_row2]
        mock_soup.select_one.return_value = None  # No next page
        df = fetcher.fetch_data(url, data_selector='tr')
        self.assertEqual(df.shape[0], 2)
        self.assertEqual(df.iloc[0, 0], 'A1')
        self.assertEqual(df.iloc[0, 1], 'B1')
        self.assertEqual(df.iloc[1, 0], 'A2')
        self.assertEqual(df.iloc[1, 1], 'B2')

class TestYahooFinanceDataFetcher(unittest.TestCase):
    @patch('lib.yahoo_fetcher.yf.Ticker')
    def test_fetch_data(self, mock_ticker):
        fetcher = YahooFinanceDataFetcher()
        # Mock the Ticker object's history method
        mock_ticker_instance = MagicMock()
        mock_df = pd.DataFrame({'close': [100, 200]})
        mock_ticker_instance.history.return_value = mock_df
        mock_ticker.return_value = mock_ticker_instance

        # Call the method
        symbol = 'AAPL'
        df = fetcher.fetch_data(symbol)

        # Assertions
        mock_ticker.assert_called_once_with(symbol)
        mock_ticker_instance.history.assert_called_once()
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertIn('close', df.columns)

if __name__ == '__main__':
    unittest.main()
