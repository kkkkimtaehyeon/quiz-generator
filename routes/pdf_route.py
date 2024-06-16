from fastapi import APIRouter, UploadFile, File, Form
from typing import Annotated
from models.pdf import Pdf
from domain.aws import S3
from db import pdf_collection
from schema.schemas import list_serial
from bson import ObjectId
import urllib

router = APIRouter()

s3 = S3()

@router.get("/")
async def get_pdfs():
    pdfs = list_serial(pdf_collection.find())
    return pdfs

@router.post("/")
async def post_pdf(name: Annotated[str, Form()], file: Annotated[UploadFile, File()]):
    key = s3.upload_pdf(file)
    pdf = Pdf(name=name, key = key)
    pdf_collection.insert_one(dict(pdf))

@router.put("/{id}")
async def put_pdf(id:str, pdf:Pdf):
    pdf_collection.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(pdf)}
        )

@router.delete("/{key}")
async def delete_pdf(key:str):
    s3.delete_pdf(key)
    pdf_collection.find_one_and_delete({"key": key})

    #pdf_collection.find_one_and_delete({"_id": ObjectId(id)})