from dotenv import find_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str
    head_url: str


settings = Settings(_env_file=find_dotenv())
