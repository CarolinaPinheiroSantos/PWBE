from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="API Gerenciamento escola",
        default_version='v1',
        description="Documentação da API de Gerenciamento de escola",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="pinheirocarol0506@gmail.com"),
        license=openapi.License(name="Carolina Pinheiro dos Santos"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('escola.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]