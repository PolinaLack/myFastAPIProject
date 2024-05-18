from data import holidays_all, users
from models import Holidays_base, User
from typing import Protocol


class RepoHolidays:
    def __init__(self):
        self.holidays_all: dict[int, Holidays_base] = holidays_all
        
    # def get_all_holidays(self) -> dict[int, Holidays_base]:
    #     return self.holidays_all
    
    # def get_holidays_by_id(self, id) -> Holidays_base:
    #     return self.holidays_all[id]
    
    def post_holidays(self, holidays_in: Holidays_base, holidays_id: int):
        self.holidays_all[holidays_id] = holidays_in
        
    
    
class RepoUsers:
    def __init__(self):
        self.users = users
        
    def get_user_by_name(self, name) -> User:
        return self.users[name]
    
    def get_all_users(self):
        return self.users

class RepoUsersProtocol(Protocol):     
    def get_user_by_name(self, name: str) -> User:
        ...