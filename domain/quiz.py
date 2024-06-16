import fitz
import os
from openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate
from domain.aws import S3
from dotenv import load_dotenv, find_dotenv
import json

from models.quiz import QuizRequest

_ = load_dotenv(find_dotenv())

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)
s3 = S3()

def read_pdf(key):
    file_stream = s3.get_pdf_file_stream(key)
    doc = fitz.open(stream=file_stream)
    text = ''
    for page in doc:
        text += page.get_text()
    return text

pdf_text = read_pdf("ead3d502-4b6b-4bba-b893-95eb9743a835_aws.pdf")

def multiple_prompt(size):
    return f"""
    너는 텍스트를 읽어서 문제와 문제의 답을 json으로 생성하는 봇이야.
    문제의 여러 개이면 최대한 중복되지 않고 다양하게 문서의 순서에 상관없이 랜덤하게 문제를 생성해.
    문제는 객관식 형태로 {size}개 생성해.
    문제의 key는 question이야.

    문제가 여러 개일 때는 question들을 questions 리스트로 감싸.
    문제 형태가 객관식일 때: 보기들은 options로 묶어.
    각 option들은 1~4까지의 리스트야.

    문제의 답인 answer은 option의 key 값 중 하나이고, 모든 문제에는 답이 필수적으로 있어야 돼.
    
    
    텍스트에 써지지 않은 내용에 대해서는 언급도 하지말고 함부로 문제를 생성하지마.
    문제의 형태에 맞는 답을 생성해.
    """

def single_prompt(size):
    return f"""
    너는 텍스트를 읽어서 문제와 문제의 답을 json으로 생성하는 봇이야.
    문제의 여러 개이면 최대한 중복되지 않고 다양하게 문서의 순서에 상관없이 랜덤하게 문제를 생성해.
    문제는 주관식 형태로 {size}개 생성해.
    문제의 key는 question이야.

    답은 하나의 짧은 단어야.
    문제의 답은 answer이고 모든 문제에는 답이 필수적으로 있어야 돼.
    
    텍스트에 써지지 않은 내용에 대해서는 언급도 하지말고 함부로 문제를 생성하지마.
    문제의 형태에 맞는 답을 생성해.
    """

def select_prompt(type, size):
    if type == "객관식":
        return multiple_prompt(size)
    elif type == "주관식":
        return single_prompt(size)

# response = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     temperature=0.1,
#     response_format = {"type": "json_object"},
#     messages=[
#     {"role": "system", "content": select_prompt("객관식", 1)},
#     {"role": "user", "content": pdf_text}
#   ]
# )


# print(response.choices[0].message.content)


# 퀴즈 생성
def create_quiz(quiz: QuizRequest):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.1,
        response_format = {"type": "json_object"}, 
        messages=[
        {"role": "system", "content": select_prompt(quiz.type, quiz.size)},
        {"role": "user", "content": read_pdf(quiz.pdf)}
        ]
    )

    return json.loads(response.choices[0].message.content)




#read_pdf("3296e43b-06f0-40cb-858e-154f7aef86a1_클라우드_요약정리.pdf")

