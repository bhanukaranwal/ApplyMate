from sqlmodel import SQLModel, Field
from typing import Optional
import datetime

class JobPost(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    external_id: Optional[str] = None
    title: str
    company: str
    location: Optional[str] = None
    url: str
    description: str
    created_at: str = Field(default_factory=lambda: datetime.datetime.utcnow().isoformat())

class Application(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    job_id: int
    status: str = "to_apply"  # to_apply / applied / interviewing / offer / rejected
    applied_at: Optional[str] = None
    notes: Optional[str] = None
