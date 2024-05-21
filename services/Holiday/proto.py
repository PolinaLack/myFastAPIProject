from typing import Protocol

from models.holiday_models import Holidays_base
from services.User.proto import UsersServicesProtocol


class HolidaysServicesProtocol(Protocol):
    def post_holidays(self, holis_in: Holidays_base) -> int:
        ...
    
    def get_holidays_by_ids(self, ids: list[int]) -> list[Holidays_base]:
        ...
    
    def get_holidays_by_user_name(self, user_name: str,
                                  users_services: UsersServicesProtocol) -> list[Holidays_base]:
        ...
        
    def delete_holidays(self, holis_id: int) -> None:
        ...
    
    def put_holidays(self, holis_id: int, holis_in: Holidays_base) -> None:
        ...