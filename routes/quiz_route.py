from fastapi import APIRouter
from models.quiz import QuizRequest
from domain.quiz import create_quiz
from schema.quiz_schemas import insert_quiz
router = APIRouter()

@router.post("")
async def post_quiz(quiz: QuizRequest):
    created_quiz = create_quiz(quiz)
    return created_quiz
    # quiz_obj_mutiple={
    #     "question": "도커 컨테이너를 생성하기 위해서는 무엇이 필요한가?",
    #     "options": {
    #         "1": "도커 이미지",
    #         "2": "도커 파일",
    #         "3": "도커 컴포즈",
    #         "4": "도커 네트워크"
    #     },
    #     "answer": "1"
    # }

    # quiz_obj_single={
    #     "question": "도커 컨테이너를 생성하기 위해서는 무엇이 필요한가?",
    #     "answer": "도커 이미지"
    # }
    # insert_quiz(quiz_obj_mutiple)