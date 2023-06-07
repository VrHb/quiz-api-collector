from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass

class Quiz(Base):
    __tablename__ = "quiz_questions"
    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer)
    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime)
