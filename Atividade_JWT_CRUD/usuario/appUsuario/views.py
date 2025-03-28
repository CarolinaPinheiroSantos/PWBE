from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import UserAbs
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import UserAbsSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def vizualizar_usuario_autenticado(request):
    usuario = request.user
    dados_usuario = {
        'id': usuario.id,
        'username': usuario.username,
        'email': usuario.email,
        'biografia': usuario.biografia,
        'idade': usuario.idade,
        'telefone': usuario.telefone,
        'endereco': usuario.endereco,  
        'escolaridade': usuario.escolaridade,
        'qtd_animais': usuario.qtd_animais
    }
    return Response(dados_usuario, status=status.HTTP_200_OK)

@api_view(['POST'])
def criar_usuario(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    biografia = request.data.get('biografia')
    idade = request.data.get('idade')
    telefone = request.data.get('telefone')
    endereco = request.data.get('endereco')
    escolaridade = request.data.get('escolaridade')
    qtd_animais = request.data.get('qtd_animais')

    if not username or not password:
        return Response({'Erro': 'informacao insuficiente'}, status=status.HTTP_400_BAD_REQUEST)
    
    if UserAbs.objects.filter(username = username).exists():
        return Response({'Erro': 'Username ja existe'}, status=status.HTTP_400_BAD_REQUEST)
    
    if UserAbs.objects.filter(email = email).exists():
        return Response({'Erro': 'email ja existe'}, status=status.HTTP_400_BAD_REQUEST)

    usuario = UserAbs.objects.create_user(
        username= username,
        password= password,
        email= email,
        biografia = biografia,
        idade = idade,
        telefone = telefone,
        endereco = endereco,
        escolaridade = escolaridade,
        qtd_animais = qtd_animais
    )
    return Response({'Criou seu usuario aenticado! Parabenssssss'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logar_usuario(request):
    usuario = request.data.get('username')
    senha = request.data.get('password')

    user = authenticate(username=usuario, password=senha)

    if user:
        refresh = RefreshToken.for_user(user)
        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        },status=status.HTTP_200_OK)
    else:
        return Response({'Error": "Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def alterar_usuario(request):
    serializer = UserAbsSerializer(request.user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'Atualizações salvas'}, serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deletar_usuario(request):
    usuario = request.user
    senha = request.data.get('password')

    if not senha:
        return Response(
            {'error': 'digite a senha para confirmar a exclusão'},
            status=status.HTTP_400_BAD_REQUEST
        )

    if not authenticate(username=usuario.username, password=senha):
        return Response(
            {'error': 'Senha incorreta. Não foi possível confirmar a exclusão'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    usuario.delete()
    return Response(
        {'success': 'Sua conta foi permanentemente excluída'},
        status=status.HTTP_204_NO_CONTENT
    )