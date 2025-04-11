from django.db import models
from django.contrib.auth.models import AbstractUser

class Cafeteria(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=30)
    preco = models.IntegerField()
    escolhas = [
    ("P", "pequeno" ),
    ("M", "medio"),
    ("G", "grande"),
    ("XG", 'extra grande')]
    tamanho = models.CharField(max_length=3, choices=escolhas)
    acucar = models.BooleanField()
    
    def __str__(self):
        return {self.nome}
    
class DonaCafeteria(AbstractUser):
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null = True, blank = True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username
