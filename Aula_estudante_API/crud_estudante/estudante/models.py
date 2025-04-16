from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    curso = models.CharField(max_length=100)
    instituicao = models.CharField(max_length=100)
    rm = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nome}-{self.rm}"