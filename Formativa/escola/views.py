from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import Professor, Disciplinar, ResevaAmbiente
from .serializers import ProfessorSerializer, DisciplinarSerializer, ResevaAmbienteSerializer, LoginSerializer
from .permissions import IsGestor
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView

class Login(TokenObtainPairView):
    serializer_class = LoginSerializer

# Professores
class ProfessorlistarAlterarDeletar(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsGestor]
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    lookup_field = 'pk' 


# Get/Post dos professores
class ProfessorlistartudoCriar(ListCreateAPIView):
    permission_classes = [IsGestor]
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    
#Disciplinar
class DisciplinarlistarAlterarDeletar(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsGestor]
    queryset = Disciplinar.objects.all()
    serializer_class = DisciplinarSerializer
    lookup_field = 'pk' 

class DisciplinarlistartudoCriar(ListCreateAPIView):
    permission_classes = [IsGestor]
    queryset = Disciplinar.objects.all()
    serializer_class = DisciplinarSerializer   

#Reserva Sala 

class ResevaAmbientelistarAlterarDeletar(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsGestor]
    queryset = ResevaAmbiente.objects.all()
    serializer_class = ResevaAmbienteSerializer
    lookup_field = 'pk' 

class ResevaAmbientelistartudoCriar(ListCreateAPIView):
    permission_classes = [IsGestor]
    queryset = ResevaAmbiente.objects.all()
    serializer_class = ResevaAmbienteSerializer 