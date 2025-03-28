from django.db import models
from django.contrib.auth.models import AbstractUser

class UserAbs(AbstractUser):
    biografia = models.CharField(max_length=300, blank=True, null=True )
    idade = models.PositiveIntegerField(blank=True, null=True)
    telefone = models.PositiveIntegerField(blank=True, null=True)
    endereco = models.TextField(max_length=100, blank=True, null=True )
    escolaridade = models.CharField(max_length=20, 
                                    choices=[('EF', "Ensino Fundamental"),('EM','Ensino Médio'),('ES', 'Ensino Superior'), ('PG' ,'Pós-Graduação')],
                                    blank=True, 
                                    null=True)
    qtd_animais = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.username