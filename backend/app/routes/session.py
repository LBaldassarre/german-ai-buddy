from fastapi import APIRouter, Depends
from app.models import session_model
from app.services.session_service import SessionService
from app.db.schema import async_session_maker

router = APIRouter()

def get_session_service() -> SessionService:
    return SessionService(session=async_session_maker())

@router.get("/get-session")
async def get_sessions(service: SessionService = Depends(get_session_service)):
    return await service.list_sessions()

@router.post("/create-session")
async def create_session(user_id:str, service: SessionService = Depends(get_session_service)):
    return await service.create_session(user_id)


@router.patch("/end-session/{session_id}")
async def end_session(session_id:str, service: SessionService = Depends(get_session_service)):
    return await service.end_session(session_id)