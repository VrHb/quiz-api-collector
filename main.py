from datetime import datetime

import requests
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import parse_obj_as

from database import Base, engine, SessionLocal
from schemas import QuestionParam, Question, QuestionCreate, QuestionsList
from crud import get_question, create_question


Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/quiz/")
def get_questions(payload: QuestionParam, db: Session = Depends(get_db)) -> Question | None:
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
            return question
