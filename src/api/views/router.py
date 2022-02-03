from fastapi import APIRouter
from src.api.views.weather.weather_view import router as weather_router

api_router = APIRouter(
    prefix='/api/v1'
)

api_router.include_router(weather_router)
