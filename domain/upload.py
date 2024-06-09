from fastapi import APIRouter, File, UploadFile, Form
from typing import Annotated
from commons.aws.s3 import S3

router = APIRouter(
    tags=["upload"]
)


@router.post("")
async def upload(customFilename: Annotated[str, Form()], file: Annotated[UploadFile, File()]):
    return {
        "file": customFilename
    }
    #return upload_pdf(file)


s3 = S3()


def upload_pdf(file):
    key = s3.generate_objectkey(file)
    s3.put_object(Body=file.file, Bucket=s3.S3_BUCKET, Key=key, ContentType='application/pdf')
    return f'https://{s3.S3_BUCKET}.s3.{s3.S3_REGION}.amazonaws.com/{key}'
