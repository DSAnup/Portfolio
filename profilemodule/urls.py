from django.urls import path
from . import views


urlpatterns = [
    path("", views.say_hello),
    path("home2/", views.index2),
]
