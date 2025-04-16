from django.urls import path
from . import views

urlpatterns = [
    path('aluno/', views.listar_alunos),
    path('aluno/criar/', views.criar_aluno),
    path('aluno/<int:pk>/', views.detalhe_aluno),
    path('aluno/alterar/<int:pk>', views.alterar_aluno),
    path('aluno/deletar/<int:pk>', views.deletar_aluno)
]