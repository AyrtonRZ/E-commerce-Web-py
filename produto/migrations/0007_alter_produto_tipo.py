# Generated by Django 4.0.5 on 2022-09-19 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0006_alter_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='tipo',
            field=models.CharField(choices=[('N', 'Nenhum'), ('D', 'Destaques'), ('L', 'Lançamentos'), ('V', 'Mais Vendidos')], default='N', max_length=1),
        ),
    ]
