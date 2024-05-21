from typing import Annotated

from data import holis_table, users_table
from fastapi import Depends
from repositories.Holiday.repo import HolidaysRepo
from repositories.Holiday.proto import HolidaysRepoProtocol
from repositories.User.proto import UsersRepoProtocol
from repositories.User.repo import UsersRepo
from services.Holiday.proto import HolidaysServicesProtocol
from services.Holiday.service import HolidaysServices
from services.User.proto import UsersServicesProtocol
from services.User.service import UsersServices


def get_users_repo() -> UsersRepoProtocol:
    return UsersRepo(users_table=users_table)


def get_users_services(user_repo: Annotated[UsersRepoProtocol, 
              Depends(dependency=get_users_repo)]) -> UsersServicesProtocol:
    return UsersServices(user_repo=user_repo)


def get_holidays_repo() -> HolidaysRepoProtocol:
    return HolidaysRepo(holis_table=holis_table)


def get_holidays_services(holis_repo: Annotated[HolidaysRepoProtocol, 
              Depends(dependency=get_holidays_repo)]) -> HolidaysServicesProtocol:
    return HolidaysServices(holis_repo=holis_repo)


