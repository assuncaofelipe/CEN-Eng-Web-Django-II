# Generated by Django 4.2.1 on 2023-05-15 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamento', '0002_alter_equipamento_situacao_alter_equipamento_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='situacao',
            field=models.CharField(choices=[('1', 'Bom'), ('2', 'Regular'), ('2', 'Ruim')], default='1', max_length=2),
        ),
    ]
