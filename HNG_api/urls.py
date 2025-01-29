from django.urls import path
from .views import my_HNG_api

urlpatterns = [
    path("info/", my_HNG_api, name="HNG_api"),
]