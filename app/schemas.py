from pydantic import BaseModel
from typing import Optional

class AskRequest(BaseModel):
    user_id: str
    topic: str
    explanation_level: str  # e.g. "beginner", "intermediate", "advanced"
    detail_level: Optional[str] = None

class AskResponse(BaseModel):
    reply: str
    model: str
