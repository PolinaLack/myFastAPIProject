from typing import Annotated

from fastapi import Depends, FastAPI
from models import Holidays_base
from servises import serv_delete_holidays, serv_get_my_holidays, serv_post_new_holidays

app = FastAPI()


# @app.get(path="/users")
# def get_users() -> list[str]:
#     res: list[str] = users
#     return res


@app.get(path="/my_holidays")
def get_my_holidays(res: Annotated[list[Holidays_base], Depends(serv_get_my_holidays)])-> list[Holidays_base]:
    return res


@app.post(path="/holidays")
def post_new_holidays(res: Annotated[str, Depends(serv_post_new_holidays)]) -> str:
    return res

    
@app.delete(path="/my_holidays")
def delete_holidays(res: Annotated[Holidays_base, Depends(serv_delete_holidays)]) -> Holidays_base:
    return res


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("endpoints:app", port=8000, reload=False)

print(__name__)


