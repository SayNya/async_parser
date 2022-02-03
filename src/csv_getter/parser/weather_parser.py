from bs4 import BeautifulSoup

from src.csv_getter.parser.abstract_parser import AbstractParser


class WeatherParser(AbstractParser):

    async def parse_content(self, html, *args, **kwargs):
        bs = BeautifulSoup(html, 'html.parser')

        url, dte = args
        times = bs.find_all('tr', class_='time')

        weather = []
        for tm in times:
            temperature = list(
                x.strip() for x in tm.find('td', class_='temp').get_text().split('\n') if not x.isspace())
            state = tm.find('td', class_='icon').get_text().strip()
            data = tm.find_all('td', class_='data')
            pressure = data[0].get_text().strip().split('…')
            humidity = data[1].get_text().strip().split('…')
            wind_speed = data[2].get_text().strip().split('…')
            wind_direction = tm.find('td', class_='dir').get_text().strip()

            weather.append([
                dte,
                temperature[0],
                temperature[1],
                temperature[2],
                state,
                pressure[0],
                pressure[1],
                humidity[0],
                humidity[1],
                wind_speed[0],
                wind_speed[1],
                wind_direction,
                url
            ])
        return weather
