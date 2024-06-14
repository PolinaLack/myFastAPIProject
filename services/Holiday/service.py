from models.holiday import Holiday_base
from repositories.Holiday.proto import HolidayRepoProtocol


class HolidayServices:
    def __init__(self, holis_repo: HolidayRepoProtocol) -> None:
        self.holis_repo: HolidayRepoProtocol = holis_repo


    def get_all_holidays(self)  -> dict[int, Holiday_base]:
        return self.holis_repo.get_all_holidays()
    

    def get_holidays_by_user_name(self, user_name: str)  -> dict[int, Holiday_base]:
        return self.holis_repo.get_holidays_by_user_name(user_name=user_name)


    def post_holidays(self, holis_in: Holiday_base) -> str:
        return self.holis_repo.post_holidays(holis_in=holis_in)    


    def put_holidays(self, holis_id: int, holis_in: Holiday_base) -> str:
        return self.holis_repo.put_holidays(holis_id=holis_id, holis_in=holis_in)
    
    
    def delete_holidays(self, holis_id: int, user_name: str) -> str:
        return self.holis_repo.delete_holidays(holis_id=holis_id, user_name=user_name)
 