from fastapi import APIRouter
from starlette.responses import StreamingResponse

from src.orm.schemas.queries.weather import WeatherParameters
from src.services.weather.weather_service import WeatherService

router = APIRouter(
    prefix='/weather'
)


@router.get(
    '/csv',
    status_code=200,
    responses={
        404: {'description': 'Not Found'},
    }
)
async def read_weather_csv(params: WeatherParameters) -> StreamingResponse:
    weather = WeatherService(params.path)
    return await weather.get_csv()


@router.get(
    '/json',
    status_code=200,
    responses={
        404: {'description': 'Not Found'},
    }
)
async def read_weather_csv(params: WeatherParameters):
    weather = WeatherService(params.path)
    return await weather.get_json()
