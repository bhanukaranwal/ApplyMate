import requests
from bs4 import BeautifulSoup
from typing import List, Optional

BASE_URLS = {
    "indeed": "https://www.indeed.com/jobs?q={keyword}&l={location}&limit={limit}",
    "weworkremotely": "https://weworkremotely.com/remote-jobs/search?term={keyword}"
}

def scrape_jobs(keyword: str, location: Optional[str] = None, max_results: int = 10) -> List[dict]:
    """
    Scrapes job listings from supported job boards.
    Currently supports Indeed and WeWorkRemotely.
    """
    jobs = []

    # Scrape Indeed
    if location:
        indeed_url = BASE_URLS["indeed"].format(keyword=keyword.replace(" ", "+"), location=location.replace(" ", "+"), limit=max_results)
    else:
        indeed_url = BASE_URLS["indeed"].format(keyword=keyword.replace(" ", "+"), location="", limit=max_results)

    try:
        resp = requests.get(indeed_url, headers={"User-Agent": "Mozilla/5.0"})
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "html.parser")
            for card in soup.select(".result")[:max_results]:
                title_elem = card.select_one("h2 a")
                company_elem = card.select_one(".company")
                location_elem = card.select_one(".location")
                link = "https://www.indeed.com" + title_elem.get("href") if title_elem else None
                jobs.append({
                    "title": title_elem.text.strip() if title_elem else "N/A",
                    "company": company_elem.text.strip() if company_elem else "N/A",
                    "location": location_elem.text.strip() if location_elem else location or "Remote",
                    "link": link
                })
    except Exception as e:
        print(f"Indeed scraping error: {e}")

    # Scrape WeWorkRemotely
    try:
        wwr_url = BASE_URLS["weworkremotely"].format(keyword=keyword.replace(" ", "+"))
        resp = requests.get(wwr_url, headers={"User-Agent": "Mozilla/5.0"})
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.text, "html.parser")
            for job_elem in soup.select("section.jobs li a")[:max_results]:
                title = job_elem.select_one("span.title")
                company = job_elem.select_one("span.company")
                link = "https://weworkremotely.com" + job_elem.get("href") if job_elem else None
                if title and company:
                    jobs.append({
                        "title": title.text.strip(),
                        "company": company.text.strip(),
                        "location": "Remote",
                        "link": link
                    })
    except Exception as e:
        print(f"WeWorkRemotely scraping error: {e}")

    return jobs
