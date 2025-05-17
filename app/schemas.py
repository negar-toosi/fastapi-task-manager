from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str
    is_completed: bool 

    class Config:
        from_attributes = True
        
class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int

    