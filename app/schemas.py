from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str
    is_completed: bool 

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int

    class Config:
        orm_mode = True