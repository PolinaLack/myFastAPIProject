from endpoints.holidays_handlers import router
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from h11 import Request
from repositories.Holiday.proto import HolidaysIdNotFoundError
from repositories.User.proto import UserNotFoundError

app = FastAPI()
app.include_router(router=router)


@app.exception_handler(exc_class_or_status_code=UserNotFoundError)
def UserNotFound_exception_handler(request: Request, exc: UserNotFoundError) -> JSONResponse:
    raise HTTPException(status_code=404, detail=f"User {exc.user_name} not found")  # noqa: B904


@app.exception_handler(exc_class_or_status_code=HolidaysIdNotFoundError)
def HolidaysIdNotFound_exception_handler(request: Request, exc: HolidaysIdNotFoundError) -> JSONResponse:
    raise HTTPException(status_code=404, detail=f"Holidays with ID {exc.holis_id} not found")  # noqa: B904


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", port=8000, reload=True)