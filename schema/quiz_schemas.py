from db import quiz_collection

def fetch_this_quiz(id) -> dict:
    quiz = quiz_collection.find_one({"_id": str(id)})
    return {
        "id": str(quiz['_id']),
        "title": quiz.get('title', ''),
        "questions": quiz.get('questions', [])
    }

def fetch_quiz(quiz) -> dict:
    return {
        "id": str(quiz['_id']),
        "title": quiz.get('title', '')
    }

def fetch_quizzes() -> list:
    quizzes = quiz_collection.find()
    return [fetch_quiz(quiz) for quiz in quizzes]

def insert_quiz(quiz):
    quiz_collection.insert_one(dict(quiz))
