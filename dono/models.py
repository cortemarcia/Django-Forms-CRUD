from django.db import models

# Create your models here
class Dono(models.Model):
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=30)

    def __str__(self):
        return self.nome