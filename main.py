from endpoints.holidays_handlers import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router=router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="main:app", port=8000, reload=True)