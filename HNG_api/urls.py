from django.urls import path
from .views import my_Hng_api

urlpatterns = [
    path("", my_Hng_api, name="HNG_api"),
]