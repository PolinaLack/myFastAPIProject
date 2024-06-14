from models.user import User


class Admin(User):
    login: str
    password: str
  
    