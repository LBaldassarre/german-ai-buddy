from app.models.message_model import Message
from app.services.session_service import SessionService
from sqlalchemy.ext.asyncio import AsyncSession
from app.ai.gemini import GeminiAPI
from datetime import datetime
import uuid


class MessageService:
    def __init__(self, session: AsyncSession):
        self._db = session
        self._gemini = GeminiAPI()
    
    async def send_message(self, prompt) -> Message:
        # current_session = await SessionService.list_sessions()[0]
        answer = await self._gemini.gemini_response(prompt)

        message = Message( 
                    # user_id = current_session.user_id,
                    # session_id = current_session.id,
                    user_id = uuid.uuid4(),
                    session_id = uuid.uuid4(),
                    prompt = prompt,
                    answer = answer,
                    role = 'User'
                )
        
        return message
    

    
