from fastapi import APIRouter, HTTPException
from ..db import get_session
from ..models import JobPost
from ..services.coverletter import generate_cover_letter

router = APIRouter(prefix='/api/generate', tags=['generate'])

@router.post('/cover-letter')
async def generate(job_id: int, resume_text: str, tone: str = 'professional'):
    with next(get_session()) as session:
        job = session.get(JobPost, job_id)
        if not job:
            raise HTTPException(status_code=404, detail='Job not found')
        letter = await generate_cover_letter(job.dict(), resume_text, tone)
        return { 'cover_letter': letter }
