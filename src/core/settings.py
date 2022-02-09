import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_uri: str = r'postgresql+asyncpg://user:password@localhost:5432/db'


env_file = '.env' if os.environ.get('ENV', 'dev') else None

settings = Settings(_env_file=env_file)
