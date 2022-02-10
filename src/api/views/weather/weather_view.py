from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from src.orm.schemas.queries.weather import WeatherParameters
from src.orm.schemas.responses.weather import WeatherResponse
from src.services.weather.weather_service import WeatherService

router = APIRouter(
    prefix='/weather'
)


@router.get(
    '/json',
    status_code=200,
    response_model=list[WeatherResponse],
    responses={
        404: {'description': 'Not Found'},
    }
)
async def read_weather(parameters_schema: WeatherParameters = Depends(),
                       weather_service: WeatherService = Depends()) -> list[WeatherResponse]:
    weather = await weather_service.get_weather_json(parameters_schema)
    return weather


@router.get(
    '/csv',
    status_code=200,
    responses={
        404: {'description': 'Not Found'},
    }
)
async def read_weather(parameters_schema: WeatherParameters = Depends(),
                       weather_service: WeatherService = Depends()) -> StreamingResponse:
    stream = await weather_service.get_weather_csv(parameters_schema)

    response = StreamingResponse(iter([stream.getvalue()]), media_type='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=export.csv'

    return response
