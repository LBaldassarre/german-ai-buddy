from pydantic import BaseModel
from datetime import datetime


class Vocabulary(BaseModel):
    user_id: str
    word: str
    translation: str
    exposure_count: int
    confidece_score: float
    last_seen: datetime