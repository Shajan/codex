# S&P 500 Stable Constituents Project

This project provides utilities to fetch a list of S&P 500 tickers that were
part of the index for a continuous time range (24 months by default), download
historical daily open and close prices, convert them to epoch based timestamps
and pivot the data into a time series table.

The code relies on `pandas` for data manipulation and `yfinance` for stock
prices. Network access is required for runtime because the data is fetched from
Wikipedia and Yahoo Finance.

## Project Structure

```
data/
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   └── sp500.py
└── tests/
    ├── __init__.py
    └── test_sp500.py
```

## Installation

Install the requirements with pip:

```bash
pip install -r requirements.txt
```

## Usage

The `src/sp500.py` module exposes these main functions:

- `get_sp500_tickers(months=24)` - Return S&P 500 tickers that have been part
  of the index for the last `months` months.
- `fetch_price_history(tickers, months=24)` - Download daily open and close
  prices using Yahoo Finance.
- `prepare_time_series(df)` - Convert the price history into a time-indexed
  table with epoch seconds for open and close times.

Example:

```python
from data.src.sp500 import get_sp500_tickers, fetch_price_history, prepare_time_series

tickers = get_sp500_tickers(24)
prices = fetch_price_history(tickers, 24)
time_series = prepare_time_series(prices)
```

## Testing

Run unit tests with `pytest`:

```bash
pytest
```

Network calls are mocked in the tests so they do not require internet access.
