from django.db import models


class Equipamento(models.Model):
    id_equipamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    patrimonio = models.CharField(unique=True, max_length=50)
