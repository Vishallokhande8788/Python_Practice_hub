# Generated by Django 5.2.3 on 2025-07-11 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("pname", models.CharField()),
                ("price", models.FloatField()),
                ("quantity", models.IntegerField()),
            ],
        ),
    ]
