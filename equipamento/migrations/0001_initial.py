# Generated by Django 4.2.1 on 2023-05-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipamento',
            fields=[
                ('id_equipamento', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=50)),
                ('patrimonio', models.CharField(max_length=50, unique=True)),
                ('codigo', models.IntegerField(unique=True)),
                ('situacao', models.CharField(max_length=15)),
                ('observacao', models.CharField(max_length=150)),
                ('status', models.CharField(choices=[('01', 'Disponivel'), ('02', 'Indisponivel')], default='01', max_length=2)),
            ],
        ),
    ]
