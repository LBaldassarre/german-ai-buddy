from fastapi import APIRouter
from app.models.message_model import Message
from app.services.message_service import MessageService
from app.db.schema import async_session_maker
from pydantic import BaseModel

class PromptRequest(BaseModel):
    prompt: str


router = APIRouter()

def get_message_service() -> MessageService:
    return MessageService(session=async_session_maker())

@router.post("/message/send-message")
async def send_message(promt) -> Message:
    message_service = get_message_service()
    return await message_service.send_message(promt=promt)