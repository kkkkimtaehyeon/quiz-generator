from pydantic import BaseModel
from typing import Optional, List
class QuizRequest(BaseModel):
    pdf: str
    type: str
    size: int

class Questions(BaseModel):
    question: str
    options: Optional[dict]
    answer: str

class Quiz(BaseModel):
    title: str
    questions: List[Questions]


quiz_dummy_data={
    "id":"1",
    "title": "첫번째 퀴즈",
    "questions":[
        {
            "id": "1",
            "question": "도커 컨테이너를 생성하기 위해서는 무엇이 필요한가?",
            "options": {
                "1": "도커 이미지",
                "2": "도커 파일",
                "3": "도커 컴포즈",
                "4": "도커 네트워크"
            },
            "answer": "1"
        },
        {
            "id": "2",
            "question": "도커 컨테이너를 생성하기 위해서는 무엇이 필요한가?",
            "options": {},
            "answer": "도커 이미지"
        }
    ]
}