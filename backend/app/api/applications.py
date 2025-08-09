from fastapi import APIRouter
from ..schemas import ApplicationCreate
from ..models import Application
from ..db import get_session

router = APIRouter(prefix='/api/applications', tags=['applications'])

@router.post('/')
async def create_application(payload: ApplicationCreate):
    with next(get_session()) as session:
        app = Application(job_id=payload.job_id, notes=payload.notes)
        session.add(app)
        session.commit()
        session.refresh(app)
        return app

@router.get('/')
async def list_applications():
    with next(get_session()) as session:
        apps = session.exec(select(Application)).all()
        return apps
