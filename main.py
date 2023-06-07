import requests
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel


class QuestionParam(BaseModel):
    questions_num: int

class Question(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/quiz/")
def get_questions(payload: QuestionParam) -> list[Question]:
    questions_num = payload.questions_num
    params = {"count": questions_num}
    service_response = requests.get(
        "https://jservice.io/api/random",
        params=params, 
        timeout=10
    )
    service_response.raise_for_status()
    quiz = service_response.json()
    return quiz
