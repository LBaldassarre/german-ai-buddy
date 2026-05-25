from pydantic import BaseModel
from datetime import datetime

class SessionEnd(BaseModel):
    id: str
    user_id: str
    topic: str
    session_type: str
    started_at: datetime