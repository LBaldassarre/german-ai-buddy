from pydantic import BaseModel
from datetime import datetime


class PostTest(BaseModel):
    title: str
    content: str

class UserT(BaseModel):
    username: str
    cefr_level: str
    native_language: str
    interface_language: str
    learning_language: str

class SessionEndT(BaseModel):
    id: str
    user_id: str
    topic: str
    session_type: str
    started_at: datetime

class MessageT(BaseModel):
    user_id: str
    session_id: str
    role: str

class MistakeT(BaseModel):
    user_id: str
    session_id: str
    message_id: str
    original_text: str
    corrected_text: str
    category: str
    expanation: str
    severity: int

class VocabularyT(BaseModel):
    user_id: str
    word: str
    translation: str
    exposure_count: int
    confidece_score: float
    last_seen: datetime

class SessionSummaryT(BaseModel):
    user_id: str
    session_id: str
    summary: str
    strengths: str
    weaknesses: str
    suggested_focus: str