from typing import NoReturn, Protocol


class UsersServicesProtocol(Protocol):
    def get_holidays_ids_by_user_name(self, user_name: str) -> list[int] | NoReturn:
        ...
    
    def post_holidays(self, user_name: str, holis_id: int) -> None:
        ...
    
    def delete_holidays(self, user_name: str, holis_id: int) -> None:
        ...