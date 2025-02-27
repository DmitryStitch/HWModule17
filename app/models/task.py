from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from app.models.base import Base
from app.models.user import User


class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {"keep_existing": True}
    id = Column(Integer, primary_key=True, index=True)
    tittle = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)
    user = relationship("User", back_populates='tasks')


print(CreateTable(Task.__table__))
