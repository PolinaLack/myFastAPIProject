from datetime import datetime
from typing import Annotated

from data import calendar, holidays_all
from dependencies import get_user_service
from fastapi import Body, Depends
from models import Holidays_base, User
from repository import RepoHolidays, RepoUsers, RepoUsersProtocol


class HolidaysServises:
    def __init__(self):
        ...
    
    def post_new_holidays(self, holidays_in: Holidays_base, user_name, 
                          users: Annotated[RepoUsers, Depends()]):
        if user_name not in users.get_all_users():
            RepoHolidays().post_holidays(holidays_in=holidays_in, holidays_id=max(holidays_all) + 1)
    
    # def get_my_holidays(self, user_name: Annotated[str, Body()], ):
    #     user: User = self.users.get_user_by_name(name=user_name)
    #     res: list[Holidays_base] = [holidays_all[i] for i in user.holidays_id]
    #     return res
    

class UsersServises:
    def __init__(self, users: Annotated[RepoUsers | None, Depends()]):
        self.users = users if 
            
    

# def serv_post_new_holidays(holidays_in: Holidays_base) -> str:
# def serv_post_new_holidays(holidays_in: Holidays_base) -> str:
#     start = datetime.strptime(holidays_in.start, "%d.%m.%Y")
#     end = datetime.strptime(holidays_in.end, "%d.%m.%Y")
    
#     if start > end:
#         return "Start date must be less than end date"
#     else:
#         if holidays_in.user_name in users and holidays_in.start not in calendar:
#             id: int = max(holidays_all) + 1
#             holidays_all[id] = Holidays_base(**holidays_in.model_dump())
#             users[holidays_in.user_name].append(id)
#             # insert_dates_in_calendar(start, end)
#             return "OK"
#         else:
#             return "User not found"


# def insert_dates_in_calendar(start, end):    
#     holidays_len = end - start
#     for date in range(holidays_len.days):
#         if start + date not in calendar:
#             calendar[str(start + date)] = 1
#         else:
#             calendar[str(start + date)] += 1

    
    



# def serv_delete_holidays(user_name: Annotated[str, Body()], 
#                       holidays_start: Annotated[str, Body()]) -> Holidays_base:
#     id_holidays: int = [i for i in users[user_name] if holidays_start == holidays_all[i].start][0]
#     deleted_holidays: Holidays_base = holidays_all.pop(id_holidays)
#     return deleted_holidays