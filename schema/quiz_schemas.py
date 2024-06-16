from db import quiz_collection

def insert_quiz(quiz):
    quiz_collection.insert_one(quiz)
