import io

from src.orm.schemas.responses.weather import WeatherResponse
from fastapi.responses import StreamingResponse


class CSVService:

    def convert_weather_to_csv_response(self, data_list: list) -> StreamingResponse:
        stream = io.StringIO()

        stream.write('date;day_time;t_min;t_max;conditions;pressure_min;pressure_max;humidity_min;'
                     'humidity_max;wind_speed_min;wind_speed_max;wind_direction;url\n')

        for model in data_list:
            line = self.weather_model_to_csv_line(model)
            stream.write(line)

        response = StreamingResponse(iter([stream.getvalue()]), media_type='text/csv')
        response.headers['Content-Disposition'] = 'attachment; filename=export.csv'
        return response

    @staticmethod
    def weather_model_to_csv_line(model: WeatherResponse):
        return f'{model.date};{model.day_time.title};{model.t_min};{model.t_max};' \
               f'{", ".join([x.title for x in model.conditions])};{model.pressure_min};{model.pressure_max};' \
               f'{model.humidity_min};{model.humidity_max};{model.wind_speed_min};{model.wind_speed_max};' \
               f'{model.wind_direction.direction};{model.url}\n'
