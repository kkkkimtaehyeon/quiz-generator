from db import pdf_collection

def fetch_pdf(pdf) -> dict:
    return {
        "id": str(pdf['_id']),
        "name": pdf.get('name', ''),
        "key": pdf.get('key', '')
    }

def fetch_pdfs() -> list:
    pdfs = pdf_collection.find()
    #특정 pdf로 생성한 문제들을 find 해야함.
    #pdfs = pdf_collection.find({"_id": ObjectId(id)})
    return [fetch_pdf(pdf) for pdf in pdfs]

def insert_pdf(pdf):
    pdf_collection.insert_one(dict(pdf))

def delete_pdf(key):
    pdf_collection.find_one_and_delete({"key": key})