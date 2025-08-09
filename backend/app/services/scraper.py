# backend/app/services/scraper.py

import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from datetime import datetime

def scrape_indeed(keyword: str, location: str, max_results: int = 10) -> List[Dict]:
    """
    Scrapes Indeed for job postings.
    
    Args:
        keyword (str): Search keyword (e.g., 'Python Developer')
        location (str): Job location
        max_results (int): Maximum number of jobs to scrape

    Returns:
        List[Dict]: A list of job data dictionaries
    """

    jobs = []
    base_url = "https://www.indeed.com/jobs"
    params = {"q": keyword, "l": location, "limit": 10}

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        for job_card in soup.select(".result")[:max_results]:
            title_elem = job_card.select_one(".jobTitle span")
            company_elem = job_card.select_one(".companyName")
            location_elem = job_card.select_one(".companyLocation")
            description_elem = job_card.select_one(".job-snippet")
            date_elem = job_card.select_one(".date")

            job = {
                "title": title_elem.get_text(strip=True) if title_elem else "No Title",
                "company": company_elem.get_text(strip=True) if company_elem else "Unknown Company",
                "location": location_elem.get_text(strip=True) if location_elem else "Not Specified",
                "description": description_elem.get_text(strip=True) if description_elem else "",
                "date_posted": date_elem.get_text(strip=True) if date_elem else datetime.today().strftime("%Y-%m-%d"),
            }
            jobs.append(job)

    except Exception as e:
        print(f"Error scraping Indeed: {e}")

    return jobs

def scrape_all(keyword: str, location: str, max_results: int = 10) -> List[Dict]:
    """
    Aggregates job results from multiple scrapers.
    Currently supports only Indeed.
    """
    all_jobs = []
    indeed_jobs = scrape_indeed(keyword, location, max_results)
    all_jobs.extend(indeed_jobs)

    # Placeholder for future scrapers (LinkedIn, Glassdoor, etc.)
    return all_jobs
