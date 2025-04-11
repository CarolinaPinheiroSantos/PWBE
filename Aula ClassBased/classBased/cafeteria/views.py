from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import Cafeteria
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework import serializers, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class CafeteriaPagina(PageNumberPagination):
    page_size = 3
    page_query_param = 'tam_size'
    max_page_size = 15

class CafeteriaListCreateAPIView(ListCreateAPIView):
    queryset = Cafeteria.objects.all()
    serializer_class = CafeteriaSerializer
    pagination_class = CafeteriaPagina

    def get_queryset(self): # como filtrar http://127.0.0.1:8000/cafeteria/?nome=capu
        queryset = super().get_queryset()
        nome = self.request.query_params.get('nome')
        if nome:
            queryset = queryset.filter(nome__icontains=nome)
        return queryset
    
    def perform_create(self, serializer):
        if serializer.validated_data['preco'] < 0:
            raise serializers.ValidationError("O valor nao pode ser menor que zero")
        serializers.save()

class CafeteriaRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Cafeteria.objects.all()
    serializer_class = CafeteriaSerializer
    lookup_field = 'pk' #por padrão já é pk

    def put(self, request, *args, **kwargs):
        preco = request.data.get('preco')
        if preco < 50:
            #jeitinho gambiarra:
            # request.data_mutable = True
            # request.data['tamanho'] = 'extra grande'
            # request.data_mutable = False

            data = request.data.copy()
            data['tamanho'] = 'Extra grande'
            request._full_data = data

        return super().put(request, request, *args, **kwargs)
    
class LoginView(CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exeption=True)

        usuario = serializer.valited_data['usuario']
        usuario_serializer = DonaCafeteria(usuario)

        return Response({
            'usuario' : usuario_serializer.data,
            'refresh' : serializer.validated_data['resfresh'],
            'access': serializer.validated['access']
        }, status =status.HTTP_200_OK)
