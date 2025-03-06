from django.shortcuts import render, redirect, get_object_or_404
from .models import Livro
from .form import livroForm
from .form import LivroSearchForm

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
    form = LivroSearchForm(request.GET)
    livros = Livro.objects.all()

    if form.is_valid():
        if form.cleaned_data['titulo']:
            livros = livros.filter(titulo__icontains=form.cleaned_data['titulo'])
        if form.cleaned_data['autor']:
            livros = livros.filter(autor__icontains=form.cleaned_data['autor'])
        if form.cleaned_data['ano']:
            livros = livros.filter(ano=form.cleaned_data['ano'])

    return render(request, 'livro_search.html', {'form': form, 'livros': livros})