from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('cafeteria/', CafeteriaListCreateAPIView.as_view(), name = 'cafeteria-list-create'),
    path('cafeteria/<int:pk>', CafeteriaRetrieveUpdateDestroyAPIView.as_view(), name = 'cafeteria-Retrieve-Update-Destroy')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)