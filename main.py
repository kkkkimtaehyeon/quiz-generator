from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from commons.aws.s3 import upload_pdf
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

@app.post("/")
async def root(file: UploadFile):
    return upload_pdf(file)