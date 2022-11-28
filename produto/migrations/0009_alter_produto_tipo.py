# Generated by Django 4.0.5 on 2022-09-19 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0008_alter_produto_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('N', 'Nenhum'), ('D', 'Destaque'), ('L', 'Lançamento'), ('V', 'Mais Vendido')], default='N', max_length=1),
        ),
    ]
