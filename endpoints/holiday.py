import json
from typing import Annotated

from dependencies import get_holidays_services
from fastapi import APIRouter, Body, Depends, Query
from models.holiday import Holiday_base, Holiday_insert
from services.Holiday.proto import HolidayServicesProtocol

router = APIRouter(prefix="/holidays")


@router.get(path="/all_holidays")
def handle_get_all_holidays(
            holis_services: Annotated[HolidayServicesProtocol, 
                                    Depends(dependency=get_holidays_services)],
            ) -> str:
    response = holis_services.get_all_holidays()
    holis_json = json.dumps({key: holis.model_dump() for key, holis in response.items()})
    return holis_json


@router.get(path="/my_holidays")
def handle_get_holidays_by_username(
            user_name: Annotated[str, Query()],
            holis_services: Annotated[HolidayServicesProtocol, 
                                    Depends(dependency=get_holidays_services)],
            ) -> str:

    response: dict[int, Holiday_base] = holis_services.get_holidays_by_user_name(
                                                        user_name=user_name,
                                                        )
    holis_json = json.dumps({key: holis.model_dump() for key, holis in response.items()})
    return holis_json


@router.post(path="/holidays")
def handle_post_holidays(
            user_name: Annotated[str, Query()],
            dates_in: Annotated[Holiday_insert, Body()],
            holis_services: Annotated[HolidayServicesProtocol,
                                    Depends(dependency=get_holidays_services)],
                            ) -> str:
    holis_in = Holiday_base(
                    user_name = user_name, 
                    start = dates_in.start,
                    end_date = dates_in.end_date)
    response = holis_services.post_holidays(holis_in=holis_in)
    return response


@router.put(path="/my_holidays")
def handle_put_holidays(
            user_name: Annotated[str, Query()],
            dates_in: Annotated[Holiday_insert, Body()],
            holis_id: Annotated[int, Body()],
            
            holis_services: Annotated[HolidayServicesProtocol, 
                                    Depends(dependency=get_holidays_services)],
            ) -> str:
    
    holis_in = Holiday_base(
                    user_name = user_name, 
                    start = dates_in.start,
                    end_date = dates_in.end_date)
    
    response = holis_services.put_holidays(holis_id=holis_id, holis_in=holis_in)
    return response
    
    
@router.delete(path="/my_holidays")
def handle_delete_holidays(
            user_name: Annotated[str, Query()],
            holis_id: Annotated[int, Body()],

            holis_services: Annotated[HolidayServicesProtocol, 
                                    Depends(dependency=get_holidays_services)],
            ) -> str:
    
    response = holis_services.delete_holidays(holis_id=holis_id, user_name=user_name)
    
    return response







