import boto3
import os
import io
import uuid
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

S3_BUCKET = os.getenv('AWS_S3_BUCKET')
S3_REGION = os.getenv('AWS_S3_REGION')

s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_S3_ACCESS_KEY'),
    aws_secret_access_key=os.getenv('AWS_S3_SECRET_KEY')
)

def upload_pdf(file):
    key = generate_objectkey(file)
    s3.put_object(Body=file.file, Bucket=S3_BUCKET, Key=key, ContentType='application/pdf')
    return f'https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{key}'

def get_pdf_file_stream(key):
    obj = s3.get_object(Bucket=S3_BUCKET, Key=key)
    return io.BytesIO(obj['Body'].read())

def generate_objectkey(file):
    filename = file.filename
    return f"{uuid.uuid4()}_{filename}"