from time import time

import aiofiles

from src.storage.abstract_storage import AbstractStorage


class CSVStorage(AbstractStorage):
    def __init__(self, path='data'):
        self.generated_path = f'../../{path}/{round(time() * 1000)}_weather'

    async def save_content(self, content):
        for day_time in ('ночь', 'утро', 'день', 'вечер'):
            async with aiofiles.open(f'{self.generated_path}_{day_time}.txt', mode='a', encoding='UTF8') as f:
                await f.write(f'{str(content[day_time])}\n')
                print(content[day_time]['date'])
