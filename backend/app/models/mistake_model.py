from pydantic import BaseModel

class Mistake(BaseModel):
    user_id: str
    session_id: str
    message_id: str
    original_text: str
    corrected_text: str
    category: str
    expanation: str
    severity: int