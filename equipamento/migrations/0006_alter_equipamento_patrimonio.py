# Generated by Django 4.2.1 on 2023-06-26 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipamento', '0005_alter_equipamento_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipamento',
            name='patrimonio',
            field=models.CharField(max_length=50),
        ),
    ]