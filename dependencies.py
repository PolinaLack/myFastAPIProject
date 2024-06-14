from typing import Annotated

from data import users_table
from fastapi import Depends
from postgres_pool import postgresql_pool
from repositories.Holiday.proto import HolidayRepoProtocol
from repositories.Holiday.repo import HolidayRepo
from repositories.User.proto import UsersRepoProtocol
from repositories.User.repo import UsersRepo
from services.Holiday.proto import HolidayServicesProtocol
from services.Holiday.service import HolidayServices
from services.User.proto import UsersServicesProtocol
from services.User.service import UsersServices


def get_users_repo() -> UsersRepoProtocol:
    return UsersRepo(users_table=users_table)


def get_users_services(user_repo: Annotated[UsersRepoProtocol, 
              Depends(dependency=get_users_repo)]) -> UsersServicesProtocol:
    return UsersServices(user_repo=user_repo)


def get_holidays_repo() -> HolidayRepoProtocol:
    return HolidayRepo(postgresql_pool)


def get_holidays_services(holis_repo: Annotated[HolidayRepoProtocol, 
              Depends(dependency=get_holidays_repo)]) -> HolidayServicesProtocol:
    return HolidayServices(holis_repo=holis_repo)


