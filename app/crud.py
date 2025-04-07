from sqlalchemy.orm import Session
from app.models import JeopardyQuestion
import random

def get_random_question(db: Session, round: str, value: int):
    questions = db.query(JeopardyQuestion).filter_by(round=round, value=value).all()
    return random.choice(questions) if questions else None

def get_question_by_id(db: Session, question_id: int):
    return db.query(JeopardyQuestion).filter_by(id=question_id).first()