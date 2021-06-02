from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode
from django.utils.safestring import mark_safe

from .models import TempRange, Image, WeatherType


# Register your models here.
@admin.register(WeatherType)
class WeatherTypeAdmin(admin.ModelAdmin):
    search_fields = ("type",)



@admin.register(TempRange)
class TempRangeAdmin(admin.ModelAdmin):
    search_fields = ("min_temp", "max_temp",)
    # list_display = (  "view_image_link",)
    # #
    # def view_image_link(self, obj):
    #     count = Image.objects.annotate(temp_range=Count('image'))
    #     return count
    #
    # view_image_link.short_description = "Images"


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    search_fields = ("temp_range__min_temp", "temp_range__max_temp", "weather_type__type")
    list_display = ['image', 'temp_range', 'weather_types_set', 'redirect_url']

    def weather_types_set(self, obj):
        return "\n".join([p.type for p in obj.weather_type.all()])

    def image(self, obj):
        return format_html('<img src="{}"  width="auto" height="100" />'.format(obj.url))
    readonly_fields = ['image']
