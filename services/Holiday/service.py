from models.holiday_models import Holidays_base
from repositories.Holiday.proto import HolidaysRepoProtocol
from services.User.proto import UsersServicesProtocol


class HolidaysServices:
    def __init__(self, holis_repo: HolidaysRepoProtocol) -> None:
        self.holis_repo: HolidaysRepoProtocol = holis_repo


    def post_holidays(self, holis_in: Holidays_base) -> int:
        holis_id: int = self.holis_repo.post_holidays(holis_in=holis_in)
        return holis_id
    
    
    def get_holidays_by_ids(self, ids: list[int]) -> list[Holidays_base]:
        return self.holis_repo.get_holidays_by_ids(ids=ids)
    
    # экспериментальная часть
    def get_holidays_by_user_name(self, user_name: str,
                                  users_services: UsersServicesProtocol) -> list[Holidays_base]:
        user_holis_ids: list[int] | None = users_services.get_holidays_ids_by_user_name(user_name=user_name)
        return self.holis_repo.get_holidays_by_ids(ids=user_holis_ids)
    # экспериментальная часть
    
    def delete_holidays(self, holis_id: int) -> None:
        self.holis_repo.delete_holidays(holis_id=holis_id)
    
    
    def put_holidays(self, holis_id: int, holis_in: Holidays_base) -> None:
        self.holis_repo.put_holidays(holis_id=holis_id, holis_in=holis_in)
    
 