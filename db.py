from pymongo import MongoClient

client = MongoClient("mongodb+srv://pdfessor:pdfessor1927@cluster-quiz.rhaoexv.mongodb.net/")

db = client.pdf_db

collection_name = db['pdf_collection']