from enum import Enum


class Conditions(Enum):
    PARTLY_CLOUDY = 'малооблачно'
    SHORT_RAIN = 'кратковременный дождь'
    SNOW = 'снег'
    CLOUDY = 'облачно'
    MAINLY_CLOUDY = 'пасмурно'
    CLEAR = 'ясно'
    RAIN = 'дождь'
