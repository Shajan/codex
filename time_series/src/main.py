from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import StreamingResponse
from typing import List

from .data_fetcher import DataFetcher
from lib.fetchers import CSVDataFetcher, TSVDataFetcher
from lib.http_fetcher import HTTPPaginatedDataFetcher
from lib.yahoo_fetcher import YahooFinanceDataFetcher

app = FastAPI()

data_sources = {}
standard_datasets = {
    "us_stock_market": "US Stock Market Index Data",
    "gdp_countries": "GDP Data from Various Countries",
    "money_supply": "Money Supply Data"
}

@app.get("/")
def read_root():
    return {"message": "Time Series Prediction Platform API"}

@app.get("/data-sources")
def list_data_sources():
    return list(data_sources.keys())

@app.post("/data-sources/upload")
def upload_data_source(name: str = Form(...), file: UploadFile = File(...)):
    data_sources[name] = file.filename
    return {"message": f"Data source '{name}' uploaded."}

@app.get("/predict")
def get_prediction(data_source: str, steps: int = 10):
    # Dummy prediction
    return {"data_source": data_source, "predictions": [0.0] * steps}

@app.get("/standard-datasets")
def get_standard_datasets():
    return standard_datasets
