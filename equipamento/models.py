from django.db import models


class Equipamento(models.Model):
    status_opcao = [
        ("01", "Disponivel"),
        ("02", "Indisponivel"),
    ]

    id_equipamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    patrimonio = models.CharField(unique=True, max_length=50)
    codigo = models.IntegerField(unique=True)
    situacao = models.CharField(max_length=15)
    observacao = models.CharField(max_length=150)
    status = models.CharField(choices=status_opcao, default="01", max_length=2)
