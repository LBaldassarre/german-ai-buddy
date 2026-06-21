from pydantic import BaseModel
import uuid

class Message(BaseModel):
    user_id: uuid.UUID
    session_id: uuid.UUID
    promt: str
    response: str
    role: str