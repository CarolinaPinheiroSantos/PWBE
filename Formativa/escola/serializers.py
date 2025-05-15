from rest_framework import serializers
from .models import Professor, Disciplinar, ResevaAmbiente
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User

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

class ProfessorCadastroSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Professor
        fields = ['username', 'password', 'NI', 'nome', 'email', 'telefone', 'data_nascimento', 'data_contratacao']

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')
        user = User.objects.create_user(username=username, password=password)
        professor = Professor.objects.create(user=user, **validated_data)
        return professor

class DisciplinarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplinar
        fields = '__all__'

class ResevaAmbienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResevaAmbiente
        fields = '__all__'