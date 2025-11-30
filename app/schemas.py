from pydantic import BaseModel

class AskRequest(BaseModel):
    user_id: str
    topic: str
    explanation_level: str  # e.g. "beginner", "intermediate", "advanced"
    detail_level: str

class AskResponse(BaseModel):
    reply: str
    model: str
