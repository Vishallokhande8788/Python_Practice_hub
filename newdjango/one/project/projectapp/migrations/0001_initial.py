# Generated by Django 5.2.3 on 2025-07-09 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("ename", models.CharField(max_length=100)),
                ("esal", models.FloatField()),
                ("eadd", models.CharField(max_length=100)),
            ],
        ),
    ]
