"""Simple script to download price data for S&P 500 changes.

This example relies on the ``data.src.sp500`` utilities already present in
this repository. It queries Wikipedia for all tickers that have changed
membership in the S&P 500 within a given time window and then downloads price
history for those tickers. The resulting data is written to ``data.csv``.
"""

from sp500 import _parse_wikipedia_changes, fetch_price_history


def main(months: int = 12) -> None:
    """Download historical prices for recently changed S&P 500 tickers."""
    # ``_parse_wikipedia_changes`` returns tickers that were either added to or
    # removed from the index within the last ``months`` months.
    tickers = _parse_wikipedia_changes(months)

    if not tickers:
        print("No ticker changes found for the given period.")
        return

    # Download historical prices for all of the symbols at once.
    data = fetch_price_history(tickers, months)
    data.to_csv("data.csv", index=True)


if __name__ == "__main__":
    main()
