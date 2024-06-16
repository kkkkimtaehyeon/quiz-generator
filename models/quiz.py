from pydantic import BaseModel
from typing import List, Dict
class QuizRequest(BaseModel):
    pdf: str
    type: str
    size: int

