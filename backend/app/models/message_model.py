from pydantic import BaseModel
import uuid

class Message(BaseModel):
    user_id: uuid.UUID
    session_id: uuid.UUID
    prompt: str
    answer: str
    role: str

class SendMessageRequest(BaseModel):
    prompt: str