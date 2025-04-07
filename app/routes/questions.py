from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import get_random_question
from app.schemas import QuestionResponse

router = APIRouter()

@router.get("/", response_model=QuestionResponse)
def get_question(round: str, value: int, db: Session = Depends(get_db)):
    question = get_random_question(db, round, value)
    if not question:
        raise HTTPException(status_code=404, detail="No question found.")
    return {
        "question_id": question.id,
        "round": question.round,
        "category": question.category,
        "value": f"${question.value}",
        "question": question.question
    }