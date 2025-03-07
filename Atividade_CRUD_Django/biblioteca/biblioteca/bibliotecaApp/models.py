from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    ano = models.IntegerField()

    def __str__(self):
        return self.titulo
    
    def __str__(self):
        return f'{self.titulo} por {self.autor}'

    class Meta:
        verbose_name_plural = "Livros"