from pydantic import BaseModel
from typing import Optional
class Pdf(BaseModel):
    name: str
    url: Optional[str]