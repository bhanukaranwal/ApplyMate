from pydantic import BaseModel
from typing import Optional

class JobPostCreate(BaseModel):
    title: str
    company: str
    url: str
    description: str
    location: Optional[str] = None

class ApplicationCreate(BaseModel):
    job_id: int
    notes: Optional[str] = None
