from typing import List

from django.shortcuts import get_list_or_404
from ninja import NinjaAPI
from . import models, schemas
api = NinjaAPI()


@api.get("/images", response=List[schemas.Image])
def get_images(request, temp: float = 0, weather_type: str = 'Rain'):
    all_temps = models.TempRange.objects.filter(min_temp__lte=round(temp), max_temp__gte=round(temp))
    images = models.Image.objects.filter(temp_range=all_temps[0]).filter(weather_type__type=weather_type)
    return get_list_or_404(images)
