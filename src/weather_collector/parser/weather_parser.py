from bs4 import BeautifulSoup

from src.weather_collector.parser.abstract_parser import AbstractParser


class WeatherParser(AbstractParser):

    async def parse_content(self, html: bytes, *args, **kwargs) -> list[dict]:
        bs = BeautifulSoup(html, 'html.parser')

        url, current_date = args

        day_times = bs.find_all('tr', class_='time')

        weather = []
        for day_time in day_times:
            temperature = [
                x.strip() for x in day_time.find('td', class_='temp').get_text().split('\n') if not x.isspace()
            ]
            conditions = [
                cond.strip() for cond in day_time.find('td', class_='icon').get_text().strip().split(',')
            ]

            data = day_time.find_all('td', class_='data')
            pressure = data[0].get_text().strip().split('…')
            humidity = data[1].get_text().strip().split('…')
            wind_speed = data[2].get_text().strip().split('…')
            wind_direction = day_time.find('td', class_='dir').get_text().strip()
            weather.append({
                'date': current_date,
                'day_time': temperature[0],
                't_min': int(temperature[1]),
                't_max': int(temperature[2]),
                'conditions': conditions,
                'pressure_min': int(pressure[0]),
                'pressure_max': int(pressure[1]),
                'humidity_min': int(humidity[0]),
                'humidity_max': int(humidity[1]),
                'wind_speed_min': int(wind_speed[0]),
                'wind_speed_max': int(wind_speed[1]),
                'wind_direction': wind_direction,
                'url': url
            })
        return weather
