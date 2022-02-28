from dotenv import find_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    head_url: str
    database_url: str

    celery_broker_url: str


settings = Settings(_env_file=find_dotenv())
