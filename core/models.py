from django.db import models

# Create your models here.

class Cursos(models.Model):
    descricao = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=10, decimal_places=2)