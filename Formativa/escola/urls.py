from django.urls import path
from .views import *

urlpatterns = [
    path('login/', view=Login.as_view()),
    path('professor/<int:pk>', view=ProfessorlistarAlterarDeletar.as_view()),
    path('professor/', view=Professorlistar.as_view()),
    path('professor/criar/', view=ProfessorCriar.as_view()),
    path('professor/disciplinas/', view=DisciplinarProfessor.as_view()),
    path('professor/reservas/', view=ReservaProfessor.as_view()),
    path('disciplina/<int:pk>', view=DisciplinarlistarAlterarDeletar.as_view()),
    path('disciplina/', view=DisciplinarlistartudoCriar.as_view()),
    path('reseva/<int:pk>', view=ResevaAmbientelistarAlterarDeletar.as_view()),
    path('reserva/', view=ResevaAmbientelistartudoCriar.as_view()),
]