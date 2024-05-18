from typing import Annotated

from data import users_table
from fastapi import Depends
from repository import UsersRepo, UsersRepoProtocol
from services import UsersServices


def get_users_repo() -> UsersRepoProtocol:
    return UsersRepo(users_table)


def get_users_services(user_repo: Annotated[UsersRepoProtocol, 
              Depends(dependency=get_users_repo)]) -> UsersServices:
    return UsersServices(user_repo=user_repo)


# def get_users_service(users_repo: 
#     Annotated[RepoUsersProtocol,
#               Depends(get_users_repo)]) -> RepoUsersProtocol:
#     return RepoUsers(users=users_repo)
