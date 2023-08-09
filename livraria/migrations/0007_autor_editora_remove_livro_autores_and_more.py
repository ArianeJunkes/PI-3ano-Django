# Generated by Django 4.2.3 on 2023-08-09 14:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("livraria", "0006_remove_livro_categoria_livro_categoria"),
    ]

    operations = [
        migrations.CreateModel(
            name="Autor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Editora",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name="livro",
            name="autores",
        ),
        migrations.RemoveField(
            model_name="livro",
            name="editora",
        ),
        migrations.AddField(
            model_name="livro",
            name="autores",
            field=models.ManyToManyField(related_name="livros", to="livraria.autor"),
        ),
        migrations.AddField(
            model_name="livro",
            name="editora",
            field=models.ManyToManyField(related_name="livros", to="livraria.editora"),
        ),
    ]
