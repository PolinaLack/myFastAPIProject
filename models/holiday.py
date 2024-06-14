from pydantic import BaseModel


class Holiday_base(BaseModel):
    user_name: str
    start: str
    end_date: str
    

class Holiday_insert(BaseModel):
    start: str
    end_date: str
    
