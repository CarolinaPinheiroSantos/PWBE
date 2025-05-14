from rest_framework import serializers
from .models import Professor, Disciplinar, ResevaAmbiente
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        dados = super().validate(attrs)
        dados['usuario'] = {
            'nome' : self.user.username
        }
        return dados

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class DisciplinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplinar
        fields = '__all__'

class ResevaAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResevaAmbiente
        fields = '__all__'