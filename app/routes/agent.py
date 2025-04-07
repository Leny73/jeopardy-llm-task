from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import get_random_question
from app.schemas import AgentPlayRequest, AgentPlayResponse
import openai

router = APIRouter()

# Set your OpenAI API key (ensure this is securely stored in environment variables in production)
openai.api_key = "your_openai_api_key"

@router.post("/", response_model=AgentPlayResponse)
def agent_play(request: AgentPlayRequest, db: Session = Depends(get_db)):
    question = get_random_question(db, round="Jeopardy!", value=200)
    if not question:
        raise HTTPException(status_code=404, detail="No question found.")
    
    # Use OpenAI API to generate an AI answer
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use the appropriate model
            prompt=f"Answer the following Jeopardy question: {question.question}",
            max_tokens=100,
            temperature=0.7
        )
        ai_answer = response.choices[0].text.strip()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating AI answer: {str(e)}")
    
    # Simulate correctness check (you can implement actual logic if needed)
    is_correct = ai_answer.lower() == question.answer.lower()

    return {
        "agent_name": request.agent_name,
        "question": question.question,
        "ai_answer": ai_answer,
        "is_correct": is_correct
    }