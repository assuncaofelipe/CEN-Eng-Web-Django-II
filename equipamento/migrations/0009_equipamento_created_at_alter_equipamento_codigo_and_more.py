# Generated by Django 4.2.1 on 2023-10-17 00:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamento', '0008_alter_equipamento_observacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipamento',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 17, 0, 47, 39, 97902, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='codigo',
            field=models.CharField(max_length=50, unique=True, verbose_name='Código do Equipamento'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='nome',
            field=models.CharField(max_length=50, verbose_name='Nome do Equipamento'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='observacao',
            field=models.CharField(blank=True, max_length=150, verbose_name='Observações'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='patrimonio',
            field=models.CharField(blank=True, max_length=50, verbose_name='Patrimônio'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='situacao',
            field=models.CharField(choices=[('1', 'Bom'), ('2', 'Regular'), ('3', 'Ruim')], default='1', max_length=2, verbose_name='Situação do equipamento'),
        ),
        migrations.AlterField(
            model_name='equipamento',
            name='status',
            field=models.CharField(choices=[('0', 'Indisponível'), ('1', 'Disponível')], default='1', max_length=2, verbose_name='Disponibilidade'),
        ),
    ]