from typing import Protocol


class UsersRepoProtocol(Protocol):     
    def get_holidays_ids_by_user_name(self, user_name: str) -> list[int]:
        ...
    
    def post_holidays(self, user_name: str, holis_id: int) -> None:
        ...  
    
    def delete_holidays(self, user_name: str, holis_id: int) -> None:
        ...