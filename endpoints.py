from typing import Annotated

from dependencies import get_users_services
from fastapi import APIRouter, Body, Depends
from models import Holidays_base
from services import UsersServicesProtocol

router = APIRouter(prefix="/holidays")


@router.get(path="/my_holidays")
def handle_get_holidays_by_username(name: str,
                                    users_services: Annotated[UsersServicesProtocol,
                                                            Depends(dependency=get_users_services)]
                                    ) -> list[Holidays_base]:
    return users_services.get_holidays_by_user_name(name=name)


# @app.get(path="/users")
# def get_users() -> list[str]:
#     res: list[str] = users
#     return res


# @router.post(path="/holidays")
# def post_new_holidays(
#         user_name: Annotated[str, Body()],
#         holidays_in: Annotated[Holidays_base, Body()],
#         holidays_services: Annotated[HolidaysServises, Depends()]
#             ) -> str:
    
#     holidays_services.post_new_holidays(holidays_in, user_name)
#     return res

    
# @router.delete(path="/my_holidays")
# def delete_holidays(res: Annotated[Holidays_base, Depends(serv_delete_holidays)]) -> Holidays_base:
#     return res






