import requests
from bs4 import BeautifulSoup
from .base import BaseScraper
from ..config import SCRAPE_USER_AGENT

class ExampleJobSiteScraper(BaseScraper):
    def __init__(self, base_url: str):
        self.base_url = base_url

    def scrape(self):
        headers = {"User-Agent": SCRAPE_USER_AGENT}
        r = requests.get(self.base_url, headers=headers, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        jobs = []
        for item in soup.select('.job')[:20]:
            title = item.select_one('.job-title').get_text(strip=True)
            company = item.select_one('.company').get_text(strip=True)
            url = item.select_one('a')['href']
            desc = item.select_one('.desc').get_text(strip=True)
            location = item.select_one('.location').get_text(strip=True) if item.select_one('.location') else None
            jobs.append({
                'title': title,
                'company': company,
                'url': url,
                'description': desc,
                'location': location,
            })
        return jobs
