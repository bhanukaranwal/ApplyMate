from fastapi import APIRouter, Depends
from typing import List
from ..scrapers.example_jobsite import ExampleJobSiteScraper
from ..db import get_session
from ..models import JobPost

router = APIRouter(prefix="/api/jobs", tags=["jobs"])

@router.post('/scrape')
async def scrape_jobs(url: str):
    scraper = ExampleJobSiteScraper(url)
    jobs = scraper.scrape()
    # persist unique jobs
    inserted = 0
    from sqlmodel import select
    with next(get_session()) as session:
        for j in jobs:
            stmt = select(JobPost).where(JobPost.url == j['url'])
            if not session.exec(stmt).first():
                jp = JobPost(title=j['title'], company=j['company'], url=j['url'], description=j['description'], location=j.get('location'))
                session.add(jp)
                inserted += 1
        session.commit()
    return {"inserted": inserted}

@router.get('/')
async def list_jobs(q: str = None):
    from sqlmodel import select
    with next(get_session()) as session:
        stmt = select(JobPost)
        if q:
            stmt = select(JobPost).where(JobPost.title.contains(q) | JobPost.description.contains(q))
        rows = session.exec(stmt).all()
        return rows
