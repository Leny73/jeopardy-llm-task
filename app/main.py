from fastapi import FastAPI
from app.routes import questions, verify, agent

app = FastAPI()

# Include routes
app.include_router(questions.router, prefix="/question", tags=["Questions"])
app.include_router(verify.router, prefix="/verify-answer", tags=["Verify"])
app.include_router(agent.router, prefix="/agent-play", tags=["Agent"])