from fastapi import APIRouter
from models.quiz import QuizRequest
from domain.quiz import create_quiz
from schema.quiz_schemas import insert_quiz, fetch_quizzes, fetch_this_quiz
from db import quiz_collection
router = APIRouter(tags=["quiz"])

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

@router.get("")
async def get_quizzes():
    quizzes = fetch_quizzes()
    return quizzes

@router.get("/{id}")
async def get_quiz(id: str):
    quiz = fetch_this_quiz(id)
    return quiz