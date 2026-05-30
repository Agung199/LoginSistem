from pydantic import BaseModel
from datetime import datetime


class TaskCreate(BaseModel):
    title: str

    description: str | None = None

    due_date: datetime | None = None


class TaskUpdate(BaseModel):
    title: str | None = None

    description: str | None = None

    status: str | None = None

    due_date: datetime | None = None
