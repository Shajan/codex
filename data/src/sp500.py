from __future__ import annotations

import datetime as dt
from typing import Iterable, List
from zoneinfo import ZoneInfo

import pandas as pd
import yfinance as yf


WIKI_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
OPEN_TIME = dt.time(9, 30)
CLOSE_TIME = dt.time(16, 0)
EASTERN = ZoneInfo("US/Eastern")


def _parse_wikipedia_changes(months: int) -> List[str]:
    """Return tickers that changed membership in the last ``months`` months."""
    tables = pd.read_html(WIKI_URL)
    changes = []
    cutoff = dt.datetime.now() - dt.timedelta(days=30 * months)
    for df in tables:
        if df.columns[0].startswith("Date") and {"Added", "Removed"}.issubset(df.columns):
            # historical change table
            for _, row in df.iterrows():
                date = pd.to_datetime(row["Date"], errors="coerce")
                if pd.isna(date) or date < cutoff:
                    continue
                added = row.get("Added")
                removed = row.get("Removed")
                if pd.notna(added):
                    changes.append(added)
                if pd.notna(removed):
                    changes.append(removed)
    return list(set(changes))


def get_sp500_tickers(months: int = 24) -> List[str]:
    """Return tickers that have been in the S&P 500 for ``months`` months."""
    tables = pd.read_html(WIKI_URL)
    constituents = tables[0]["Symbol"].tolist()
    changed = _parse_wikipedia_changes(months)
    return [t for t in constituents if t not in changed]


def fetch_price_history(tickers: Iterable[str], months: int = 24) -> pd.DataFrame:
    """Download daily open/close prices for ``tickers`` for ``months`` months."""
    period = f"{months}mo"
    data = yf.download(",".join(tickers), period=period, auto_adjust=False, group_by="ticker")
    # Normalize into long format DataFrame
    frames = []
    for ticker in tickers:
        df = data[ticker].copy()
        df["Ticker"] = ticker
        frames.append(df[["Open", "Close", "Ticker"]])
    df_all = pd.concat(frames, keys=tickers, names=["Ticker", "Date"])
    df_all.reset_index(level=0, inplace=True)
    return df_all


def _to_epoch(d: dt.date, t: dt.time) -> int:
    dt_obj = dt.datetime.combine(d, t, tzinfo=EASTERN).astimezone(dt.timezone.utc)
    return int(dt_obj.timestamp())


def prepare_time_series(df: pd.DataFrame) -> pd.DataFrame:
    """Convert price history into pivot table with epoch seconds index."""
    rows = []
    for date, group in df.groupby(df.index):
        for _, row in group.iterrows():
            epoch_open = _to_epoch(date, OPEN_TIME)
            epoch_close = _to_epoch(date, CLOSE_TIME)
            rows.append({"time": epoch_open, "ticker": row["Ticker"], "price": row["Open"]})
            rows.append({"time": epoch_close, "ticker": row["Ticker"], "price": row["Close"]})
    out = pd.DataFrame(rows)
    pivot = out.pivot(index="time", columns="ticker", values="price").sort_index()
    pivot = pivot.dropna(axis=1, how="any")
    return pivot
