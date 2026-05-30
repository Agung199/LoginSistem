from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from app.db.base import Base

from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))

    role = Column(String, nullable=False, default="user")

    tasks = relationship("Task", back_populates="owner")
