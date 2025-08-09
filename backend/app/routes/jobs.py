# backend/app/routes/jobs.py

from fastapi import APIRouter, Query, HTTPException
from typing import List
from app.services import scraper, database

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.get("/", summary="Get all stored jobs")
def list_jobs():
    """Retrieve all jobs from the database."""
    return database.get_jobs()

@router.get("/{job_id}", summary="Get job details by ID")
def get_job(job_id: int):
    """Retrieve a single job's details."""
    job = database.get_job_by_id(job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.post("/scrape", summary="Scrape jobs from online boards")
def scrape_jobs(
    keyword: str = Query(..., description="Keyword for job search"),
    location: str = Query(..., description="Location for job search"),
    limit: int = Query(10, description="Number of jobs to fetch")
):
    """
    Scrape jobs using the scraper service and save them in the database.
    """
    jobs = scraper.scrape_all(keyword, location, limit)
    for job in jobs:
        database.add_job(
            title=job["title"],
            company=job["company"],
            location=job["location"],
            description=job["description"],
            date_posted=job["date_posted"]
        )
    return {"message": f"Added {len(jobs)} jobs to database.", "jobs": jobs}
