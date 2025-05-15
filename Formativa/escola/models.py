from django.db import models
from django.contrib.auth.models import User

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='professor')
    NI = models.CharField(max_length=20)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    data_contratacao = models.DateField()

class Disciplinar(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    carga_horario = models.IntegerField()
    descricao = models.TextField()
    professor_resposavel = models.ForeignKey(Professor, on_delete=models.CASCADE)

class ResevaAmbiente(models.Model):
    data_inicio = models.DateField()
    data_termino = models.DateField()
    periodo = [
        ('manha','Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite')
    ]
    sala_reservada = models.TextField()
    professor_resposavel = models.ForeignKey(Professor, on_delete=models.CASCADE)
    disciplinas_associadas = models.ForeignKey(Disciplinar, on_delete=models.CASCADE)
