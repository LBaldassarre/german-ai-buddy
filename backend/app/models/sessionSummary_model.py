from pydantic import BaseModel


class SessionSummary(BaseModel):
    user_id: str
    session_id: str
    summary: str
    strengths: str
    weaknesses: str
    suggested_focus: str