from django.db import models
from equipamento.models import Equipamento


class Emprestimo(models.Model):
    id_emprestimo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250)
    matricula = models.IntegerField(unique=True)
    curso = models.CharField(max_length=250)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField('Inicio')
    data_devolucao = models.DateTimeField('Fim')
    observacao = models.CharField(max_length=500)
