from sqlalchemy.orm import Session
from app import models, schemas

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tasks).offset(skip).limit(limit).all()

def get_task(db: Session, task_id: int):
    return db.query(models.Tasks).filter(models.Task.id == task_id).first()

def delete_task(db: Session, task_id: int):
    task = db.query(models.Tasks).filter(models.Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task

def update_task(db: Session, task_id: int, updated_task: schemas.TaskCreate):
    task = db.query(models.Tasks).filter(models.Task.id == task_id).first()
    if task:
        task.title = updated_task.title
        task.description = updated_task.description
        db.commit()
        db.refresh(task)
    return task