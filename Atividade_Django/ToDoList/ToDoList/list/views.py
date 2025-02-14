from django.shortcuts import render
from .models import List

def lista_list(request):
    listas = List.objects.all()
    return render(request, 'list/listas.html', {'listas': listas})