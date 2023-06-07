from datetime import datetime

import requests

from fastapi import FastAPI, Depends, HTTPException

from sqlalchemy.orm import Session
from pydantic import parse_obj_as

from database import engine, SessionLocal
from schemas import QuestionParam, Question
from crud import get_question, get_previous_question, create_question
from models import Base


Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/quiz/")
def collect_question(payload: QuestionParam, db: Session = Depends(get_db)) -> str | None:
    questions_num = payload.questions_num
    params = {"count": questions_num}
    jservice_response = requests.get(
        "https://jservice.io/api/random",
        params=params, 
        timeout=10
    )
    jservice_response.raise_for_status()
    questions_from_jservice = jservice_response.json()
    questions = parse_obj_as(list[Question], questions_from_jservice) 
    for question in questions:
        db_question = get_question(
            db,
            question_id=question.id
        )
        if not db_question:
            db_question = create_question(
                db,
                question
            )
            question = get_previous_question(
                    db,
                    id=db_question.id
            )
            return question.question


