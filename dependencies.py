from typing import Annotated

from fastapi import Depends
from repository import RepoUsers, RepoUsersProtocol
from services import HolidaysServises

    

# def get_users_service(users_repo: 
#     Annotated[RepoUsersProtocol,
#               Depends(get_users_repo)]) -> RepoUsersProtocol:
#     return RepoUsers(users=users_repo)


def get_holiday_services():
    return HolidaysServises()

def users_repo_dependency():
    return RepoUsers()
