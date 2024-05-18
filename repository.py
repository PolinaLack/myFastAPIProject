from typing import Protocol

from data import holis_all, users_table
from models import Holidays_base, User

# class UsersRepoProtocol(Protocol):     
#     def get_user_by_name(self, name: str) -> User:
#         ...
        

class UsersRepoProtocol(Protocol):     
    def get_holidays_by_user_name(self, name: str) -> list[Holidays_base]:
        ...


class UsersRepo:
    def __init__(self, users: dict[str, User]) -> None:
        self.users: dict[str, User] = users
    
    
    def get_holidays_by_user_name(self, name) -> list[Holidays_base]:
        user: User = users_table[name]   
        return [holis_all[id] for id in user.holis_id]
    
        
    # def get_all_users(self):
    #     return self.users
    
    # def get_user_by_name(self, name: str) -> User:
    #     ...



# class HolidaysRepo:
#     def __init__(self):
#         ...
    
               
    # def get_all_holidays(self) -> dict[int, Holidays_base]:
    #     return self.holidays_all
    
    # def get_holidays_by_id(self, id) -> Holidays_base:
    #     return self.holidays_all[id]
    
    # def post_holidays(self, holidays_in: Holidays_base, holidays_id: int):
    #     self.holidays_all[holidays_id] = holidays_in
        
    
