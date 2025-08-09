from fastapi import APIRouter, Query
from typing import List, Optional
from app.services.scraper import scrape_jobs
from app.db import save_job, get_all_jobs

router = APIRouter()

@router.get("/", summary="Get all saved job applications")
def list_jobs():
    """
    Returns all jobs saved in the database.
    """
    return get_all_jobs()

@router.get("/search", summary="Search jobs from the web")
def search_jobs(
    keyword: str = Query(..., description="Keyword for job search, e.g., 'Python Developer'"),
    location: Optional[str] = Query(None, description="Job location, e.g., 'New York'"),
    max_results: int = Query(10, ge=1, le=50, description="Max number of jobs to fetch")
):
    """
    Scrapes jobs from supported job boards and returns results.
    """
    jobs = scrape_jobs(keyword, location, max_results)
    return {"results": jobs}

@router.post("/save", summary="Save a job application to database")
def save_job_entry(job: dict):
    """
    Saves a job entry to the database.
    """
    return save_job(job)
