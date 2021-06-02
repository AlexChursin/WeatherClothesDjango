from django.db import models


class WeatherType(models.Model):
    type = models.CharField('тип погоды', max_length=200)

    class Meta:
        verbose_name = 'Тип погоды'
        verbose_name_plural = 'Типы погоды'

    def __str__(self):
        return self.type


class TempRange(models.Model):
    min_temp = models.IntegerField('min_temp', max_length=50)
    max_temp = models.IntegerField('max_temp', max_length=50)

    class Meta:
        verbose_name = 'Диапазон температур (включительно)'
        verbose_name_plural = 'Диапазоны температур'

    def __str__(self):
        return f" от {self.min_temp} до {self.max_temp} °С"


def allWeatherType():
    return WeatherType.objects.all()


class Image(models.Model):
    url = models.CharField('url', max_length=250)
    redirect_url = models.CharField('ссылка на магазин', max_length=250, default='', blank=True)
    weather_type = models.ManyToManyField(WeatherType, default=allWeatherType, blank=True)
    temp_range = models.ForeignKey(TempRange, on_delete=models.CASCADE)

    def __str__(self):
        return self.url[:30]

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
