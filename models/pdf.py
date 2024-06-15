from pydantic import BaseModel
class Pdf(BaseModel):
    name: str
    key: str