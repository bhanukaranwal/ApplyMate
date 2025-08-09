from abc import ABC, abstractmethod
from typing import List, Dict

class BaseScraper(ABC):
    @abstractmethod
    def scrape(self) -> List[Dict]:
        """Return list of job dicts with keys: title, company, url, description, location"""
        pass
