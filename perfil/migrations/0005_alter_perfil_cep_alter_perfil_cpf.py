# Generated by Django 4.0.5 on 2022-09-12 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_alter_perfil_complemento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='cep',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
    ]
