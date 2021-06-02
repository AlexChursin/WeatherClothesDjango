from django.contrib import admin
from django.urls import path

from weather_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.api.urls)
]
