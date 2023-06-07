from sqlalchemy.orm import Session


from models import Quiz
from schemas import QuestionCreate


def get_question(db: Session, question_id: int):
    return db.query(Quiz).filter(Quiz.question_id == question_id).first()


def get_previous_question(db: Session, id: int):
    return db.query(Quiz).filter(Quiz.id == (id - 1)).first()


def create_question(db: Session, question: QuestionCreate):
    db_question = Quiz(
        question_id=question.id,
        question=question.question,
        answer=question.answer,
        created_at=question.created_at,
        )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question
