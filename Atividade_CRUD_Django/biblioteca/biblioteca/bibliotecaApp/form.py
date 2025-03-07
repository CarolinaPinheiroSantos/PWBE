from django import forms
from .models import Livro

class livroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'

class LivroSearchForm(forms.Form):
    titulo = forms.CharField(required=False, max_length=200)
    autor = forms.CharField(required=False, max_length=100)
    ano = forms.IntegerField(required=False)