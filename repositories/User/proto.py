from typing import Protocol


class UserNotFoundError(Exception):
    def __init__(self,user_name: str) -> None:
        self.user_name: str = user_name


class UsersRepoProtocol(Protocol):     
    def get_holidays_ids_by_user_name(self, user_name: str) -> list[int] | None:
        try:
            ...
        except KeyError:
            raise UserNotFoundError(user_name=user_name) from KeyError
    
    def post_holidays(self, user_name: str, holis_id: int) -> None:
        ...  
    
    def delete_holidays(self, user_name: str, holis_id: int) -> None:
        ...