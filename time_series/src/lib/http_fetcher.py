# Moved HTTPPaginatedDataFetcher from src/http_fetcher.py
import requests
import pandas as pd
from bs4 import BeautifulSoup
from data_fetcher import DataFetcher

class HTTPPaginatedDataFetcher(DataFetcher):
    def fetch_data(self, base_url: str, params: dict = None, next_page_selector: str = None, data_selector: str = None, max_pages: int = 10) -> pd.DataFrame:
        all_data = []
        url = base_url
        for _ in range(max_pages):
            resp = requests.get(url, params=params)
            soup = BeautifulSoup(resp.text, 'html.parser')
            rows = soup.select(data_selector) if data_selector else []
            for row in rows:
                all_data.append([cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])])
            next_link = soup.select_one(next_page_selector) if next_page_selector else None
            if not next_link or not next_link.get('href'):
                break
            url = next_link['href']
        return pd.DataFrame(all_data)
