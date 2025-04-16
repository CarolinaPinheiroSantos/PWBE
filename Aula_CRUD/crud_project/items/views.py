from django.shortcuts import render, redirect, get_object_or_404
from .models import item  
from .form import itemForm

def item_read(request):
    item = item.objects.all() 
    return render(request, "item_read.html", {'items': item})

def item_create(request):
    if request.method == 'POST':
        form = itemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_read')
    else:
        form = itemForm()

    return render(request, 'item_form.html', {'form': form})

def item_update(request, pk):
    item = get_object_or_404(item, pk=pk)
    if request.method == 'PUT':
        form = itemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_read')
        else:
            form =itemForm(instance=item)
        return render(request, 'item_form.html', {'form': form})    
    
def item_delete(request, pk):
    item = get_object_or_404(item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_read')
    return render(request, 'item_confirm_delete.html', {'item':item})

