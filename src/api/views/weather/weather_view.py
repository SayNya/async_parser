from datetime import date

from fastapi import APIRouter, Depends

from src.orm.schemas.queries.weather import WeatherParameters
from src.orm.schemas.responses.weather import WeatherResponse
from src.services.weather.weather_service import WeatherService

router = APIRouter(
    prefix='/weather'
)


@router.get(
    '',
    status_code=200,
    response_model=WeatherResponse,
    responses={
        404: {'description': 'Not Found'},
    }
)
async def read_weather(parameters_schema: WeatherParameters = Depends(),
                       weather_service: WeatherService = Depends()) -> WeatherResponse:

    a = await weather_service.get_weather(parameters_schema)
    return a
