from dependency_injector import containers, providers

from src.core.settings import settings
from src.orm.async_database import AsyncDatabase
from src.orm.repositories import *
from src.services.csv.csv_service import CSVService
from src.services.weather.weather_service import WeatherService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            'src.api.views.weather.weather_view',
        ]
    )

    async_database = providers.Singleton(AsyncDatabase, db_url=settings.database_url)

    weather_repository = providers.Factory(
        WeatherRepository,
        session_factory=async_database.provided.session,
    )
    day_time_repository = providers.Factory(
        DayTimeRepository,
        session_factory=async_database.provided.session,
    )
    condition_repository = providers.Factory(
        ConditionRepository,
        session_factory=async_database.provided.session,
    )
    wind_direction_repository = providers.Factory(
        WindDirectionRepository,
        session_factory=async_database.provided.session,
    )
    weather_condition_repository = providers.Factory(
        WeatherConditionRepository,
        session_factory=async_database.provided.session,
    )

    csv_service = providers.Factory(
        CSVService
    )

    weather_service = providers.Factory(
        WeatherService,
        weather_repository=weather_repository,
        day_time_repository=day_time_repository,
        condition_repository=condition_repository,
        wind_direction_repository=wind_direction_repository,
        weather_condition_repository=weather_condition_repository,
        csv_service=csv_service
    )
