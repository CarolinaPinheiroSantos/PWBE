from django.urls import path
from . import views

urlpatterns = [
    path('usuario/', view=views.vizualizar_usuario_autenticado),
    path('usuario/criar', view=views.criar_usuario),
    path('usuario/logar', view=views.logar_usuario),
    path('usuario/alerar', view=views.alterar_usuario),
    path('usuario/deletar', view=views.deletar_usuario),
]