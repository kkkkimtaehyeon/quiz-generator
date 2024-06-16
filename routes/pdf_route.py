from fastapi import APIRouter, UploadFile, File, Form
from typing import Annotated
from models.pdf import Pdf
from domain.aws import S3
from schema.pdf_schemas import fetch_pdfs, insert_pdf, delete_pdf
from bson import ObjectId

router = APIRouter(tags=["pdf"])

s3 = S3()

@router.get("/")
async def get_pdfs():
    pdfs = fetch_pdfs()
    return pdfs

@router.post("/")
async def post_pdf(name: Annotated[str, Form()], file: Annotated[UploadFile, File()]):
    key = s3.upload_pdf(file)
    pdf = Pdf(name=name, key = key)
    insert_pdf(dict(pdf))

# PDF 수정
# @router.put("/{id}")
# async def put_pdf(id:str, pdf:Pdf):
#     pdf_collection.find_one_and_update(
#         {"_id": ObjectId(id)},
#         {"$set": dict(pdf)}
#         )

# PDF 삭제
@router.delete("/{key}")
async def delete_pdf(key:str):
    s3.delete_pdf(key)
    delete_pdf(key)