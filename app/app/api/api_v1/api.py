from fastapi import APIRouter

from app.api.api_v1.endpoints import conferences, talks

api_router = APIRouter()
# api_router.include_router(login.router, tags=["login"])
api_router.include_router(
    conferences.router, prefix="/conferences", tags=["conferences"])
api_router.include_router(
    talks.router, prefix="/talks", tags=["talks"])
