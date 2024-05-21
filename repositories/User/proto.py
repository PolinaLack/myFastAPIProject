from typing import NoReturn, Protocol


class UserNotFoundError(Exception):
    def __init__(self,user_name: str) -> None:
        self.user_name: str = user_name


class UsersRepoProtocol(Protocol):     
    def get_holidays_ids_by_user_name(self, user_name: str) -> list[int] | NoReturn:
        ...
    
    def post_holidays(self, user_name: str, holis_id: int) -> None:
        ...
    
    def delete_holidays(self, user_name: str, holis_id: int) -> None:
        ...