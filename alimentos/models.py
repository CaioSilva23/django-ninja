from django.db import models

# Create your models here.

class Alimento(models.Model):
    nome = models.CharField(max_length=25)
    qtde = models.IntegerField()


    def __str__(self) -> str:
        return self.nome