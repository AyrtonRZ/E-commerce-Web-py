# Generated by Django 4.0.5 on 2022-09-02 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_produto_categoria_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.URLField(blank=True, null=True),
        ),
    ]
