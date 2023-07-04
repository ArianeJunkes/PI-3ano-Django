# Generated by Django 4.2.3 on 2023-07-04 19:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("livraria", "0002_rename_descricao_livro_titulo"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="autores",
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name="livro",
            name="categoria",
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name="livro",
            name="editora",
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name="livro",
            name="isbn",
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name="livro",
            name="titulo",
            field=models.CharField(max_length=255),
        ),
    ]