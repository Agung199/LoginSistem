from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.task_model import Task
#from app.models.user_model import User

from app.schemas.task_schema import TaskCreate
from app.schemas.task_schema import TaskUpdate

from app.auth import get_current_user


router = APIRouter()


# Create Tasks
@router.post("/tasks")
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    new_task = Task(
        title=task.title,
        description=task.description,
        due_date=task.due_date,
        user_id=current_user["id"],
    )

    db.add(new_task)

    db.commit()

    db.refresh(new_task)

    return {"message": "Task created", "task": new_task}


@router.get("/tasks")
def get_my_tasks(db: Session = Depends(get_db), current_user=Depends(get_current_user)):

    tasks = db.query(Task).filter(Task.user_id == current_user["id"]).all()

    return tasks


@router.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):

    task = (
        db.query(Task)
        .filter(Task.id == task_id, Task.user_id == current_user["id"])
        .first()
    )

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    if task_update.title:
        task.title = task_update.title

    if task_update.description:
        task.description = task_update.description

    if task_update.status:
        task.status = task_update.status

    if task_update.due_date:
        task.due_date = task_update.due_date

    db.commit()

    return {"message": "Task updated"}


@router.delete("/tasks/{task_id}")
def delete_task(
    task_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)
):

    task = (
        db.query(Task)
        .filter(Task.id == task_id, Task.user_id == current_user["id"])
        .first()
    )

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)

    db.commit()

    return {"message": "Task deleted"}
