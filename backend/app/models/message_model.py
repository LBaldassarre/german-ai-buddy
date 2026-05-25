from pydantic import BaseModel

class Message(BaseModel):
    user_id: str
    session_id: str
    role: str