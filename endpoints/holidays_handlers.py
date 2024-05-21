from typing import Annotated

from dependencies import get_holidays_services, get_users_services
from fastapi import APIRouter, Body, Depends, Query
from models.holiday_models import Holidays_base
from services.Holiday.proto import HolidaysServicesProtocol
from services.User.proto import UsersServicesProtocol

router = APIRouter(prefix="/holidays")


@router.get(path="/my_holidays")
def handle_get_holidays_by_username(
            user_name: Annotated[str, Query()],
            
            holis_services: Annotated[HolidaysServicesProtocol, 
                                    Depends(dependency=get_holidays_services)],
            users_services: Annotated[UsersServicesProtocol,
                                    Depends(dependency=get_users_services)],
            ) -> list[Holidays_base]:

    user_holis: list[Holidays_base] = holis_services.get_holidays_by_user_name(
                                                        user_name=user_name,
                                                        users_services=users_services
                                                        )
    return user_holis


@router.post(path="/holidays")
def handle_post_new_holidays(
            user_name: Annotated[str, Body()],
            holis_in: Annotated[Holidays_base, Body()],
            
            holis_services: Annotated[HolidaysServicesProtocol,
                                    Depends(dependency=get_holidays_services)],
            users_services: Annotated[UsersServicesProtocol,
                                    Depends(dependency=get_users_services)],
            ) -> list[Holidays_base]:
    
    holis_id: int = holis_services.post_holidays(holis_in=holis_in)
    users_services.post_holidays(user_name=user_name, holis_id=holis_id)
    
    user_holis: list[Holidays_base] = holis_services.get_holidays_by_user_name(
                                                            user_name=user_name,
                                                            users_services=users_services
                                                            )
    return user_holis

    
@router.delete(path="/my_holidays")
def handle_delete_holidays(
            user_name: Annotated[str, Query()],
            holis_to_del_ids: Annotated[int, Body()],
            
            users_services: Annotated[UsersServicesProtocol,
                                    Depends(dependency=get_users_services)],
            holis_services: Annotated[HolidaysServicesProtocol, 
                                    Depends(dependency=get_holidays_services)],
            ) -> list[Holidays_base]:
    
    users_services.delete_holidays(user_name=user_name, holis_id=holis_to_del_ids)
    holis_services.delete_holidays(holis_id=holis_to_del_ids)
    
    user_holis: list[Holidays_base] = holis_services.get_holidays_by_user_name(
                                                            user_name=user_name,
                                                            users_services=users_services
                                                            )
    return user_holis


@router.put(path="/my_holidays")
def handle_put_holidays(
            user_name: Annotated[str, Body()],
            holis_to_put_ids: Annotated[int, Body()],
            holis_to_put_in: Annotated[Holidays_base, Body()],
            
            holis_services: Annotated[HolidaysServicesProtocol, 
                                    Depends(dependency=get_holidays_services)],
            users_services: Annotated[UsersServicesProtocol,
                                    Depends(dependency=get_users_services)],
            ) -> list[Holidays_base]:
    
    holis_services.put_holidays(holis_id=holis_to_put_ids, holis_in=holis_to_put_in)
    
    user_holis: list[Holidays_base] = holis_services.get_holidays_by_user_name(
                                                            user_name=user_name,
                                                            users_services=users_services
                                                            )
    return user_holis


# в разработке
# @app.get(path="/users")
# def get_users() -> list[str]:
#     res: list[str] = users
#     return res





