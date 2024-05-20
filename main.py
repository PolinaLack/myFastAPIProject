from endpoints import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router=router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)