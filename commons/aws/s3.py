import boto3
import os
import io
import uuid
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

class S3:
    def __init__(self) -> None:
        pass

    S3_BUCKET = os.getenv('AWS_S3_BUCKET')
    S3_REGION = os.getenv('AWS_S3_REGION')

    client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_S3_ACCESS_KEY'),
        aws_secret_access_key=os.getenv('AWS_S3_SECRET_KEY')
    )

    def get_pdf_file_stream(self, key):
        obj = self.get_object(Bucket=self.S3_BUCKET, Key=key)
        return io.BytesIO(obj['Body'].read())

    def generate_objectkey(self, file):
        filename = file.filename
        return f"{uuid.uuid4()}_{filename}"