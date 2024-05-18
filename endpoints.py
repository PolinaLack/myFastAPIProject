from typing import Annotated

from fastapi import Body, Depends, APIRouter
from dependencies import get_holiday_services, get_user_service
from models import Holidays_base
from repository import RepoUsersProtocol
from services import serv_delete_holidays, HolidaysServises , serv_post_new_holidays


router = APIRouter(prefix="/holidays", tags=["Holidays"])


# @app.get(path="/users")
# def get_users() -> list[str]:
#     res: list[str] = users
#     return res


# @router.get(path="/my_holidays")
# def get_my_holidays(name: Annotated[str, Body()],
#                     holiday_services: Annotated[HolidaysServises, Depends(get_holiday_services)]
#                     ) -> list[Holidays_base]:
#     my_holidays: list[Holidays_base] = holiday_services.get_my_holidays(user_name=name)
#     return my_holidays


@router.post(path="/holidays")
def post_new_holidays(
        user_name: Annotated[str, Body()],
        holidays_in: Annotated[Holidays_base, Body()],
        holidays_services: Annotated[HolidaysServises, Depends()]
            ) -> str:
    
    holidays_services.post_new_holidays(holidays_in, user_name)
    return res

    
@router.delete(path="/my_holidays")
def delete_holidays(res: Annotated[Holidays_base, Depends(serv_delete_holidays)]) -> Holidays_base:
    return res






