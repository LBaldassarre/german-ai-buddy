from fastapi import APIRouter
from app.models.message_model import Message, SendMessageRequest
from app.services.message_service import MessageService
from app.db.schema import async_session_maker


router = APIRouter()

def get_message_service() -> MessageService:
    return MessageService(session=async_session_maker())

@router.post("/message/send-message")
async def send_message(request: SendMessageRequest) -> Message:
    message_service = get_message_service()
    return await message_service.send_message(prompt=request.prompt)