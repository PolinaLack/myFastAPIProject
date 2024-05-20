from models.user_models import User


class Admin(User):
    login: str
    password: str
  
    