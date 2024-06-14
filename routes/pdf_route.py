from fastapi import APIRouter, UploadFile, File, Form
from typing import Annotated
from models.pdf import Pdf
from domain.aws import S3
from db import collection_name
from schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

s3 = S3()

@router.get("/")
async def get_pdfs():
    pdfs = list_serial(collection_name.find())
    return pdfs

@router.post("/")
async def post_pdf(name: Annotated[str, Form()], file: Annotated[UploadFile, File()]):
    url = s3.upload_pdf(file)
    pdf = Pdf(name=name, url = url)
    collection_name.insert_one(dict(pdf))

@router.put("/{id}")
async def put_pdf(id:str, pdf:Pdf):
    collection_name.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(pdf)}
        )

@router.delete("/{id}")
async def delete_pdf(id:str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})