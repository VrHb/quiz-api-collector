from sqlalchemy.orm import Session


from models import Quiz
from schemas import QuestionCreate


def get_question(db: Session, question_id: int):
    return db.query(Quiz).filter(Quiz.id == question_id).first()


def create_question(db: Session, question: QuestionCreate):
    db_question = Quiz(
        id=question.id,
        question=question.question,
        answer=question.answer,
        created_at=question.created_at,
        )
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question
