from dotenv import find_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    database_uri: str


settings = Settings(_env_file=find_dotenv())
