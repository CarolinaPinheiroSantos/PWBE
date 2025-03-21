from django.shortcuts import render
from . models import Eventos
from . serializers import EventosSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from datetime import datetime, timedelta

@api_view(['GET'])
def mostrar_eventos(request):
    categoria = request.query_params.get('categoria')
    data = request.query_params.get('data')
    quantidade = request.query_params.get('quantidade')
    ordenar = request.query_params.get('ordenar')

    queryset = Eventos.objects.all()

    if categoria:
        queryset = queryset.filter(categoria=categoria)
    if data:
        try:
            data = datetime.strptime(data, "%Y-%m-%d").date()  
            queryset = queryset.filter(data__date=data)  
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    if quantidade:
        try:
            quantidade = int(quantidade)
            queryset = queryset[:quantidade] 
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    if ordenar:
        queryset = queryset.order_by(ordenar)
    serializer = EventosSerializer(queryset, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def adicionar_eventos(request):
    if request.method == 'POST':
        serializer = EventosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def mudar_eventos(request, pk):
    try:
        evento = Eventos.objects.get(pk=pk)
    except Eventos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventosSerializer(evento, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def apagar_eventos(request, pk):
    try:
        eventos = Eventos.objects.get(pk=pk)
    except eventos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    eventos.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def eventos_proximos(request):
    agora = datetime.now()
    futuro_proximo = agora + timedelta(days=7)
    queryset = Eventos.objects.filter(data_hora__gte=agora, data_hora__lte=futuro_proximo)
    serializer = EventosSerializer(queryset, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def cada_eventos(request, pk):
    try:
        evento = Eventos.objects.get(pk=pk)
    except Eventos.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = EventosSerializer(evento)
    return Response(serializer.data, status=status.HTTP_200_OK)