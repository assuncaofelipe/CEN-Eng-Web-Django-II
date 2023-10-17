from django.db import models
from django.utils import timezone

class Equipamento(models.Model):
    status_opcao = [
        ("0", "Indisponível"),
        ("1", "Disponível"),
    ]

    situacao_opcao = [
        ("1", "Bom"),
        ("2", "Regular"),
        ("3", "Ruim"),
    ]

    id_equipamento = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, verbose_name="Nome do Equipamento")
    patrimonio = models.CharField(unique=False, max_length=50, blank=True, verbose_name="Patrimônio")
    codigo = models.CharField(unique=True, max_length=50, verbose_name="Código do Equipamento")
    situacao = models.CharField(choices=situacao_opcao, default="1", max_length=2, verbose_name="Situação do equipamento")
    observacao = models.CharField(max_length=150, blank=True, verbose_name="Observações")
    status = models.CharField(choices=status_opcao, default="1", max_length=2, verbose_name="Disponibilidade")
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nome
