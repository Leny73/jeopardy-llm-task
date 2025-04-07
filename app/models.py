from sqlalchemy import Column, Integer, String, Date
from app.db_base import Base

class JeopardyQuestion(Base):
    __tablename__ = "jeopardy_questions"
    id = Column(Integer, primary_key=True, index=True)
    show_number = Column(Integer)
    air_date = Column(Date)
    round = Column(String)
    category = Column(String)
    value = Column(Integer)
    question = Column(String)
    answer = Column(String)