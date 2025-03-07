from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .form import livroForm

def livro_read(request):
    livros = Livro.objects.all()
    return render(request, "livro_read.html", {'livros': livros})

def livro_create(request):
    if request.method == 'POST':
        form = livroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('livro_read')
    else:
        form = livroForm()

    return render(request, 'livro_form.html', {'form': form})

def livro_update(request, pk):
    livros = get_object_or_404(Livro, pk=pk)

    if request.method == 'POST':
        form = livroForm(request.POST, instance=livros)
        if form.is_valid():
            form.save()
            return redirect('livro_read')
    else:
        form =livroForm(instance=livros)
    return render(request, 'livro_form.html', {'form': form})    

def livro_delete(request, pk):
    livros = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livros.delete()
        return redirect('livro_read')
    return render(request, 'livro_delete.html', {'livros':livros})

def livro_pesquisar(request):
    query = request.GET.get('q')
    livros = Livro.objects.none()

    if query:
        livros = Livro.objects.filter(titulo__icontains=query) | Livro.objects.filter(autor__icontains=query)
    
    return render(request, 'livro_pesquisar.html', {'livros': livros, 'query': query})