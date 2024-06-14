from typing import NoReturn, Protocol

from models.holiday import Holiday_base


class HolidayIdNotFoundError(Exception):
    def __init__(self,holis_id: int) -> None:
        self.holis_id: int = holis_id
        

class DateIsBusyError(Exception):
    def __init__(self,holis_in) -> None:
        self.start: str = holis_in.start
        self.end_date: str = holis_in.end_date


class HolidayRepoProtocol(Protocol):     
    def get_all_holidays(self) -> dict[int, Holiday_base]:
        ...
    
    
    def get_holidays_by_user_name(self, user_name) -> dict[int, Holiday_base]:
        ...
    
    
    def post_holidays(self, holis_in: Holiday_base) -> str | NoReturn: # type: ignore
        ...
        
        
    def put_holidays(self, holis_id: int, holis_in: Holiday_base) -> str | NoReturn: # type: ignore
        ...


    def delete_holidays(self, holis_id: int, user_name: str)-> str | NoReturn: # type: ignore
        ...
