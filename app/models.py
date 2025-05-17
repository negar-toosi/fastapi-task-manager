from sqlalchemy import Boolean, Column, Integer, String, DateTime
from app.database import base
from sqlalchemy.sql import func

class Tasks(base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())