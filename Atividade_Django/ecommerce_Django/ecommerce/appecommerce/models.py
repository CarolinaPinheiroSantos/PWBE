from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length = 20)
    valor = models.FloatField()
    descricao = models.TextField()
    imagem = models.ImageField()

    def __str__(self):
        return self.nome
