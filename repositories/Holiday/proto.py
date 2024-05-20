from typing import Protocol

from models import Holidays_base


class HolidaysRepoProtocol(Protocol):     
    def post_holidays(self, holis_in: Holidays_base) -> int:
        ...
        
    def get_holidays_by_ids(self, ids) -> list[Holidays_base]:
        ...
    
    def delete_holidays(self, holis_id: int) -> None:
        ...
    
    def put_holidays(self, holis_id: int, holis_in: Holidays_base) -> None:
        ...

