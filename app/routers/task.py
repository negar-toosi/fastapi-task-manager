from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud, database

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# GET /tasks/
@router.get("/", response_model=list[schemas.TaskRead])
def read_tasks(db: Session = Depends(database.get_db)):
    return crud.get_tasks(db)

# POST /tasks/
@router.post("/", response_model=schemas.TaskRead)
def create_task(task: schemas.TaskCreate, db: Session = Depends(database.get_db)):
    return crud.create_task(db, task)

# GET /tasks/{task_id}
@router.get("/{task_id}", response_model=schemas.TaskRead)
def read_task(task_id: int, db: Session = Depends(database.get_db)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# PUT /tasks/{task_id}
@router.put("/{task_id}", response_model=schemas.TaskRead)
def update_task(task_id: int, task_update: schemas.TaskCreate, db: Session = Depends(database.get_db)):
    task = crud.update_task(db, task_id, task_update)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# DELETE /tasks/{task_id}
@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(database.get_db)):
    success = crud.delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
