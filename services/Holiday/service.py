from models import Holidays_base
from repositories.Holiday.proto import HolidaysRepoProtocol


class HolidaysServices:
    def __init__(self, holis_repo: HolidaysRepoProtocol) -> None:
        self.holis_repo: HolidaysRepoProtocol = holis_repo


    def post_holidays(self, holis_in: Holidays_base) -> int:
        holis_id: int = self.holis_repo.post_holidays(holis_in=holis_in)
        return holis_id
    
    
    def get_holidays_by_ids(self, ids: list[int]) -> list[Holidays_base]:
        return self.holis_repo.get_holidays_by_ids(ids=ids)
    
    
    def delete_holidays(self, holis_id: int) -> None:
        self.holis_repo.delete_holidays(holis_id=holis_id)
    
    
    def put_holidays(self, holis_id: int, holis_in: Holidays_base) -> None:
        self.holis_repo.put_holidays(holis_id=holis_id, holis_in=holis_in)
    
 