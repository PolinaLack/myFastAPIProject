from models import User


class UsersRepo:
    def __init__(self, users_table: dict[str, User]) -> None:
        self.users_table: dict[str, User] = users_table
    
    
    def get_holidays_ids_by_user_name(self, user_name) -> list[int]:
        user: User = self.users_table[user_name]   
        return user.holis_ids
    
    
    def post_holidays(self, user_name: str, holis_id: int) -> None:
        updated_user: User =  self.users_table[user_name]
        updated_user.holis_ids.append(holis_id)
        self.users_table[user_name] = updated_user
   
   
    def delete_holidays(self, user_name: str, holis_id: int) -> None:
        updated_user: User =  self.users_table[user_name]
        updated_user.holis_ids.remove(holis_id)
        self.users_table[user_name] = updated_user
   
    
    # в разработке
    # def get_all_users(self):
    #     return self.users
    