from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from app.services.scraper import scrape_jobs
from app.db import save_job, get_all_jobs

router = APIRouter()

@router.get("/", summary="List all saved job applications")
def list_saved_jobs():
    """
    Returns all jobs saved in the database.
    """
    try:
        return {"jobs": get_all_jobs()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/search", summary="Search jobs online")
def search_jobs(
    keyword: str = Query(..., description="Keyword for job search, e.g., 'Python Developer'"),
    location: Optional[str] = Query(None, description="Location for job search, e.g., 'New York'"),
    max_results: int = Query(10, ge=1, le=50, description="Maximum jobs to fetch")
):
    """
    Scrapes jobs from online job boards based on keyword and location.
    """
    try:
        jobs = scrape_jobs(keyword, location, max_results)
        return {"results": jobs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/save", summary="Save a job application")
def save_job_entry(job: dict):
    """
    Saves a job entry to the database.
    """
    try:
        result = save_job(job)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
