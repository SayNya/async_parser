import os
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_uri: str = ''


env_file = '.env' if os.environ.get('ENV', 'dev') else None

settings = Settings(_env_file=env_file)
