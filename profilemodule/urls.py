from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.say_hello),
    path("home2/", views.index2),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
