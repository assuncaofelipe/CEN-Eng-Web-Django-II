from django.db import models
from equipamento.models import Equipamento
from django.utils import timezone


class Emprestimo(models.Model):
    
    DEVOLVIDO = 'D'
    EM_ANDAMENTO = 'E'

    STATUS_EMPRESTIMO_CHOICES = [
        (DEVOLVIDO, 'Devolvido'),
        (EM_ANDAMENTO, 'Emprestado'),
    ]

    curso_opcao = [
        ("0", "Engenharia de Software"),
        ("1", "Sistemas de Informação"),
        ("2", "Engenharia de Produção"),
    ]
    id_emprestimo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=250, verbose_name="Responsável")
    matricula = models.IntegerField(unique=True, verbose_name="Matrícula")
    curso = models.CharField(choices=curso_opcao, default="0", max_length=2, verbose_name="Curso")
    equipamento = models.ForeignKey(Equipamento, on_delete=models.CASCADE, verbose_name="Equipamento")
    data_emprestimo = models.DateField(verbose_name="Data de Empréstimo", default=timezone.now)
    data_devolucao = models.DateField(verbose_name="Data de DEvolução")
    observacao = models.CharField(max_length=500, blank=True, verbose_name="Observações")
    status_emprestimo = models.CharField(max_length=1, choices=STATUS_EMPRESTIMO_CHOICES, default=EM_ANDAMENTO)

    def status_emprestimo_legivel(self):
        return "Devolvido" if self.status_emprestimo == Emprestimo.DEVOLVIDO else "Emprestado"
