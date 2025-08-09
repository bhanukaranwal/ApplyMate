import requests
from bs4 import BeautifulSoup
from typing import Optional, List, Dict
import urllib.parse

BASE_URL = "https://www.indeed.com/jobs"

def scrape_jobs(keyword: str, location: Optional[str] = None, max_results: int = 10) -> List[Dict]:
    """
    Scrapes job listings from Indeed based on a keyword and optional location.
    Returns a list of dictionaries containing job details.
    """
    jobs = []
    query_params = {
        "q": keyword,
        "l": location or "",
        "limit": max_results
    }
    search_url = f"{BASE_URL}?{urllib.parse.urlencode(query_params)}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/115.0.0.0 Safari/537.36"
    }
    
    response = requests.get(search_url, headers=headers, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")

    for card in soup.find_all("div", class_="job_seen_beacon")[:max_results]:
        title_elem = card.find("h2", class_="jobTitle")
        company_elem = card.find("span", class_="companyName")
        location_elem = card.find("div", class_="companyLocation")
        summary_elem = card.find("div", class_="job-snippet")
        link_elem = title_elem.find("a") if title_elem else None

        job_data = {
            "title": title_elem.get_text(strip=True) if title_elem else "N/A",
            "company": company_elem.get_text(strip=True) if company_elem else "N/A",
            "location": location_elem.get_text(strip=True) if location_elem else "N/A",
            "summary": summary_elem.get_text(strip=True) if summary_elem else "N/A",
            "link": f"https://www.indeed.com{link_elem['href']}" if link_elem and link_elem.has_attr("href") else None
        }
        jobs.append(job_data)

    return jobs
