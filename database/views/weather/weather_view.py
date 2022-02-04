from fastapi import APIRouter
from starlette.responses import StreamingResponse

from database.orm.schemas.queries import WeatherParameters
from database.services.weather.weather_service import Weather

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
    weather = Weather(params.path)
    return await weather.get_csv()


@router.get(
    '/json',
    status_code=200,
    responses={
        404: {'description': 'Not Found'},
    }
)
async def read_weather_csv(params: WeatherParameters):
    weather = Weather(params.path)
    return await weather.get_json()
