from fastapi import APIRouter
from models.quiz import QuizRequest
from domain.quiz import create_quiz
router = APIRouter()

@router.post("/new")
async def post_quiz(quiz: QuizRequest):
    return await create_quiz(quiz)