from src.orm.schemas.responses.weather import WeatherResponse


def weather_model_to_csv_line(model: WeatherResponse):
    return f'{model.date};{model.day_time.title};{model.t_min};{model.t_max};' \
           f'{", ".join([x.title for x in model.conditions])};{model.pressure_min};{model.pressure_max};' \
           f'{model.humidity_min};{model.humidity_max};{model.wind_speed_min};{model.wind_speed_max};' \
           f'{model.wind_direction.direction};{model.url}\n'
