from django.db import models

class Eventos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_hora = models.DateTimeField()
    local = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, 
                                 choices=[('musica', "Música"),('palestra','Palestra'),('workshop', 'Workshop')])
    

    def __str__(self):
        return self.nome