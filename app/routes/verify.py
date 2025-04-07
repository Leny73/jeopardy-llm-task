from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import get_question_by_id
from app.schemas import VerifyAnswerRequest, VerifyAnswerResponse
from fuzzywuzzy import fuzz

router = APIRouter()

@router.post("/", response_model=VerifyAnswerResponse)
def verify_answer(request: VerifyAnswerRequest, db: Session = Depends(get_db)):
    question = get_question_by_id(db, request.question_id)
    if not question:
        raise HTTPException(status_code=404, detail="Question not found.")
    
    similarity = fuzz.ratio(question.answer.lower(), request.user_answer.lower())
    is_correct = similarity >= 80
    ai_response = f"Yes, {question.answer} is the correct answer." if is_correct else f"No, the correct answer is {question.answer}."
    
    return {"is_correct": is_correct, "ai_response": ai_response}