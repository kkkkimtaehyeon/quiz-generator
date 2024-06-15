from pydantic import BaseModel

class QuizRequest(BaseModel):
    pdf: str
    type: str
    size: int
    