from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import Professor, Disciplinar, ResevaAmbiente
from .serializers import ProfessorSerializer, ProfessorCadastroSerializer, DisciplinarSerializer, ResevaAmbienteSerializer, LoginSerializer
from .permissions import IsGestor
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

#Login
class Login(TokenObtainPairView):
    serializer_class = LoginSerializer

# Professores

class ProfessorlistarAlterarDeletar(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsGestor]
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    lookup_field = 'pk' 

    def perform_update(self, serializer):
        ni = serializer.validated_data.get('NI')
        if Professor.objects.filter(NI=ni).exists():
            raise serializers.ValidationError({'NI': 'Já existe um professor cadastrado com este NI.'})
        serializer.save()

class ProfessorCriar(CreateAPIView):
    permission_classes = [IsGestor]
    queryset = Professor.objects.all()
    serializer_class = ProfessorCadastroSerializer

    def perform_create(self, serializer):
        ni = serializer.validated_data.get('NI')
        if Professor.objects.filter(NI=ni).exists():
            raise serializers.ValidationError({'NI': 'Já existe um professor cadastrado com este NI.'})
        serializer.save()

class Professorlistar(ListAPIView):
    permission_classes = [IsGestor]
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

    def perform_create(self, serializer):
        ni = serializer.validated_data.get('NI')
        if Professor.objects.filter(NI=ni).exists():
            raise serializers.ValidationError({'NI': 'Já existe um professor cadastrado com este NI.'})
        serializer.save()

#Disciplina e Reservas Professor 
class DisciplinarProfessor(ListAPIView):
    serializer_class = DisciplinarSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Disciplinar.objects.filter(professor_resposavel__user=self.request.user)
    
class ReservaProfessor(ListAPIView):
    serializer_class = ResevaAmbienteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ResevaAmbiente.objects.filter(professor_resposavel__user=self.request.user)

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