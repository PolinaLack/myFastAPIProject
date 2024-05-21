from models.holiday_models import Holidays_base
from repositories.Holiday.proto import HolidaysIdNotFoundError


class HolidaysRepo:
    def __init__(self, holis_table) -> None:
        self.holis_table: dict[int, Holidays_base] = holis_table
    
                                      
    def post_holidays(self, holis_in: Holidays_base) -> int:
        holis_id: int = max(self.holis_table) + 1
        self.holis_table[holis_id] = holis_in
        return holis_id

    
    def get_holidays_by_ids(self, ids: list[int]) -> list[Holidays_base]:
        return [self.holis_table[id] for id in ids]

    
    def delete_holidays(self, holis_id: int) -> None:
        try:
            del self.holis_table[holis_id]
        except KeyError:
            raise HolidaysIdNotFoundError(holis_id=holis_id) from KeyError
    
    
    def put_holidays(self, holis_id: int, holis_in: Holidays_base) -> None:
        try:
            self.holis_table[holis_id] = holis_in
        except KeyError:
            raise HolidaysIdNotFoundError(holis_id=holis_id) from KeyError
    
    
    # в разработке
    # def get_all_holidays(self) -> dict[int, Holidays_base]:
    #     return self.holidays_all  