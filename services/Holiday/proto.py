from typing import Protocol

from models.holiday import Holiday_base


class HolidayServicesProtocol(Protocol):
    def get_all_holidays(self) -> dict[int, Holiday_base]:
        ...

    
    def get_holidays_by_user_name(self, user_name: str)  -> dict[int, Holiday_base]:
        ...


    def post_holidays(self, holis_in: Holiday_base) -> str:
        ...
    
    
    def put_holidays(self, holis_id: int, holis_in: Holiday_base) -> str:
        ...
        
    
    def delete_holidays(self, holis_id: int, user_name: str) -> str:
        ...
        
        
        