from datetime import datetime

from pydantic import BaseModel


class QuestionParam(BaseModel):
    questions_num: int

class QuestionBase(BaseModel):
    question: str
    answer: str

class QuestionCreate(QuestionBase):
    pass

class Question(QuestionBase):
    id: int
    created_at: datetime

    class config:
        orm_mode = True
