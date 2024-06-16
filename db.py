from pymongo import MongoClient

client = MongoClient("mongodb+srv://pdfessor:pdfessor1927@cluster-quiz.rhaoexv.mongodb.net/")

db = client.pdf_db

pdf_collection = db['pdf_collection']
quiz_collection = db['quiz_collection']