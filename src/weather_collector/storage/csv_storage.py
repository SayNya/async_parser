import os
import time

import aiofiles
from dotenv import load_dotenv, find_dotenv

from src.weather_collector.storage.abstract_storage import AbstractStorage

load_dotenv(find_dotenv())


class CSVStorage(AbstractStorage):
    def __init__(self):
        self.generated_path = \
            fr'{os.environ.get("PATH_TO_SAVE_DATA")}\weather_{time.strftime("%Y%m%d-%H%M%S")}.csv'

    async def save_content(self, content):
        async with aiofiles.open(f'{self.generated_path}', mode='a', encoding='UTF8') as f:
            await f.write('date;day_time;t_min;t_max;state;pressure_min;pressure_max;humidity_min;'
                          'humidity_max;wind_speed_min;wind_speed_max;wind_direction;url\n')
            for dta in content:
                await f.write(f'{";".join(dta)}\n')
        return self.generated_path
