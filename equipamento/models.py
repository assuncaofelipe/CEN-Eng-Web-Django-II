from django.db import models


class Equipamento(models.Model):
    status_opcao = [
        ("0", "Indisponivel"),
        ("1", "Disponivel"),
    ]

    situacao_opcao = [
        ("1", "Bom"),
        ("2", "Regular"),
        ("2", "Ruim"),
    ]

    id_equipamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    patrimonio = models.CharField(unique=True, max_length=50)
    codigo = models.IntegerField(unique=True)
    situacao = models.CharField(
        choices=situacao_opcao, default="1", max_length=2)
    observacao = models.CharField(max_length=150)
    status = models.CharField(choices=status_opcao, default="1", max_length=2)

    def __str__(self):
        return self.nome
