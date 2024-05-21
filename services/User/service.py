from typing import NoReturn
from repositories.User.proto import UsersRepoProtocol


class UsersServices:
    def __init__(self, user_repo: UsersRepoProtocol) -> None:
        self.user_repo: UsersRepoProtocol = user_repo
    
      
    def get_holidays_ids_by_user_name(self, user_name: str) -> list[int] | NoReturn:
        return self.user_repo.get_holidays_ids_by_user_name(user_name=user_name)
    
    
    def post_holidays(self, user_name: str, holis_id: int) -> None:
        self.user_repo.post_holidays(user_name=user_name, holis_id=holis_id)
        
    
    def delete_holidays(self, user_name: str, holis_id: int) -> None:
        self.user_repo.delete_holidays(user_name=user_name, holis_id=holis_id)

