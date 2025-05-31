# Time Series Prediction Platform

This project is a Time Series Prediction Platform that allows users to upload, manage, and predict time series data through a web interface, REST API, and Python SDK.

## Features

- **Web Interface**: Upload new data sources, view available datasets, and request predictions via a user-friendly web UI.
- **REST API**: FastAPI backend provides endpoints to manage data sources, access standard datasets, and get predictions.
- **Python SDK**: Easily interact with the platform programmatically from Python applications.

## Project Structure

```
src/
  main.py                # FastAPI backend server
  requirements.txt       # Backend dependencies
  static_html/
    index.html           # Web UI
  sdk/
    client.py            # Python SDK client
    setup.py             # SDK packaging
    __init__.py
  lib/
    fetchers.py
    http_fetcher.py
    yahoo_fetcher.py
  test/
    test_fetchers.py
    __init__.py
```

## Usage

### 1. Backend API
- Built with FastAPI (`main.py`).
- Endpoints:
  - `/data-sources` (GET): List uploaded data sources
  - `/data-sources/upload` (POST): Upload a new data source
  - `/standard-datasets` (GET): List standard datasets
  - `/predict` (GET): Get dummy predictions for a data source

### 2. Web Frontend
- Open `src/static_html/index.html` in your browser for a simple UI to interact with the backend.

### 3. Python SDK
- Use the SDK in `src/sdk/client.py` to interact with the API from Python code.

#### Example usage:
```python
from timeseries_sdk import TimeSeriesClient
client = TimeSeriesClient(base_url="http://localhost:8000")
print(client.list_data_sources())
```

## Installation & Running

1. **Install backend dependencies:**
   ```bash
   pip install -r src/requirements.txt
   ```
2. **Run the backend server:**
   ```bash
   uvicorn src.main:app --reload
   ```
3. **Open the frontend:**
   - Open `src/static_html/index.html` in your browser.

## Running Unit Tests

To run the unit tests for this project, use the following command from the project root:

```bash
python -m unittest discover -s src/test -p 'test_*.py'
```

Or, to run all tests in the main source directory:

```bash
python -m unittest discover -s src -p 'test_*.py'
```

This will automatically discover and run all test files matching the pattern `test_*.py`.

## Notes
- The prediction endpoint currently returns dummy data.
- Standard datasets are hardcoded for demonstration.

## License
MIT License
