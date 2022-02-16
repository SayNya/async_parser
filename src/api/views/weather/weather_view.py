from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from src.containers.container import Container
from src.orm.schemas.queries.weather import WeatherParameters
from src.orm.schemas.responses.weather import WeatherResponse
from src.services.weather.weather_service import WeatherService

router = APIRouter(
    prefix='/weather'
)


@router.get(
    '/json',
    status_code=200,
    responses={
        404: {'description': 'Not Found'},
    },
    tags=['weather']
)
@inject
async def read_weather_json(
        parameters_schema: WeatherParameters = Depends(),
        weather_service: WeatherService = Depends(Provide[Container.weather_service])) -> list[WeatherResponse]:
    weather_json = await weather_service.get_weather_json(parameters_schema)
    return weather_json


@router.get(
    '/csv',
    status_code=200,
    responses={
        404: {'description': 'Not Found'},
    },
    tags=['weather']
)
@inject
async def read_weather_csv(
        parameters_schema: WeatherParameters = Depends(),
        weather_service: WeatherService = Depends(Provide[Container.weather_service])) -> StreamingResponse:
    weather_csv = await weather_service.get_weather_csv(parameters_schema)

    return weather_csv
