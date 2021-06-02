from typing import List

from ninja import Schema


class WeatherType(Schema):
    type: str


class TempRange(Schema):
    min_temp: int
    max_temp: int


class Image(Schema):
    url: str
    redirect_url: str
    weather_type: List[WeatherType]
    temp_range: TempRange = None


