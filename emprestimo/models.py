from django.db import models
from equipamento.models import Equipamento


class Emprestimo(models.Model):
    curso_opcao = [
        ("0", "Engenharia de Software"),
        ("1", "Sistemas de Informação"),
        ("2", "Engenharia de Produção"),
        ("3", "Engenharia Sanitária"),
        ("4", "Farmarcia"),
        ("5", "Agronomia"),
    ]
    id_emprestimo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250)
    matricula = models.IntegerField(unique=True)
    curso = models.CharField(
        choices=curso_opcao, default="0", max_length=2)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    data_emprestimo = models.DateField('Inicio')
    data_devolucao = models.DateField('Fim')
    observacao = models.CharField(max_length=500)
