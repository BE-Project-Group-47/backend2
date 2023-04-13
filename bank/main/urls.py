from django.urls import path
from .views import *

urlpatterns = [
    path("main/", main),
    path("add-data/", addData),
    path("get-data/", getData),
]