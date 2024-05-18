from fastapi import FastAPI
from endpoints import router

app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=False)