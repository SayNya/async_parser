import csv
import os
import time

import aiofiles

from src.storage.abstract_storage import AbstractStorage
from src.utils.utils import get_project_root


class CSVStorage(AbstractStorage):
    def __init__(self, path='data'):
        self.generated_path = \
            fr'{get_project_root()}\{path}\weather_{time.strftime("%Y%m%d-%H%M%S")}'

    async def save_content(self, content):
        print(content)
        async with aiofiles.open(f'{self.generated_path}.csv', mode='a', encoding='UTF8') as f:
            await f.write('date;day_time;t_min;t_max;state;pressure_min;pressure_max;humidity_min;'
                          'humidity_max;wind_speed_min;wind_speed_max;wind_direction;url\n')
            for dta in content:
                print(dta)
                await f.write(f'{";".join(dta)}\n')
