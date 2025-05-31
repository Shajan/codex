from abc import ABC, abstractmethod
from typing import Any

class DataFetcher(ABC):
    @abstractmethod
    def fetch_data(self, *args, **kwargs) -> Any:
        """
        Fetch data from a data source.
        Returns:
            Any: The fetched data (e.g., pandas DataFrame, list, etc.)
        """
        pass
