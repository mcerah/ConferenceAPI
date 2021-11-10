
from fastapi import FastAPI
from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI(title="Conference API",
              openapi_url=f"{settings.API_V1_STR}/openapi.json")

app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
def read_root():
    return {"Hello": "World"}
