from django.db import models
from django.db import models

class List(models.Model):
    descricao = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao