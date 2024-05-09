from pydantic import BaseModel


class Task(BaseModel):
    id: int
    name: str
    description: str| None = None
    completed: bool = False
    

class TaskCreate(BaseModel):
    name: str
    description: str| None = None
    completed: bool = False
    
    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Task1",
                    "description": "To do something important",
                    "completed": False
                }
            ]
        }
    }

class TaskPatch(BaseModel):
    name: str | None =  None
    description: str | None = None
    completed: bool = None    # type: ignore
    
