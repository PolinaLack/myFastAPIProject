from pydantic import BaseModel


class Holidays_base(BaseModel):
    user_name: str
    start: str
    end: str
    

class Holidays_insert(Holidays_base):
    user_name: None
    start: str
    end: str
    
