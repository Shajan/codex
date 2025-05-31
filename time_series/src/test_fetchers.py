import unittest
import pandas as pd
import os
import sys
import pathlib

# Add the src directory to sys.path for absolute imports
SRC_PATH = str(pathlib.Path(__file__).parent)
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

from fetchers import CSVDataFetcher, TSVDataFetcher
from http_fetcher import HTTPPaginatedDataFetcher
from yahoo_fetcher import YahooFinanceDataFetcher
from unittest.mock import patch, MagicMock

# All fetcher tests have been moved to src/test/test_fetchers.py

if __name__ == '__main__':
    unittest.main()
