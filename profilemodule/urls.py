from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.index),
    path('send/', views.send_message, name='send_message'),
    path('update/', views.update_data, name='update_data'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
