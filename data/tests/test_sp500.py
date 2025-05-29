import pandas as pd
from unittest import mock

import data.src.sp500 as sp500


def test_get_sp500_tickers():
    constituents = pd.DataFrame({"Symbol": ["AAA", "BBB", "CCC"]})
    changes = pd.DataFrame({
        "Date": ["2024-01-01"],
        "Added": ["BBB"],
        "Removed": [None],
    })

    tables = [constituents, changes]
    with mock.patch("data.src.sp500.pd.read_html", return_value=tables):
        tickers = sp500.get_sp500_tickers(24)
    assert tickers == ["AAA", "CCC"]


def test_prepare_time_series():
    index = pd.to_datetime(["2024-01-01", "2024-01-02"])
    df = pd.DataFrame({
        "Open": [1, 3],
        "Close": [2, 4],
        "Ticker": ["AAA", "AAA"],
    }, index=index)

    ts = sp500.prepare_time_series(df)
    assert ts.shape[0] == 4
    assert list(ts.columns) == ["AAA"]
