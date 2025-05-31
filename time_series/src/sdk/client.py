import requests

class TimeSeriesClient:
    def __init__(self, base_url: str, api_key: str = None):
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.session = requests.Session()
        if api_key:
            self.session.headers.update({"Authorization": f"Bearer {api_key}"})

    def list_data_sources(self):
        url = f"{self.base_url}/data-sources"
        resp = self.session.get(url)
        resp.raise_for_status()
        return resp.json()

    def upload_data_source(self, name: str, file_path: str):
        url = f"{self.base_url}/data-sources/upload"
        with open(file_path, "rb") as f:
            files = {"file": (file_path, f)}
            data = {"name": name}
            resp = self.session.post(url, data=data, files=files)
        resp.raise_for_status()
        return resp.json()

    def get_prediction(self, data_source: str, steps: int = 10):
        url = f"{self.base_url}/predict"
        params = {"data_source": data_source, "steps": steps}
        resp = self.session.get(url, params=params)
        resp.raise_for_status()
        return resp.json()

    def get_standard_datasets(self):
        url = f"{self.base_url}/standard-datasets"
        resp = self.session.get(url)
        resp.raise_for_status()
        return resp.json()
