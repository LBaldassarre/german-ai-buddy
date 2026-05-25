from pydantic import BaseModel

class User(BaseModel):
    username: str
    cefr_level: str
    native_language: str
    interface_language: str
    learning_language: str