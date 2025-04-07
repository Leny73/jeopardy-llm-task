from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import get_random_question
from app.schemas import AgentPlayRequest, AgentPlayResponse

router = APIRouter()

@router.post("/", response_model=AgentPlayResponse)
def agent_play(request: AgentPlayRequest, db: Session = Depends(get_db)):
    question = get_random_question(db, round="Jeopardy!", value=200)
    if not question:
        raise HTTPException(status_code=404, detail="No question found.")
    
    ai_answer = question.answer  # Simulate AI answering correctly
    return {
        "agent_name": request.agent_name,
        "question": question.question,
        "ai_answer": ai_answer,
        "is_correct": True
    }