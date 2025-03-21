from django.urls import path
from . import views

urlpatterns = [
    path('eventos/', views.mostrar_eventos),
    path('eventos/adicionar', views.adicionar_eventos),
    path('eventos/mudar/<int:pk>', views.mudar_eventos),
    path('eventos/deletar/<int:pk>', views.apagar_eventos),
    path('eventos/proximos/', views.eventos_proximos),
    path('eventos/detalhar/<int:pk>', views.cada_eventos),
]