import uvicorn
from fastapi import FastAPI
from app.api.v1 import router as v1
from app.config import settings

app = FastAPI(title="IsCoolGPT")
app.include_router(v1)

@app.get("/")
async def root():
    return {"service": "IsCoolGPT", "env": settings.ENV}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=settings.HOST, port=settings.PORT, reload=(settings.ENV=="development"))
