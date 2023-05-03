from django.urls import path
from .views import *
# from classifiers import classifier
urlpatterns = [
    path("main/", main),
    path("add-data/", addData),
    path("get-data/", getData),
]