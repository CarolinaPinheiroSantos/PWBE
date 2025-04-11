from rest_framework import serializers
from .models import Cafeteria, DonaCafeteria
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

class CafeteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafeteria
        fields = '__all__'

class DonaCafeteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonaCafeteria
        fields = '__all__'

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get['username']
        password = attrs.get['password']
        if username and password:
            usuario = authenticate(request=self.context.get('request'), username=username, password=password)
            if not usuario:
                mensagem = "Credencial não identificada"
                raise serializers.ValidationError(mensagem, code='authorization')

            if not usuario.is_active:
                mensagem = "Conta desativada"
                raise serializers.ValidationError(mensagem, code='authorization')

            refrech = RefreshToken.for_user(usuario)

            attrs['usuario'] = usuario
            attrs['refrech'] = str(refrech)
            attrs['access'] = str(refrech.access_token)

            return attrs
    
        else:
            mensagem = 'username ou senha não inseridos'
            raise serializers.ValidationError(mensagem, code='authorization')

        
                        
