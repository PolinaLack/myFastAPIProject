from typing import NoReturn, Protocol


class UserNotFoundError(Exception):
    def __init__(self,user_name: str) -> None:
        self.user_name: str = user_name


class UsersRepoProtocol(Protocol):     
    ...