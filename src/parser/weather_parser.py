from bs4 import BeautifulSoup

from src.parser.abstract_parser import AbstractParser


class WeatherParser(AbstractParser):
    async def parse_content(self, html, url):
        bs = BeautifulSoup(html, 'html.parser')

        times = bs.find_all('tr', class_='time')

        dte = url.split('/')[-1]
        print(len(times))
        weather = []
        test = []
        for tm in times:
            temperature = list(
                x.strip() for x in tm.find('td', class_='temp').get_text().split('\n') if not x.isspace())
            state = tm.find('td', class_='icon').get_text().strip()
            data = tm.find_all('td', class_='data')
            pressure = data[0].get_text().strip().split('…')
            humidity = data[1].get_text().strip().split('…')
            wind_speed = data[2].get_text().strip().split('…')
            wind_direction = tm.find('td', class_='dir').get_text().strip()

            weather.append({
                'date': dte,
                'day_time': safe_list_get(temperature, 0, '-'),
                't_min': safe_list_get(temperature, 1, '-'),
                't_max': safe_list_get(temperature, 2, '-'),
                'state': state,
                'pressure_min': safe_list_get(pressure, 0, '-'),
                'pressure_max': safe_list_get(pressure, 1, '-'),
                'humidity_min': safe_list_get(humidity, 0, '-'),
                'humidity_max': safe_list_get(humidity, 1, '-'),
                'wind_speed_min': safe_list_get(wind_speed, 0, '-'),
                'wind_speed_max': safe_list_get(wind_speed, 1, '-'),
                'wind_direction': wind_direction,
                'url': url
            })
            test.append([
                dte,
                safe_list_get(temperature, 0, '-'),
                safe_list_get(temperature, 1, '-'),
                safe_list_get(temperature, 2, '-'),
                state,
                safe_list_get(pressure, 0, '-'),
                safe_list_get(pressure, 1, '-'),
                safe_list_get(humidity, 0, '-'),
                safe_list_get(humidity, 1, '-'),
                safe_list_get(wind_speed, 0, '-'),
                safe_list_get(wind_speed, 1, '-'),
                wind_direction,
                url
            ])
        print(len(test), test)
        return test


def safe_list_get(l, idx, default):
    try:
        return l[idx]
    except IndexError:
        return default
